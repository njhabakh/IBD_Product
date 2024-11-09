### How to run the backend

example code in main.py

1. Vector_store
   1. initialize your data folder path 
   2. run initialize_vector_store(), two options
      1. passing the dict of your file_mapping
      2. passing None, then vector store will be loaded from a coded location
2. Team creation and run
   1. create the team by calling your_team = team( particapants_list ), where the particapants_list should be a list containing some of the following:
      1. sec_filling_report_analysis_agent: retrieve information from sec_filing database
      2. research_report_analysis_agent: retrieve information from research database
      3. news_analysis_agent: retrieve infromation from news database
      4. stock_price_analysis_agent: retrieve information from stock price database
      5. report_agent: generating report
   2. run your query with your_team.run(query)


### TODOs:
1. currently the document RAG is still basic, I just used get_relevant_document(), more advanced RAG method can be applied
2. More advance prompts to be added and connected to the frontend
3. HTML data parsing functionality to be added 
4. stock_price functionality to be tests