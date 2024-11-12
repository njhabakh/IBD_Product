from vector_store import initialize_vector_store
from backend import team
import vector_store

import pathlib
import time
import asyncio


async def main():
    global sec_filling_db
    global research_db
    global news_db

    ### initializing the data store
    cwd = pathlib.Path.cwd()
    data_folder = f"{cwd}/../../Data"
    #
    file_mapping = {
        'sec_filling': f"{data_folder}/10k_mini/",
        'research_report': f'{data_folder}/research_reports_mini/',
        'news': f'{data_folder}/news_mini/',
    }

    initialize_vector_store(file_mapping)
    print('done with vector store init\n')

    basic_info_team = team(['sec_filling_report_analysis_agent', 'report_agent'])

    result =await basic_info_team.run("who are Google's competitors")
    basic_info_team.dialog_print(result)

# main()

asyncio.run(main())