# 🍽️ Julep LangChain Cuisine Assistant

This project is a modular AI-powered assistant built with LangChain and Julep.ai that takes a cuisine type (like "Italian" or "Japanese") as input, recommends a restaurant for that cuisine, and then provides a list of signature dishes served at that restaurant. It demonstrates a clean architecture using LangChain's `RunnableSequence`, custom LLM integration, YAML-based task creation, and automatic agent/task ID caching.

## 🔧 Features

* Modular architecture (agent, task, executor, LLM interface, config store)
* Reuses agent and task IDs via local JSON config to avoid duplicates
* Julep Task definitions written in YAML and passed dynamically
* Uses LangChain-compatible custom `JulepLLM` class for integration
* Modern chaining syntax using `prompt1 | llm1 | transform | prompt2 | llm2`
* Input schema defined per task (e.g., "cuisine")
* Full virtual environment setup and dependency isolation

## 🚀 Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/julep-langchain-cuisine.git
cd julep-langchain-cuisine
```

2. **Set up Python virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your Julep API Key**

In `app/julep_client.py`, replace:

```python
API_KEY = "your_actual_julep_api_key"
```

with your real key.

## 🧠 How It Works

* On first run, the app creates a Julep Agent and a YAML-defined Task that takes a "cuisine" as input.
* The agent and task IDs are saved in a local config JSON file for reuse.
* Then, using LangChain’s `RunnableSequence`, it executes a 2-step pipeline:

  1. Ask: "Suggest a restaurant based on the cuisine"
  2. Ask: "Given that restaurant, what dishes is it known for?"

## 📁 Folder Structure

```
julep_langchain/
├── app/
│   ├── agents.py              # Creates and manages Julep Agents
│   ├── tasks.py               # Loads and creates YAML-based tasks
│   ├── executor.py            # Polls execution results
│   ├── langchain_llm.py       # LangChain-compatible Julep LLM
│   └── utils/
│       └── config_store.py    # Saves/loads agent/task config
├── prompts/
│   ├── cuisine_prompt.py      # Prompt for restaurant suggestion
│   └── restaurant_dishes.py   # Prompt for dishes suggestion
├── main.py                    # End-to-end pipeline logic
├── requirements.txt           # Python dependency list
└── README.md                  # This documentation
```

## ⚙️ Example: Full Pipeline

```python
final_chain = cuisine_prompt | llm1 | extract_restaurant | dishes_prompt | llm2
result = final_chain.invoke({"cuisine": "Mexican"})
```

### Output

```
Suggested Restaurant: El Camino Real
Top Dishes:
- Chicken Enchiladas
- Tacos al Pastor
- Churros con Chocolate
```

## 🧹 Extend This Project

* Use real APIs (Yelp, Zomato) instead of AI-suggested restaurants
* Add optional fields like location, price range, or dietary needs
* Convert it into a chatbot using LangChain AgentExecutor
* Deploy with FastAPI or Gradio for a user-facing app

## ✅ Requirements

* Python 3.10 or higher
* Julep Python SDK
* LangChain v0.1.17+
* PyYAML

## 📜 License

MIT License

---

Built with ❤️ using LangChain and Julep by \Yajuvendrasinh Chudasama.
