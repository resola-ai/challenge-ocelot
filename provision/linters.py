from invoke import Exit, UnexpectedExit, task
from rich import print
from rich.panel import Panel

BASE_FOLDERS = "apps provision"


@task
def flake8(context, path=BASE_FOLDERS):
    context.run(f"python -m flake8 {path}")


@task
def all(context, path=BASE_FOLDERS):
    linters = [flake8]
    failed = []
    for linter in linters:
        try:
            linter(context, path)
        except UnexpectedExit:
            failed.append(linter.__name__)
    if failed:
        msg = f"Linters failed: {', '.join(map(str.capitalize, failed))}"
        print(Panel(msg, style="yellow bold"))
        raise Exit(code=1)
