"""Restore NXR CTRL 5.3 source archive, rejecting unsafe paths."""
import base64
import io
import tarfile
from pathlib import Path
import brotli
root = Path(__file__).resolve().parents[1]
payload = (root/"source"/"nxr_5_3.tar.br.base64").read_text(encoding="ascii").strip()
raw = brotli.decompress(base64.b64decode(payload, validate=True))
with tarfile.open(fileobj=io.BytesIO(raw),mode="r:") as archive:
    entries=archive.getmembers()
    for item in entries:
        path=Path(item.name)
        if not item.isfile() or path.is_absolute() or ".." in path.parts or len(path.parts)>3 or (len(path.parts)>1 and path.parts[0]!="tests"):
            raise ValueError(f"Invalid archive path: {item.name}")
        dst=root/path
        dst.parent.mkdir(parents=True,exist_ok=True)
        data=archive.extractfile(item)
        if data is None: raise ValueError("Missing file contents")
        dst.write_bytes(data.read())
print("Restored",len(entries),"project files")
