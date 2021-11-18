import typer

app = typer.Typer()


@app.command()
def tree():
    """View the current directory structure"""


@app.command()
def preview():
    """Open the current state of the documentation in less"""


@app.command()
def status():
    """Stats about the current state of your documentation"""


@app.callback()
def callback():
    """Review aspects of the current project"""


if __name__ == "__main__":
    app()
