import streamlit as st
from page_modules.utilities import save_content_to_ppt

def show_valuation():
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    valuation_tabs = st.tabs(["DFC", "LBO"])

    # Content for each sub-tab within the Valuation section
    with valuation_tabs[0]:
        st.write("### Discounted Cash Flow (DFC) Analysis")
        st.write("Sample DFC analysis content and calculations.")

    with valuation_tabs[1]:
        st.write("### Leveraged Buyout (LBO) Analysis")
        st.write("Sample LBO analysis content and calculations.")

    ## Button to generate and download the PowerPoint file
    if st.button("Download PPT"):
        save_content_to_ppt(content, chart_path)  # Save the content to a PowerPoint file