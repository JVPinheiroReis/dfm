from pathlib import Path

from dfm.rm import rm


def push(src: Path, root: Path, owr: bool):
    tgt = root / (src.resolve()).relative_to(Path.cwd())

    if tgt.exists():
        if owr:
            rm(tgt)
        else:
            raise FileExistsError()

    tgt.parent.mkdir(parents=True, exist_ok=True)

    tgt.symlink_to(src.resolve())
