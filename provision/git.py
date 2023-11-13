from invoke import task


@task
def setup(context):
    """Set up git configuration."""
    context.run("git config --add merge.ff false")
    context.run(
        "git config blame.ignoreRevsFile .git-blame-ignore-revs",
    )
