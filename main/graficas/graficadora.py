import matplotlib.pyplot as plt

def gene_pie_chart(values, labels):
    fig1, ax = plt.subplots()
    ax.pie(values, labels= labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def gene_bar_chart(values, labels):
    plt.bar(values, labels)
    plt.title('Food price index from 1990 to 2022')
    plt.show()

if __name__ == '__main__':
    print ('hola me gusta ser un modulo, que da una grafica')