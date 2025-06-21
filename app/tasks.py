import yaml
from app.julep_client import client
# from app.julep_client import agent

def create_story_task(agent_id):
    task_definition = yaml.safe_load("""
    name: Story Generator
    description: Generate a short story based on a given topic
    main:
    - prompt:
      - role: system
        content: You are a creative story writer.
      - role: user
        content: $ f'Write a short story about {steps[0].input.topic}'
    """)
    task = client.tasks.create(agent_id=agent_id, **task_definition)
    return task


def create_task_with_definition(agent_id: str, task_yaml: str):
    """
    Create a task for a given agent using a YAML task definition.

    Args:
        agent_id (str): The ID of the agent to attach the task to.
        task_yaml (str): The YAML string defining the task.

    Returns:
        Task object created via Julep API.
    """
    task_definition = yaml.safe_load(task_yaml)
    task = client.tasks.create(agent_id=agent_id, **task_definition)
    return task