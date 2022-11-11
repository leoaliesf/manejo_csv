import pandas as pd
career = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/career.xlsx')
students = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/students.xlsx')
teachers = pd.read_excel('D:/proyecto_csv_python/universidad_alies/Excel_data/teachers.xlsx')



def join_1(num2,num1):
    if num2 == 1:
        return  pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how=num1)
    elif num2 == 2:
        return  pd.merge(career, teachers, left_on=['id'],right_on=['carrera_id'], how=num1)
    else:
        print('bye')

def incomes_exercise():
    inner_join = pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how='inner')
    incomes= inner_join[['programa','valor']]
    return incomes.groupby('programa').sum().reset_index().sort_values('valor', ascending=False)

def students_list():
    inner_join = pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how='inner')
    estudiante = inner_join[inner_join['programa']=='odontologia'] #condition to bring all the students from career "odontologia"
    return estudiante.loc[:,'estudiante']

def full_table():
    inner_join = pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how='inner')
    return pd.merge(inner_join, teachers, left_on=['id_y'], right_on=['carrera_id'], how= 'inner')

def teacher_list(full_table):
    teachers= full_table[full_table['id_x'] == 10]
    return teachers.loc[:, ['programa', 'nombre']]

    

if __name__=='__main__':
    print ('module -- join')

