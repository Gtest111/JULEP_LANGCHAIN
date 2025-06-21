from langchain_core.prompts import PromptTemplate

# Step 1: Get restaurant name based on cuisine
cuisine_prompt = PromptTemplate.from_template(
    "Suggest a famous restaurant that serves {cuisine} cuisine."
)

# Step 2: Get dishes based on restaurant
restaurant_dishes_prompt = PromptTemplate.from_template(
    "List 3 popular dishes served at the restaurant named {restaurant}."
)
