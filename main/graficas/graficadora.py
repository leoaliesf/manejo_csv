import matplotlib.pyplot as plt

def gene_pie_chart(values, labels):
    fig1, ax = plt.subplots()
    ax.pie(values, labels= labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def gene_xy_chart(values, labels):
    plt.plot(values, labels,  color='red')
    plt.xticks(rotation=90)
    plt.title('Food price index from 1990 to 2022')
    plt.xlabel('Time')
    plt.show()

if __name__ == '__main__':
    print ('hola me gusta ser un modulo, que da una grafica')