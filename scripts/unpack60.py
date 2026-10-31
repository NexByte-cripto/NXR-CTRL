"""Extract versioned NXR CTRL 6.0 source from an audited archive."""
import base64
import io
import tarfile
from pathlib import Path
import brotli

root = Path(__file__).resolve().parents[1]
source = root / "source" / "nxr_6_0.tar.br.base64"
raw = brotli.decompress(base64.b64decode(source.read_text(encoding="ascii").strip(), validate=True))
with tarfile.open(fileobj=io.BytesIO(raw),mode="r:") as archive:
    files=[m for m in archive.getmembers() if m.isfile()]
    for m in archive.getmembers():
        p=Path(m.name)
        if not (m.isfile() or m.isdir()) or p.is_absolute() or ".." in p.parts or len(p.parts)>3:
            raise ValueError(f"Unsafe source entry: {m.name}")
        if len(p.parts)>1 and p.parts[0]!="tests":
            raise ValueError(f"Unsupported source path: {m.name}")
    for member in files:
        path=root / member.name
        path.parent.mkdir(parents=True,exist_ok=True)
        f=archive.extractfile(member)
        if f is None: raise ValueError("Missing archive member contents")
        path.write_bytes(f.read())
print(f"Recovered {len(files)} NXR CTRL 6.0 source files")
