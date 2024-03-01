import streamlit as st
from services.sendIssue import sendIssue

# Page config
st.set_page_config(
    page_title="CodePulse",
    page_icon="🧊",
    layout="centered",
)


# Header
st.header("CodePulse")
st.caption("A simple, feedback platform for devs")
st.divider()

# Feedback form
issueType = st.selectbox("Choose Issue type", ["Feedback", "Bug", "Feature Request"])
issueName = st.text_input("Issue Title")
issueDescription = st.text_area("Issue Description")
if st.button("Submit Issue"):
    sendIssue(
        service="notion",
        title=issueName,
        description=issueDescription,
        issue_type=issueType,
        file_links=[]
    )
