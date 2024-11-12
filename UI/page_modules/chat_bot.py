# pages/chat_bot.py
import streamlit as st

# Create an agent that can access and use a large language model (LLM).
def create_agent():
    
    ### replace with AzureAI
    from langchain import OpenAI
    API_KEY = 'tmp-open-ai-api-key'
    llm = OpenAI(openai_api_key=API_KEY)
    return llm

# Query an agent and return the response as a string.
def query_agent(agent, query):

    prompt = (
        """
            For the following query, if it requires drawing a table, reply as follows:
            {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

            If the query requires creating a bar chart, reply as follows:
            {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            If the query requires creating a line chart, reply as follows:
            {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

            There can only be two types of chart, "bar" and "line".

            If it is just asking a question that requires neither, reply as follows:
            {"answer": "answer"}
            Example:
            {"answer": "The title with the highest rating is 'Gilead'"}

            If you do not know the answer, reply as follows:
            {"answer": "I do not know."}

            Return all output as a string. Please do not reply any code, only text message is fine.

            All strings in "columns" list and data list, should be in double quotes,

            For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}

            Lets think step by step.

            Below is the query.
            Query: 
            """
        + query
    )

    # Run the prompt through the agent.
    response = agent.invoke(prompt)

    # Convert the response to a string.
    return response.__str__()


# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


def show_chat_bot():
    st.write("## Chat Bot Section")
    query = st.text_area("Insert your query")
    # st.text_input("Enter your question or prompt here:")
    # st.write(response)

    if st.button("Submit Query", type="primary"):
        # Create an agent from the CSV file.
        llm = create_agent()
    
        # Query the agent.
        response = query_agent(agent=llm, query=query)

        # Add user query and model response to chat history
        st.session_state.chat_history.append({"sender": "User", "message": query})
        st.session_state.chat_history.append({"sender": "AI", "message": response})
        
        # Clear the input box after submission
        st.session_state.user_query = ""
    
    # Display the chat history
    for entry in st.session_state.chat_history:
        align = "left" if entry["sender"] == "AI" else "right"
        
        st.markdown(
            f"<div style='text-align: {align};'>"
            f"<div style=' display: inline-block; max-width: 70%; padding: 10px; border-radius: 10px;"
            f"margin: 5px; background-color: {'#E8F5E9' if align == 'left' else '#f0f0f0'};'>"
            f"<strong>{entry['sender']}:</strong> {entry['message']}</div>",
            unsafe_allow_html=True,
        )
        