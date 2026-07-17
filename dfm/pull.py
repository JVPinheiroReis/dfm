from pathlib import Path


def pull(src: Path, tgt: Path, owr: bool):
    src.move(tgt / src.name)
    src.symlink_to(tgt / src.name)
