
from graficas import graficadora as grf
from transformar_csv import transformar_csv as trans
from escoger_grafica import escoge as esco
import pandas as pd

#aqui escogeras la variable analizar
esco.mensaje()
va = int(input('ingresa un numero del 1 al 6, dependiendo que deseas analizar : '))
anali = esco.analizar(va)
'''
data = trans.reader_csv('D:\proyecto_csv_python\main\FAOFP1990_2022.csv')


time_1 = list(map(lambda items: items['Date'],data))


analizado = list(map(lambda items: items[anali], data))
analizado_list = [float(i) for i in analizado]'''
# puedes obtener el mismo resultado usando pandas (debes instalar la libreria) y es mucho mas simplificado
df = pd.read_csv('D:\proyecto_csv_python\main\FAOFP1990_2022.csv')
analizado_list = df[anali].values
time_1 = df['Date']

grf.gene_bar_chart(time_1, analizado_list)
