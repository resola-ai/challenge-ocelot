from invoke import task


@task
def setup(context):
    """Set up git configuration."""
    context.run("git config --add merge.ff false")
