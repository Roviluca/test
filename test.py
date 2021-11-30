import prefect
from prefect import task, Flow

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, JD!!")
with Flow("hello-flow-tutorial") as flow:
    say_hello()
