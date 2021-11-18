import typer

app = typer.Typer()


@app.command()
def minimal():
    """READMEs with headers for each file or sub-directory"""


@app.command()
def intelligent():
    """READMEs that reference stuff inside files for supported languages"""


@app.command()
def manual():
    """Choose exactly which sub-directories get READMEs"""


@app.callback()
def callback():
    """Begin your project here"""


if __name__ == "__main__":
    app()
