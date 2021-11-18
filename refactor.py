import typer

app = typer.Typer()


@app.command()
def unify():
    """Unite all the nested READMEs into a single top level file"""


@app.callback()
def callback():
    """Transform some aspect of the current project"""


if __name__ == "__main__":
    app()
