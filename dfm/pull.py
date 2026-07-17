from pathlib import Path

from dfm.rm import rm


def pull(src: Path, root: Path, owr: bool):
    tgt = root / (src.resolve()).relative_to(Path.home())

    if tgt.exists():
        if owr:
            rm(tgt)
        else:
            raise FileExistsError()

    tgt.parent.mkdir(parents=True, exist_ok=True)

    src.move(tgt.resolve())
    src.symlink_to(tgt.resolve())
