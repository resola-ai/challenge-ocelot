from invoke import Collection

from provision import django, docker, git, linters, project

ns = Collection(
    linters,
    project,
    docker,
    django,
    git,
)


# Configurations for run command
ns.configure(
    dict(
        run=dict(
            pty=True,
            echo=True,
        ),
    ),
)
