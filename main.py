import pandas as pd
from src import (
    get_files,
    get_files_with_same_headers,
    )


files_directory_path = '../samples'

xlsx_files, csv_files = get_files(files_directory_path)
files_dict_with_same_headers = get_files_with_same_headers(xlsx_files, files_directory_path)