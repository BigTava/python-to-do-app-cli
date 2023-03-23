"""This module provides the To-Do-App-Cli CLI."""
# app/cli.py

from typing import Optional

import typer

from app import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True, # version command-line option has precedence over other commands
    )
) -> None:
    return