import os
import openpyxl

def get_files(path):
    list_of_files = os.listdir(path)
    xlsx_files = csv_files = list()

    for filename in list_of_files:
        if "xlsx" in filename:
            xlsx_files.append(filename)
        if 'csv' in filename:
            csv_files.append(filename)
    
    return xlsx_files, csv_files

def get_files_with_same_headers(xlsx_files, files_directory):
    columns_headers_sets = {}
    for filename in xlsx_files:
        headers_list, _ = get_headers_and_sheet(files_directory, filename)
        name_of_key = str(headers_list)
        if name_of_key not in columns_headers_sets:
            columns_headers_sets[name_of_key] = list()
        columns_headers_sets[name_of_key].append(filename)
    
    return list(columns_headers_sets.values())

def get_headers_and_sheet(files_directory, filename):
    address_to_file = "{}/{}".format(files_directory, filename)
    wb_obj = openpyxl.load_workbook(address_to_file, read_only=True)
    sheet_obj = wb_obj.active
    headers_list = list()
    for i in range(sheet_obj.max_column):
        headers_list.append(sheet_obj.cell(row = 5, column = i+1).value)
        
    return headers_list, sheet_obj
