from vector_store import initialize_vector_store
from backend import team


if __name__ == '__main__':
    # initializing the data store
    data_folder = "/Users/michael/PycharmProjects/2024BarclaysHackathonNew/IBD_Product/Data"

    file_mapping = {
        'sec_filling': f"{data_folder}/10k/",
        'research_report': f'{data_folder}/research_reports/',
        # 'news': f'{data_folder}/news/',
    }

    initialize_vector_store(file_mapping)

    basic_info_team = team(['sec_filling_report_analysis_agent', 'report_agent'])

    result = team.run("What do company Amazon do")
    team.dialog_print(result)

