from app.agents import create_writing_agent
from app.tasks import create_story_task
from app.langchain_llm import JulepLLM

# Create agent
# agent = create_writing_agent()
# print(f"🧠 Created agent: {agent.id}")

# # Optional: create task if needed
# task = create_story_task(agent.id)
# print(f"📝 Created task: {task.id}")

# # Use LangChain interface
# llm = JulepLLM(model=agent.model, agent_id=agent.id)
# response = llm.invoke("Write a short story about a time-traveling squirrel.")
# print("✍️ Response:\n", response)


# main.py
import os
from app.agents import create_writing_agent
from app.tasks import create_story_task
from app.langchain_llm import JulepLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.runnables import RunnableSequence
from prompts import cuisine_prompt, restaurant_dishes_prompt
os.environ["JULEP_API_KEY"] = "your-secret-api-key"

# 👷 Setup
agent = create_writing_agent()
task = create_story_task(agent.id)
llm = JulepLLM(model="cerebras/llama-4-scout-17b-16e-instruct", task_id=task.id)

# 🤖 Define a chain
prompt = PromptTemplate.from_template("Write a short story about {topic}")
chain = prompt | llm  # new LangChain style

# 🚀 Run it
response = chain.invoke({"topic": "a squirrel who time-travels"})
print("✨", response)

