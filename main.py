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


@app.callback()
def callback():
    """
    Descent is a tool designed to make documentation, especially 'forensic' or
    'archaeological' documentation easier.

    The core concept is that a given directory becomes the root of a tree, sub-directories
    are branches and files are leaves.  Every directory is populated with a README and
    this system of nested READMEs is what ultimately gives shape to our documentation.

    These 'seed' READMEs can be deployed and later refactored into a single top level README.

    This makes bite-sized chunks for your documentation writing.  Navigate to
    a sub-directory and describe what's going on with the adjacent leaves and branches.

    Once you're done writing, output your documentation to whatever format you need.
    """


if __name__ == "__main__":
    app()
