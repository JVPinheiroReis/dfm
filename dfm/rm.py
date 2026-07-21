from pathlib import Path


def rm(p: Path):
    p.rmdir() if p.is_dir(follow_symlinks=False) else p.unlink()
