import typer

app = typer.Typer()


@app.callback()
def callback():
    """Review aspects of the current project"""


if __name__ == "__main__":
    app()
