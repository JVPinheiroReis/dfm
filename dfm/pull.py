from pathlib import Path


def pull(src: Path, tgt: Path, owr: bool):
    if not owr and tgt.exists():
        raise FileExistsError()

    src.move(tgt)
    src.symlink_to(tgt.resolve())
