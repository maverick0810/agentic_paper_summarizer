import streamlit as st
import sys
import os

# Import your main flow
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'arxiv_paper'))
from src.arxiv_paper.main import ResearchPaperFlow, ResearchPaperState

st.title("arXiv Paper Summarizer")

query = st.text_input("Enter your arXiv research query:", value="Large Language Models in HealthCare")

if st.button("Fetch & Summarize Paper"):
    with st.spinner("Fetching and processing paper..."):
        flow = ResearchPaperFlow()
        # Run the flow with the input query
        flow.kickoff(inputs={'query': query})
        summary = flow.state.summary
    st.success("Done!")
    st.subheader("Summary")
    st.write(summary if summary else "No summary generated.")
