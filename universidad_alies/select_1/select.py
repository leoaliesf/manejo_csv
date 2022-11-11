# this module was made to pick the type of join you want to see and the exercises
def mensaje1():
    print(''' what tables do you want to use ?
1. Students - career
2. career - teachers
10. exit()
    ''')

def selec_table(num2):
    if num2 == 1:
        return 1
    elif num2 == 2:
       return 2     
    else:
          print('bye')
          exit()



def mensaje2():
    print("""hi, you have to pick what type of join you want to see or if you want to see the exercises
1.inner
2.left
3.right
4.Outer
5.go to exercise 1
6. go to exercise 2
10. exit
    """)
    


def select_join (num):
    if num == 1:
        return 'inner'
    elif num == 4:
       return 'outer'     
    elif num == 2:
        return 'left'
    elif num == 3:
          return 'right' 
    elif num == 5:
        return 5
    elif num == 6:
        return 6
    elif num == 10:
        exit()
    else:
        print ('select a correct number')
        exit()
        
def mensaje3 ():
    print('''
    EXERCISE 1
    step 1. incomes for each career
    step 2. students from the career with highest income''')

def mensaje4():
    print('''
    EXERCISE 2
    step 1. all tables join (full_table)
    step 2. teacher from student wiht id ==10
    ''')

if __name__ == '__main__':
    print (' i like to be module')

            
        

