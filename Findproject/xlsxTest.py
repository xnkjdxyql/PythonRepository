import xlsxwriter

projectbook = xlsxwriter.Workbook('Book.xlsx')
worksheet = projectbook.add_worksheet('ProInfo')

worksheet.write('A1', '名称') # 向A1写入
worksheet.write('B1', '城市')
worksheet.write('C1', '开始')
worksheet.write('D1', '结束')
worksheet.write('E1', '地址')
i = 2
worksheet.write('A'+str(i),'test')

worksheet.write(5,5,55)
projectbook.close()