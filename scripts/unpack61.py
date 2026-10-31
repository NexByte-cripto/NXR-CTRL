"""Extract NXR CTRL 6.1 source archive into repository root with path safety."""
from __future__ import annotations
import base64
import io
import tarfile
from pathlib import Path
import brotli

root = Path(__file__).resolve().parents[1]
source = root / "source" / "nxr_6_1.tar.br.base64"
encoded = source.read_text(encoding="ascii").strip()
raw = brotli.decompress(base64.b64decode(encoded, validate=True))
with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
    files = []
    for item in archive.getmembers():
        path = Path(item.name)
        if (not item.isfile() or path.is_absolute() or ".." in path.parts
            or len(path.parts) > 3
            or (len(path.parts) > 1 and path.parts[0] != "tests")):
            raise ValueError("Invalid archive item: "+item.name)
        files.append(item)
    for item in files:
        target=root/item.name
        target.parent.mkdir(parents=True,exist_ok=True)
        member=archive.extractfile(item)
        if member is None:
            raise ValueError("Missing entry "+item.name)
        target.write_bytes(member.read())
print("Restored NXR CTRL 6.1 source files:",len(files))
