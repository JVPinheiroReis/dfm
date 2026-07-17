import typer
from pathlib import Path
from typing import Annotated

from dfm.pull import pull
from dfm.push import push

app = typer.Typer()


@app.command("pull")
def cli_rpull(
    src_path: Annotated[Path, typer.Argument()],
    tgt_path: Annotated[Path, typer.Argument()] = Path.cwd(),
    overwrite: Annotated[bool, typer.Option()] = False,
):
    pull(src_path, tgt_path, overwrite)


@app.command("push")
def cli_rpush(
    src_path: Annotated[Path, typer.Argument()],
    root_path: Annotated[Path, typer.Argument()] = Path.home(),
    overwrite: Annotated[bool, typer.Option()] = False,
):
    push(src_path, root_path, overwrite)


if __name__ == "__main__":
    app()
