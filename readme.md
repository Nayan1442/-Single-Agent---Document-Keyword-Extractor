# 📄 LangGraph Keyword Extractor

---

## 🚀 Features

- ✅ Extracts predefined keywords with context from any input text  
- 🤖 Uses local LLM (e.g., `mistral`) via Ollama — no API keys needed  
- 🔄 Modular agent-based design using LangGraph  
- 💡 JSON output format for easy integration  

---

## 📂 Project Structure

.
├── input.txt # Input file with raw text
├── main.py # Main script with LangGraph pipeline
├── output/
│ └── result.json # Extracted keywords with context
└── README.md # You're here!


---

## 🧠 How It Works

1. Reads `input.txt` containing raw text.
2. The LangGraph pipeline runs a single **LLM-based agent** to:
   - Search for configured keywords.
   - Extract their surrounding context.
3. Outputs results to `output/result.json`.

---

## 🔧 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- Supported Ollama model (e.g., `mistral`)

---

## 📦 Installation

# 1. Clone the repository
git clone https://github.com/yourusername/keyword-extraction-agent.git
cd keyword-extraction-agent

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

## Run the pipeline
python main.py
