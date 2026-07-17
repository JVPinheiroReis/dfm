import typer
from pathlib import Path
from typing import Annotated

from dfm.cmd.pull import pull
from dfm.cmd.push import push

app = typer.Typer()


@app.command("pull")
def cli_pull(
    src_path: Annotated[Path, typer.Argument()],
    tgt_path: Annotated[Path, typer.Argument()] = Path.cwd(),
    overwrite: Annotated[bool, typer.Option()] = False,
):
    pull(src_path, tgt_path, overwrite)


@app.command("push")
def cli_push(
    src_path: Annotated[Path, typer.Argument()],
    tgt_path: Annotated[Path, typer.Argument()] = Path.home(),
    overwrite: Annotated[bool, typer.Option()] = False,
):
    push(src_path, tgt_path, overwrite)


if __name__ == "__main__":
    app()
