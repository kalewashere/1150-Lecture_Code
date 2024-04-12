import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')  # make sure file name is typed exactly the same way otherwise
# it will not open, or open an incorrect file. Since file is already in directory, Pycharm may suggest it while typing.
# spreadsheets are made up of sheets rows (1, 2, 3...) columns (A, B, C..)
# cells are (row, column)
# some spreadsheets have multiple sheets, we need to make sure we are working with the correct one if there are multiple
sheet_names = workbook.sheetnames
print(sheet_names)
# to select sheet

codes_sheet = workbook.active

b2_data = codes_sheet['B2'].value  # variable for cell we want data from, .value calls that data for us
# use square brackets to obtain
print(b2_data)

c5_data = codes_sheet['C5'].value
print(c5_data)

for row in codes_sheet.rows:
    for cell in row:
        print(cell.value)  # prints by row, more organized but still not neat
print('')

for col in codes_sheet.columns:
    for cell in col:
        print(cell.value)  # similar output as above but less organized.

print('')

class_names_column = codes_sheet['C']
for cell in class_names_column:  # list of cells in column
    print(cell.value)  # will print data in entire column
print()

rooms_sheet = workbook['rooms']  # square/dictionary brackets - works the same as dictionaries

rooms_column = rooms_sheet['B']
for cell in rooms_column:
    print(cell.value)  # will print data from column called
