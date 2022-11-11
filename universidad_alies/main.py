from select_1 import select as slt
from join_1 import join 

slt.mensaje1()
num2 =int(input(' type what table you are going to look:'))
slt.selec_table(num2)
slt.mensaje2()
num1 = int(input(' type what join you are going to look:'))
slt.select_join(num1)

join.joins(num1,num2)