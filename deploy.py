import typer
import os

app = typer.Typer()


@app.command()
def minimal(obey_gitignore: bool = True):
    """READMEs with headers for each file or sub-directory"""
    files_to_ignore = [".git"]
    if obey_gitignore and os.path.isfile(".gitignore"):
        with open(".gitignore") as file:
            files_to_ignore += [item.strip().replace('/', '') for item in file.readlines()]

    for current_dir, sub_dirs, files in os.walk('.', topdown=True):
        if current_dir != '.' and current_dir.split('/')[1] in files_to_ignore:
            continue
        else:
            with open(current_dir + "/test_README.md", 'x') as readme:
                readme.write(f"# {current_dir}" + "\n" * 3)
                readme.write(f"## FILES:" + "\n" * 2)
                for file in files:
                    readme.write(f"### {file}" + "\n" * 2)
                readme.write(f"## SUB-DIRECTORIES:" + "\n" * 2)
                for sub_dir in sub_dirs:
                    readme.write(f"### {sub_dir}" + "\n" * 2)


@app.command()
def intelligent():
    """READMEs reference stuff inside files for supported languages"""


@app.command()
def manual():
    """Choose exactly which sub-directories get READMEs"""


@app.callback()
def callback():
    """Begin your project here"""


if __name__ == "__main__":
    app()
