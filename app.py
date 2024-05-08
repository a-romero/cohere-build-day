import os
from tools.get_repair_quotes import get_repair_quotes
from tools.get_vehicle_info import get_vehicle_info
from tools.search_internet import search_internet
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate

from langchain_cohere.chat_models import ChatCohere

cohere_api_key=os.getenv('COHERE_API_KEY')

chat = ChatCohere(model="command-r-plus", temperature=0.3, cohere_api_key=cohere_api_key)

# Preamble
preamble = """
Use all tools that are available to answer the question.
You are equipped with an internet search tool, a vehicle info lookup service and a get repair quote API tool
"""

# Prompt
prompt = ChatPromptTemplate.from_template("{input}")

# Create the ReAct agent
agent = create_cohere_react_agent(
    llm=chat,
    tools=[search_internet, get_repair_quotes, get_vehicle_info],
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent, tools=[search_internet, get_repair_quotes, get_vehicle_info], verbose=True
)

result = agent_executor.invoke(
    {
        "input": "Vehicle with registrationnumber FG4234IJ has got its door damaged. What garage can repair it cheapest and how much would it cost?",
        "preamble": preamble,
    }
)

print(result)