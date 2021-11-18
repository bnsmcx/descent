import typer

app = typer.Typer()


@app.command()
def build():
    """Generate documentation"""
    pass


if __name__ == "__main__":
    app()
