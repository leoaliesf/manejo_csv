from select_1 import select as slt
from join_1 import join 
import pandas as pd
import time

while True:
    print ()
    print ()
    slt.mensaje1()
    num2 =int(input(' select what tables you are going to make joins:'))
    slt.selec_table(num2)

    print()
    print()
    slt.mensaje2()
    num1 = int(input(' select what join you are going to make:'))
    slt.select_join(num1)
   
    print()

    if num1 >=1 and num1 <=4:
        print(join.join_1(num2,slt.select_join(num1)))
        
        
    elif num1 == 5:
        slt.mensaje3()
        time.sleep(5)
        print()
        print('STEP 1')
        print (join.incomes_exercise())
        time.sleep(10)
        print()
        print('STEP 2')
        print(join.students_list())
    
    elif num1 == 6:
        slt.mensaje4()
        time.sleep(5)
        print()
        print('STEP1')
        print(join.full_table())
        time.sleep(10)
        print('STEP2')
        print(join.teacher_list(join.full_table()))


    
   
    

