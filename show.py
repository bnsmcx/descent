import typer

app = typer.Typer()


@app.command()
def show():
    """Review aspects of the current project"""
    pass


if __name__ == "__main__":
    app()
