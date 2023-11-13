from invoke import Collection

from provision import ci, django, docker, git, linters, project, tests

ns = Collection(
    linters,
    project,
    docker,
    django,
    git,
    ci,
    tests,
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
