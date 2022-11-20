import os

def get_files(path):
    list_of_files = os.listdir(path)
    xlsx_files = csv_files = list()
    
    for filename in list_of_files:
        if "xlsx" in filename:
            xlsx_files.append(filename)
        if 'csv' in filename:
            csv_files.append(filename)
    
    return xlsx_files, csv_files