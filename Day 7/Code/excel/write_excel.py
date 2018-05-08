from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet['A1'] = 'Number'
sheet['B1'] = 'Name'

sheet['A2'] = 1
sheet['B2'] = 'AAA'
sheet['A3'] = 2
sheet['B3'] = 'BBB'


wb.save('test02.xlsx')
