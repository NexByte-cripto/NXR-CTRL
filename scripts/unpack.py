"""Restore audited release sources archived as a tar.br payload."""
import base64
import io
import tarfile
from pathlib import Path
import brotli

root = Path(__file__).resolve().parents[1]
payload = (root / "source" / "nxr_5_2_1.tar.br.base64").read_text(encoding="ascii").strip()
raw = brotli.decompress(base64.b64decode(payload, validate=True))
with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
    entries = archive.getmembers()
    for item in entries:
        relative = Path(item.name)
        if item.isdir():
            continue
        if not item.isfile() or relative.is_absolute() or len(relative.parts) != 1 or ".." in relative.parts:
            raise ValueError(f"Unsafe archive member: {item.name}")
        dest = root / relative
        dest.write_bytes(archive.extractfile(item).read())
print(f"Restored {len([item for item in entries if item.isfile()])} release files")
