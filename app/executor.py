# app/executor.py
import time
from app.julep_client import client

# def run_execution(task_id, topic: str):
#     execution = client.executions.create(task_id=task_id, input={"topic": topic})
    
#     while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
#         time.sleep(1)

#     if result.status == "succeeded":
#         return result.output["choices"][0]["message"]["content"]
#     else:
#         raise Exception(f"Execution failed: {result.error}")

# import time
# from julep import Julep

def run_execution(task_id: str, input_data: dict) -> str:
    """
    Run a Julep execution for a given task with dynamic input.
    
    Args:
        client (Julep): An instance of the Julep client.
        task_id (str): The ID of the task to execute.
        input_data (dict): Dictionary of inputs matching the task's schema.

    Returns:
        str: Output message content from the AI assistant.

    Raises:
        Exception: If execution fails or output format is unexpected.
    """
    execution = client.executions.create(task_id=task_id, input=input_data)

    while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
        time.sleep(1)

    if result.status == "succeeded":
        try:
            return result.output["choices"][0]["message"]["content"]
        except Exception as e:
            raise Exception(f"[Parsing Error]: {e} | Raw Output: {result.output}")
    else:
        raise Exception(f"Execution failed: {result.error}")
