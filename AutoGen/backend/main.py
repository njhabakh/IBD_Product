from vector_store import initialize_vector_store
from backend import team

import pathlib
import time
import asyncio

async def main():
    # initializing the data store
    data_folder = "/Users/michael/PycharmProjects/2024BarclaysHackathonNew/IBD_Product/Data"
    #
    file_mapping = {
        'sec_filling': f"{data_folder}/10k/",
        'research_report': f'{data_folder}/research_reports/',
        # 'news': f'{data_folder}/news/',
    }

    start = time.time()
    initialize_vector_store(None)
    end = time.time()

    print(f"elapse time {end - start}")

    basic_info_team = team(['sec_filling_report_analysis_agent', 'report_agent'])

    result =await basic_info_team.run("What do company Amazon do")
    basic_info_team.dialog_print(result)

asyncio.run(main())