import streamlit as st
from page_modules.profiler import show_profiler
from page_modules.chat_bot import show_chat_bot
from page_modules.valuation import show_valuation
from page_modules.overview import show_overview  # Import the Overview function

import pandas as pd

# Sidebar layout for "Company/ Ticker" input and Start button
st.sidebar.markdown("### Company/ Ticker")
company_ticker = st.sidebar.text_input("Enter Company/Ticker", key="company_ticker")

# Start button below the company ticker input
if st.sidebar.button("Start"):
    st.session_state["started"] = True

# Initialize session state for "started" if not already set
if "started" not in st.session_state:
    st.session_state["started"] = False
    
# Navigation using st.radio for persistent state
st.sidebar.markdown("## Navigation")
page = st.sidebar.radio("Go to", ["Profiler", "Chat Bot", "Valuation"])

# Only display the content if "Start" button has been clicked
if st.session_state["started"]:

    # Set the selected page in session state for tracking
    st.session_state["page"] = page

    #st.markdown('<div class="main-content">', unsafe_allow_html=True)
    # Display the selected page content
    if st.session_state["page"] == "Profiler":
        show_profiler()
    elif st.session_state["page"] == "Chat Bot":
        show_chat_bot()
    elif st.session_state["page"] == "Valuation":
        show_valuation()
    #st.markdown('</div>', unsafe_allow_html=True)

else:
    # Display a message prompting the user to click the Start button
    st.write("Please enter a Company/Ticker and click the Start button to begin.")
    show_overview()
    
# File uploader in the sidebar
st.sidebar.markdown("### Upload a File")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx", "pdf"], key="file_uploader")

# Display uploaded file info (for demonstration)
if uploaded_file is not None:
    st.sidebar.write(f"Uploaded file: {uploaded_file.name}")
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        st.write("### Uploaded Excel File Content")
        st.dataframe(df)
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded CSV File Content")
        st.dataframe(df)
    elif uploaded_file.type == "application/pdf":
        st.write("PDF files cannot be displayed directly here, but they are uploaded successfully.")