from pathlib import Path


def pull(src: Path, tgt: Path, owr: bool):

    src.move_into(tgt)

    src.symlink_to(tgt / src.name)
