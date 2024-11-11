import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from page_modules.utilities import save_content_to_ppt


# Sample data for financials and geographic distribution
####
data = {
    "Region": ["North America", "Europe", "Asia"],
    "Revenue": [120000, 85000, 100000],
    "Profit": [20000, 15000, 18000]
}

df = pd.DataFrame(data)

def create_bar_chart():
    fig, ax = plt.subplots()
    ax.bar(df["Region"], df["Revenue"], color="skyblue")
    ax.set_title("Revenue by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue ($)")
    fig_path = "result/bar_chart.png"
    plt.savefig(fig_path)  # Save the chart as an image file
    plt.close(fig)
    return fig_path
####

def show_profiler():
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Profiler sub-tabs
    profiler_tabs = st.tabs(["Overview", "Financials", "Geographic Mix", "Management", "Recent News"])

    # Collect content for each tab
    content = {}
    with profiler_tabs[0]:
        content["Overview"] = "This is the company overview with a sample paragraph.\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent nec nisl vel mauris blandit interdum."
        st.write("### Overview")
        st.write(content["Overview"])

    with profiler_tabs[1]:
        content["Financials"] = "Financial Table:\n" + df.to_string()
        st.write("### Financial Table")
        st.dataframe(df)
        st.write("### Financial Bar Chart")
        chart_path = create_bar_chart()
        st.image(chart_path)

    with profiler_tabs[2]:
        content["Geographic Mix"] = "Geographic Distribution Table:\n" + df[["Region", "Revenue"]].to_string()
        st.write("### Geographic Distribution Table")
        st.dataframe(df[["Region", "Revenue"]])

    with profiler_tabs[3]:
        content["Management"] = "This section could include profiles or key information about the management team."
        st.write("### Management Information")
        st.write(content["Management"])

    with profiler_tabs[4]:
        content["Recent News"] = "1. Company launches new product.\n2. Q3 earnings report shows positive growth.\n3. Expansion into new markets."
        st.write("### Recent News")
        st.write(content["Recent News"])



    # Button to generate and download the PowerPoint file
    if st.button("Download PPT"):
        save_content_to_ppt(content, chart_path)  # Save the content to a PowerPoint file
