import json
from pathlib import Path
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnableLambda

# --- Configuration ---
KEYWORDS = ["AI", "machine learning", "agent", "language model", "token", "prompt"]
MODEL_NAME = "mistral"

# --- Load input text ---
with open("input.txt", "r", encoding="utf-8") as f:
    document_text = f.read()

# --- Agent function ---
def extract_keywords(state):
    llm = ChatOllama(model=MODEL_NAME)

    prompt = f"""
You are a keyword extraction agent.

Extract the following keywords: {", ".join(KEYWORDS)} from the text.

Return a JSON object like:
{{
  "keyword1": [{{"context": "..."}}, ...],
  "keyword2": [{{"context": "..."}}, ...]
}}

Only include keywords that are found in the text.

Text:
\"\"\"
{state['text']}
\"\"\"
"""
    response = llm.invoke(prompt)
    try:
        result_json = json.loads(response.content[response.content.find("{"):])
    except Exception as e:
        result_json = {"error": str(e)}
    return {"text": state["text"], "result": result_json}

# --- Build LangGraph ---
graph = StateGraph(dict)
graph.add_node("extract", RunnableLambda(extract_keywords))
graph.set_entry_point("extract")
graph.set_finish_point("extract")
graph.add_edge("extract", END)
app = graph.compile()

# --- Run the agent ---
output = app.invoke({"text": document_text})

# --- Save the result ---
Path("output").mkdir(exist_ok=True)
with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(output["result"], f, indent=4)

print("✅ Done! Results saved to output/result.json")
