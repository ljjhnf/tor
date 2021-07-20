import xlsxwriter
import pymysql

def get_data(sql):
    db=pymysql.connect(host="localhost", user="root", password="#a6161569a", database="pythondb", charset="utf8")
    cursor=db.cursor()
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    db.close()
    return results


def write_data_to_excel():
    sql="select * from user"
    results=get_data(sql)
    workbook=xlsxwriter.Workbook('file1.xlsx')
    worksheet=workbook.add_worksheet()
    for i in range(len(results)):
        for j in range(len(results[i])):
            worksheet.write(i,j,str(results[i][j]))
    
    workbook.close()

if __name__=='__main__':
    write_data_to_excel()
    