from pathlib import Path


def push(src: Path, root: Path, owr: bool):
    tgt = root / (src.resolve()).relative_to(Path.cwd())

    if tgt.exists():
        if owr:
            tgt.rmdir() if tgt.is_dir() else tgt.unlink()
        else:
            raise FileExistsError()

    tgt.symlink_to(src.resolve())
