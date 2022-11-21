import xlsxwriter
from src import (
    get_files,
    get_headers_and_sheet,
    get_files_with_same_headers,
    )


files_directory_path = '../samples'

xlsx_files, csv_files = get_files(files_directory_path)
files_dict_with_same_headers = get_files_with_same_headers(xlsx_files, files_directory_path)

for list_of_filenames in files_dict_with_same_headers:
    if len(list_of_filenames) > 1:
        headers, sheet = get_headers_and_sheet(files_directory_path, list_of_filenames[0])
        workbook = xlsxwriter.Workbook(list_of_filenames[len(list_of_filenames)-1].split('.')[0]+"__MERGED.xlsx")
        worksheet = workbook.add_worksheet()

        # adding headers in file
        for index, header in enumerate(headers):
            worksheet.write(4, index, header)

        all_sheets_data = list()
        starting_row = 5
        for filename in list_of_filenames:
            _, sheet = get_headers_and_sheet(files_directory_path, filename)
            print(filename)
            for row in range(starting_row+1, sheet.max_row + starting_row + 1):
                data_row = list()
                for column in range(sheet.max_column):
                    data_row.append(sheet.cell(row=row, column=column+1).value)
                if all(elem is None for elem in data_row):
                    continue
                all_sheets_data.append(data_row)

        for row in all_sheets_data:
            for index, value in enumerate(row):
                worksheet.write(starting_row, index, value)
            starting_row += 1
        workbook.close()