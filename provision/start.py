from . import docker


def run_local_python(context, command: str, watchers=()):
    """Run command using local python interpreter."""
    docker.up(context)
    return context.run(
        " ".join(["python3", command]),
        watchers=watchers,
    )


run_python = run_local_python
