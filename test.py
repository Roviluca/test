import prefect
from prefect import task, Flow

@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello, JD!!")

@task
def say_hello_to_isobel():
    logger = prefect.context.get("logger")
    logger.info("Hello, Isobel!")

    
with Flow("hello-flow-tutorial") as flow:
    say_hello()
    say_hello_to_isobel()
