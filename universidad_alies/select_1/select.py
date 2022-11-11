# this module was made to pick the type of join you want to see and the exercises
def mensaje1():
    print(''' what tables do you want to use ?
1. Students - career
2. career - teachers
3. all_table
    ''')

def selec_table(num2):
    if num2 == 1:
        return 1
    elif num == 2:
       return 2     
    elif num == 3:
        return 3
    else:
          print('pick a right choice')



def mensaje2():
    print("""hi, you have to pick what type of join you want to see
1.inner
2.left
3.right
4.Outer
5.go to exercises
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
        return 'go to exercises'
    else:
        exit
        

if __name__ == '__main__':
    print (' i like to be module')

            
        

