import pandas as pd

career = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/career.xlsx')
students = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/students.xlsx')
teachers = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/teachers.xlsx')

def joins(num2,num1):
    if num1 == 1:
        return  pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how=num2)
    elif num1 == 2:
        return  pd.merge(career, teachers, left_on=['id'],right_on=['carrera_id'], how=num2)
    else:
        print('bye')


if __name__=='__main__':
    print ('module -- join')

