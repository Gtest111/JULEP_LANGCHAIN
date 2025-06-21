from julep import Julep
from app.agents import create_agent_with_prompt
from app.tasks import create_task_with_definition
from app.langchain_llm import JulepLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.runnables import RunnableSequence
from prompts import cuisine_prompt, restaurant_dishes_prompt
from app.utils.config_store import save_agent_task_config, load_agent_task_config

# Try to load existing config
config = load_agent_task_config()

if config:
    agent_id = config["agent_id"]
    task_id = config["task_id"]
    model = config["model"]
    name = config["name"]

    llm = JulepLLM(
        model="cerebras/llama-4-scout-17b-16e-instruct",
        task_id=task_id,  # Your cuisine assistant task ID
        input_key="cuisine"
    )

    response = llm.invoke("Indian")  # 👈 This is your "Which cuisine?" input
    print(response)
else:
    agent = create_agent_with_prompt(
        name="Cuisine Assistant",
        model="cerebras/llama-4-scout-17b-16e-instruct",
        about="Suggests restaurants and dishes based on cuisine"
    )
    definition = """
name: Cuisine Explorer
description: Given a cuisine, suggest a top restaurant and its best dishes.
main:
  - prompt:
      - role: system
        content: >
          You are a food assistant who recommends restaurants and their best dishes based on a given cuisine.
          Be helpful, concise, and culturally aware.
      - role: user
        content: >
          I’m in the mood for {{ steps[0].input.cuisine }} food. Recommend one popular restaurant for that cuisine,
          and then list a few dishes that they’re known for.
input_schema:
  cuisine:
    type: string
    description: The cuisine type to explore (e.g., Italian, Thai, Japanese).
"""


    task = create_task_with_definition(agent.id, definition)
    save_agent_task_config(agent.name, agent.model, agent.id, task.id)

    llm = JulepLLM(
        model="cerebras/llama-4-scout-17b-16e-instruct",
        task_id=task.id,  # Your cuisine assistant task ID
        input_key="cuisine"
    )

    response = llm.invoke("Indian")  # 👈 This is your "Which cuisine?" input
    print(response)
