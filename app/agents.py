from app.julep_client import client

def create_writing_agent():
    agent = client.agents.create(
        name="Writing Assistant",
        model="cerebras/llama-4-scout-17b-16e-instruct",
        about="A helpful AI assistant that specializes in writing and editing."
    )
    return agent

def create_agent_with_prompt(name: str, model: str, about: str):
    """
    Creates a new Julep agent with the given name, model, and description.

    Args:
        client: Julep client object
        name (str): Name of the agent
        model (str): Model identifier (e.g., "cerebras/llama-4-scout-17b-16e-instruct")
        about (str): Short description of the agent's purpose

    Returns:
        Agent object
    """
    agent = client.agents.create(
        name=name,
        model=model,
        about=about
    )
    print(f"✅ Agent created: {agent.id}")
    return agent
