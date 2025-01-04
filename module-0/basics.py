from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


load_dotenv()

#####################################################
# Chat models
print("".join("#" for _ in range(100)))
print("Chat Models basics\n")
gpt35_chat = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo-0125")

content = "Hello World"
humman_msg = HumanMessage(content=content, name="Mohamed")

response = gpt35_chat.invoke([humman_msg])
print(response)
# response = gpt35_chat.invoke(content)
# print(response)

#####################################################
# Search Tools
print("".join("#" for _ in range(100)))
print("Search Tools\n")

from langchain_community.tools.tavily_search import TavilySearchResults

tavily_search = TavilySearchResults(max_results=3)
tavily_response = tavily_search.invoke("Who is the prophet Muhammad?")
print(tavily_response)
