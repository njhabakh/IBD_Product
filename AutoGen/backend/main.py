from vector_store import initialize_vector_store
from backend import team

import pathlib
import time
import asyncio

global sec_filling_db
global research_db
global news_db

import glob


### initializing the data store
cwd = pathlib.Path.cwd()
data_folder = f"{cwd}/../../Data"
#
file_mapping = {
    'sec_filling': f"{data_folder}/10k_mini/",
    'research_report': f'{data_folder}/research_reports_mini/',
    'news': f'{data_folder}/news_mini/',
}

if len(glob.glob(f"{cwd}/../../faiss-db/*/*.faiss")) == 0:
    initialize_vector_store(file_mapping)
else:
    initialize_vector_store(None)

print('done with vector store init\n')

async def frontend_run():

    basic_info_team = team(['news_analysis_agent', 'report_agent'])
    result =await basic_info_team.run("What's trump victory mean for google")
    basic_info_team.dialog_print(result)

# main()
asyncio.run(frontend_run())