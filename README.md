Absolutely! Here’s a professional, informative `README.md` for your project, tailored to your workflow and Streamlit UI:

---

# Agentic Paper Summarizer

A modern, agentic AI-powered tool to **search, download, extract, and summarize research papers from arXiv**—all in a single, interactive Streamlit web app.

---

## 🚀 Features

- **Search arXiv** for the most relevant research papers using your query
- **Download PDFs** automatically
- **Extract text** from downloaded papers
- **Summarize** the extracted content using prompt-engineered AI agents
- **User-friendly Streamlit UI** for seamless interaction
- **Planned:** Memory and RAG integration for even smarter research

---

## 🧠 How It Works

This project leverages [CrewAI](https://github.com/joaomdmoura/crewai) to orchestrate a team of AI agents, each with a specialized role:

1. **Fetch Agent:** Finds and downloads the most relevant papers from arXiv.
2. **Extract Agent:** Extracts text from the downloaded PDFs.
3. **Summarize Agent:** Summarizes the extracted content for quick insights.

All steps are performed sequentially and visualized in a clean Streamlit interface.


---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maverick0810/agentic_paper_summarizer.git
   cd agentic_paper_summarizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if using Poetry:
   ```bash
   poetry install
   ```

3. **Set up your environment:**
   - Add your `OPENAI_API_KEY` to a `.env` file in the root directory.

---

## ▶️ Usage

**To launch the Streamlit app:**
```bash
streamlit run app.py
```

- Enter your research query and number of papers to fetch.
- Click "Search, Extract & Summarize" and let the agents do the work!
- Download the summary or review extracted text right in the browser.

---

## 📁 Project Structure

```
arxiv_paper_streamlit/
├── app.py                  # Streamlit UI
├── src/arxiv_paper/        # Core logic, agents, tools
├── arxiv_papers/           # Downloaded PDFs
├── README.md
├── pyproject.toml
└── ...
```

---

## 🤖 Tech Stack

- Python
- Streamlit
- CrewAI
- arXiv API
- PyMuPDF (fitz) for PDF extraction

---

## 📝 Future Plans

- Integrate memory for context-aware summarization
- Add RAG (Retrieval-Augmented Generation) capabilities
- More advanced UI features

---

