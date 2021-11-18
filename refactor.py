import typer

app = typer.Typer()


@app.command()
def refactor():
    """Transform some aspect of the current project"""
    pass


if __name__ == "__main__":
    app()
