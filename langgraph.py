# %%
from typing import Annotated
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from IPython.display import Image, display
import gradio as gr
from langgraph.prebuilt import ToolNode, tools_condition
import requests
import os
from langchain_openai import ChatOpenAI
from typing import TypedDict


# %%
# Our favorite first step! Crew was doing this for us, by the way.
load_dotenv(override=True)


# %%
from langchain_community.utilities import GoogleSerperAPIWrapper

serper = GoogleSerperAPIWrapper()
serper.run("tell me about jodhpur")

# %%
from langchain.agents import Tool

tool_search =Tool(
        name="search",
        func=serper.run,
        description="Useful for when you need more information from an online search"
    )



# %%
tool_search.invoke("Central Academy CHB what is this and where it is present")

# %%
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"

def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})

# %%
tool_push = Tool(
        name="send_push_notification",
        func=push,
        description="useful for when you want to send a push notification"
    )

tool_push.invoke("Hello, me")

# %%
tools = [tool_search, tool_push]

# %%
class State(TypedDict):
    messages: Annotated[list, add_messages]

# %%
graph_builder = StateGraph(State)

# %%
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1")

llm_with_tools = llm.bind_tools(tools)   # ✅ works here

# %%
pip install langchain-ollama

# %%



def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

# %%


graph_builder.add_conditional_edges( "chatbot", tools_condition, "tools")

graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# %%
# Step 5: Compile the Graph
graph = graph_builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))

# %%
def chat(user_input: str, history):
    result = graph.invoke({"messages": [{"role": "user", "content": user_input}]})
    return result["messages"][-1].content


gr.ChatInterface(chat, type="messages").launch()

# %%
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

# %%
# Steps 1 and 2
graph_builder = StateGraph(State)


# Step 3
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1")

llm_with_tools = llm.bind_tools(tools) 

def chatbot(state: State):
    print(state)
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))

# Step 4
graph_builder.add_conditional_edges( "chatbot", tools_condition, "tools")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Step 5
graph = graph_builder.compile(checkpointer=memory)
display(Image(graph.get_graph().draw_mermaid_png()))

# %%
config = {"configurable": {"thread_id": "1"}}

def chat(user_input: str, history):
    result = graph.invoke({"messages": [{"role": "user", "content": user_input}]}, config=config)
    return result["messages"][-1].content


gr.ChatInterface(chat, type="messages").launch()

# %%
graph.get_state(config)

# %%


list(graph.get_state_history(config))

# %%
pip uninstall langgraph -y

# %%
import sys
!{sys.executable} -m pip uninstall langgraph -y

# %%
import sys
!{sys.executable} -m pip install langgraph==0.2.34

# %%
import sys
print(sys.executable)

# %%
!pip install langgraph==0.2.34

# %%
!pip install -U langgraph langchain-core

# %%



