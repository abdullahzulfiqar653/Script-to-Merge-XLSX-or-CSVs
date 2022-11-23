import xlsxwriter
from src import (
    get_files,
    get_headers_and_sheet,
    get_files_with_same_headers,
    )


files_directory_path = '..\samples'

xlsx_files, csv_files = get_files(files_directory_path)
files_dict_with_same_headers = get_files_with_same_headers(xlsx_files)

for listOfFileAdresses in files_dict_with_same_headers:
    if len(listOfFileAdresses) > 1:
        headers, header_row, sheet = get_headers_and_sheet(listOfFileAdresses[0])
        new_workbook_name = "{}__MERGED.xlsx".format(listOfFileAdresses[-1].split(".")[-2].split("\\")[-1])
        workbook = xlsxwriter.Workbook(new_workbook_name)
        worksheet = workbook.add_worksheet()

        # adding headers in file
        for index, header in enumerate(headers):
            worksheet.write(header_row-1, index, header)

        all_sheets_data = list()
        starting_row = header_row  
        print("____________________Starting Reading data____________________")
        for fileAddress in listOfFileAdresses:
            _,_, sheet = get_headers_and_sheet(fileAddress)
            print("____________________ Reading: {} ____________________".format(fileAddress))
            for row in range(starting_row+1, sheet.max_row + starting_row + 1):
                data_row = list()
                for column in range(sheet.max_column):
                    data_row.append(sheet.cell(row=row, column=column+1).value)
                if all(elem is None for elem in data_row):
                    continue
                all_sheets_data.append(data_row)
            
        print("_______________ Writing data into {} _______________".format(new_workbook_name))
        for row in all_sheets_data:
            for index, value in enumerate(row):
                worksheet.write(starting_row, index, value)
            starting_row += 1
        workbook.close()