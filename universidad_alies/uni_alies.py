import pandas as pd
import numpy as np
career = pd.read_excel('./Excel_data/career.xlsx')
students = pd.read_excel('./Excel_data/students.xlsx')
teachers = pd.read_excel('./Excel_data/teachers.xlsx')
inner_join = pd.merge(students, career, left_on=['carrera_id'],right_on=['id'], how='inner')

inner_join.shape