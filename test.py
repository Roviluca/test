import prefect
from prefect import task

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, JD!!")
