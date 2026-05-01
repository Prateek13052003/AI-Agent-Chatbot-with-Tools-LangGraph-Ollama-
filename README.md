
---

# 🤖 AI Agent Chatbot (LangGraph + Ollama)

An intelligent AI chatbot built using **LangGraph** and **Ollama (Llama 3.1)** that can **think, use tools, remember conversations, and interact in real-time**.

---

## 📸 Demo

![Gradio UI](Gradio%20Image.png)
---

## 🚀 Features

* 🧠 Local LLM powered chatbot (Llama 3.1 via Ollama)
* 🔍 Real-time web search using Google Serper API
* 📲 Push notifications using Pushover API
* 🔁 Tool-calling agent workflow (LangGraph)
* 💬 Interactive chat UI with Gradio
* 🧠 Conversation memory (thread-based state management)

---

## 🛠️ Tech Stack

* Python
* LangGraph & LangChain
* Ollama (Llama 3.1)
* Gradio
* Google Serper API
* Pushover API

---

## ⚙️ Setup

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install langgraph langchain-core langchain-ollama gradio python-dotenv
```

---

## ▶️ Run

```bash
ollama run llama3.1
python your_script.py
```

---

## 🧩 How it works

* User sends a message via Gradio UI
* LangGraph agent processes the request
* LLM decides whether to:

  * answer directly
  * call search tool
  * send notification
* Memory stores conversation context

---

## 📌 Example Use Cases

* Smart assistant with real-time information
* Notification-based automation
* Tool-augmented AI systems
* Local AI agent experimentation

---

## 📄 Description

This project demonstrates a **tool-augmented AI agent** capable of reasoning, acting, and maintaining memory using a local LLM setup.

---

## ⭐ Author

**Prateek Choudhary**

---


