def mensaje():
    print("""hola deberas escoger un valor 
    para la variable que deseas analizar
    1.Meat
    2.Dairy
    3.Cereals
    4.Oils
    5.Sugar
    6.Food.price.index
    """)

def analizar(variable2):
    if variable2 == 1:
        return 'Meat'
    elif variable2 == 2:
        return 'Dairy'
    elif variable2 == 3:
        return 'Cereals'
    elif variable2 == 4:
        return 'Oils'
    elif variable2 == 5:
        return 'Cereals'
    else:
        return 'Food.Price.Index'

if __name__ == '__main__':
    print('hola soy el modulo que escoge la variable anañizar en el tiempo')