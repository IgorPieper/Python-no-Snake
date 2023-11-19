import os
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

# pip install openai==0.28.1
# pip install langchain==0.0.330

os.environ["OPENAI_API_KEY"] = "Your key"

llm = ChatOpenAI()

def generate_travel_plan(climate_preference, budget, cultural_interests):

    prompt = f"I am planning a trip and need some suggestions. I prefer a destination with a {climate_preference} climate, my budget is {budget}, and I am interested in {cultural_interests}."

    messages = [
        SystemMessage(content="You are a helpful assistant who can plan trips."),
        HumanMessage(content=prompt),
    ]

    return llm.invoke(messages)


print(generate_travel_plan("tropical", "$1000 - $2000", "historical sites"))
print(generate_travel_plan("cold", "below $1000", "art and music festivals"))
print(generate_travel_plan("temperate", "$3000 - $5000", "outdoor adventures"))
