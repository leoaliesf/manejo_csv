import csv

def reader_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            prueba =dict((iterable))
            data.append(prueba)
        return data
if __name__ == '__main__':
   print ('hola soy un modulo que extrae información de un archivo csv')