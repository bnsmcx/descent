import typer

app = typer.Typer()


@app.callback()
def callback():
    """Transform some aspect of the current project"""


if __name__ == "__main__":
    app()
