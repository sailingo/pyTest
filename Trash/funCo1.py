
def printProgressBar():    #打印进度条
    from tqdm import trange
    from time import sleep
    for i in trange(100):
        sleep(0.01)


def funAdd():
    x = int(input("please input x="))

    y = int(input("please input y="))
    z = x + y
    print("x+y = ", z)

# 列表
def listFun():
    list1 = ['good', 'runoob', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]
    list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print(len(list1))
    print("list = ",list2, end = '\n---end---')

# my calculator
def myCalculator():
    status = 'c'
    tips = "\033[33m * type 'c' to continute Calculator \n" \
           + " * type 'h' to show the history\n" \
           + " * type 'q' to quit\n\033[0m" \
           + "Please input your choose# "
    history = []
    while status != 'q':
        if(status == 'h'):
            #print(history)
            showHistory(history)
            status = input(tips)
        elif(status == 'c'):
            formula = input("please input your formula:")
            try:
                result = eval(formula)
            except:
                print("\033[41m【Wrong！】Please make sure you have input the right type.\033[0m")
            else:
                content =  formula + " = " + str(result)
                history.append(content)
                print("--------------")
                print('\033[1;36m' + str(result) + '\033[0m')
                print("--------------")
                status = input(tips)
        else:
            print("You type the wrong command!\n")
            status = input(tips)

    else:
        print("bye!")


def showHistory(list):
    print("---------- cal history ---------")
    for index in range(len(list)):
        print("\033[32m["+str(index)+"] " + list[index] + "\033[0m")
    print("---------- cal history ---------")

