
# Steps
- conda create --name ibd python=3.10
- conda update --name ibd <path to environment.yml file>
- Update the file for OpenAI Key
- streamlit run app.py


# To do
### Prompting
- Multimodel LLM provided with chart sample prompt


### Dataset 
- Add vector db
- Add connection to sql DB
- Add API endpoints for news sources
- Using these sources to fetch the data

### Deck and Charting
- Option 1 - Check the charting functionality inside generate_slide_content and enhance (Agent)
    - Variable python environment
    - Fixed Python environment
- Option 2 - Upload a ppt template and update it. 

### Chatbot 
- Reasoning with Q&A
- Agent to fetch the data from the vector DB, endpoints and sql DB

### Formula
- Upload excel file and get the formula and code

### Agent based architecture
- CrewAI


## Screenshots

#### Pitch Deck generator:
![Pitch deck](Images/image1.png)

#### Valuation mode:
![Sample Image](Images/image1.png)


