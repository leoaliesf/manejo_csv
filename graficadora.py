import matplotlib.pyplot as plt

def gene_pie_chart(values, labels):
    fig1, ax = plt.subplots()
    ax.pie(values, labels= labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def gene_bar_chart(values, labels):
    plt.bar(values, values, align='center', alpha=0.5)
    plt.xticks(values, labels)
    plt.title('bar chart')
    plt.show()

if __name__ == '__main__':
    print ('hola me gusta ser un modulo')