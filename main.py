
import graficadora as grf
import transformar_csv as trans
import escoge as esco
from datetime import datetime

data = trans.reader_csv('D:\proyecto_csv_python\FAOFP1990_2022.csv')
esco.mensaje()
va = int(input('ingresa un numero del 1 al 6, dependiendo que deseas analizar : '))
anali = esco.analizar(va)

time_1 = list(map(lambda items: items['Date'],data))
time_list = [datetime.strptime(i, '%d/%m/%Y') for i in time_1]

analizado = list(map(lambda items: items[anali], data))
analizado_list = [float(i) for i in analizado]
grf.gene_bar_chart( time_1, analizado_list)
