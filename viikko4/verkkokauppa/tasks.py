from invoke import task

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def cov_rep(ctx):
    ctx.run("coverage html")