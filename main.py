#! /usr/bin/env python3
import typer

import build
import deploy
import refactor
import show

app = typer.Typer()
app.add_typer(refactor.app, name="refactor")
app.add_typer(deploy.app, name="deploy")
app.add_typer(build.app, name="build")
app.add_typer(show.app, name="show")

if __name__ == "__main__":
    app()
