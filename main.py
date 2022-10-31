
import graficadora as grf
import transformar_csv as trans

from datetime import datetime

data = trans.reader_csv('D:\proyecto_csv_python\FAOFP1990_2022.csv')
#data = list(filter(lambda items: items ['Date'] <= '01/01/2020', data))

time_1 = list(map(lambda items: items['Date'],data))
time_list = [datetime.strptime(i, '%d/%m/%Y') for i in time_1]

meat = list(map(lambda items: items['Meat'], data))
meat_list = [float(i) for i in meat]
grf.gene_bar_chart( time_1, meat_list)
