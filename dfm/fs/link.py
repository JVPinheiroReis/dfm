from pathlib import Path


def link_to(src: str, tgt: str):
    Path(src).symlink_to(tgt)
