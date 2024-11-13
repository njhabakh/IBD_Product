import streamlit as st
from page_modules.utilities import save_content_to_ppt

def show_valuation():
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    valuation_tabs = st.tabs(["DFC", "LBO"])
    # Content for each sub-tab within the Valuation section
    with valuation_tabs[0]:
        sample_dfc_str = "Sample DFC analysis content and calculations."
        
        st.write("### Discounted Cash Flow (DFC) Analysis")
        st.write(sample_dfc_str)
        agree = st.checkbox("Add DFC Analysis to presentation", 
                            value = st.session_state.get("Discounted Cash Flow Analysis", False))
      
        st.session_state["Discounted Cash Flow Analysis"] = sample_dfc_str if agree else False

    with valuation_tabs[1]:
        sample_lbo_str = "Sample LBO analysis content and calculations."
        
        st.write("### Leveraged Buyout (LBO) Analysis")
        st.write(sample_lbo_str)
        agree = st.checkbox("Add LBO Analysis to presentation", 
                            value = st.session_state.get("Leveraged Buyout Analysis", False))

        st.session_state["Leveraged Buyout Analysis"] = sample_lbo_str if agree else False