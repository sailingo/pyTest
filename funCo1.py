import traceback
debug_config = 0
language_config = 1
def debug_print(debugStr , debug_level = 0):
    if debug_config == 0:
        return
    level = debug_level
    if level == 0:
        print("\033[33m[DEBUG][LEVEL=" + str(level) + "]" + str(debugStr) + "\033[0m")
    else:
        print("\033[31m[DEBUG][LEVEL=" + str(level) + "]" + str(debugStr) + "\033[0m")

def myprint(debugStr , debug_level = 0):
    level = debug_level
    if level == 0:
        print("\033[37m[MYPRINT][LEVEL=" + str(level) + "]" + '\033[36m' + str(debugStr) + "\033[0m")
    else:
        print("\033[32m[MYPRINT][LEVEL=" + str(level) + "]" + '\033[1;36m' + str(debugStr) + "\033[0m")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def printProgressBar():    #打印进度条
    from tqdm import trange
    from time import sleep
    for i in trange(100):
        sleep(0.01)

# my calculator
def myCalculator():
    status = 'c'
    if (language_config == 0):
        tips = "\033[33m * type 'c' to continute Calculator \n" \
               + " * type 'h' to show the history\n" \
               + " * type 'r' to calulator the history result\n"\
               + " * type 'q' to quit\n\033[0m" \
               + "Please input your choose# "
    #elif (language_config == 1):
    else:
        tips = "\033[33m * 按 'c' 继续执行计算 \n" \
               + " * 按 'h' 显示历史记录\n" \
               + " * 按 'r' 根据历史结果索引计算\n"\
               + " * 按 'q' 退出\n\033[0m" \
               + "请输入你的选择# "

    #history = []
    history = {}
    count = 0
    while status != 'q':
        if(status == 'h'):
            #print(history)
            showHistory(history)
            status = input(tips)
        elif(status == 'c'):
            if (language_config == 0):
                formula = input("please input your formula:")
            else:
                formula = input("请输入你的计算公式:")
            try:
                result = eval(formula)
            except:
                if (language_config == 0):
                    print("\033[41m【Wrong！】Please make sure you have input the right type.\033[0m")
                else:
                    print("\033[41m【错误！】请确认你输入正确的公式.\033[0m")
            else:
                #content =  formula + " = " + str(result)
                #history.append(content)
                #use dic to replace the str content
                dicContent = formula + ' = ' + str(result)
                history[count] = dicContent
                count += 1
                print('\033[1;36m' + str(result) + '\033[0m')
                status = input(tips)
        elif(status == 'r'):
            r_formula = input("please input your r_formula:")
            calStr = cal_the_r_formula(history, r_formula)
            #print("the result is:" + str(eval(calStr)))
            result = str(eval(calStr))
            myprint("-------------")
            myprint(result,1)
            myprint("-------------")
            history[count] = calStr + ' = ' + str(eval(calStr))
            count += 1
            status = input(tips)
        else:
            print("You type the wrong command!\n")
            status = input(tips)

    else:
        print("bye!")

#print the function name
def fun_name(status=0):
    if status == 0:
        return "[Enter Function]:" + traceback.extract_stack()[-2][2]
    elif status == 1:
        return "[Leave Function]:" + traceback.extract_stack()[-2][2]
    else:
        pass

def cal_the_r_formula(historyDic, r_formula):
    myprint(fun_name())
    debug_print(historyDic,1)
    dic = getHistoryDic(historyDic)
    calList = calSplit(r_formula)
    debug_print(calList)
    debug_print(dic)
    ret =  replace_calListIndex_to_calResult(calList, dic)
    return ret

'''  getHistoryDic(dic)
change {0:'1+7-2=6',1:'2+9-3=8'}
to
{0:'6',1:'8'}
'''
def getHistoryDic(dic):
    debug_print(fun_name())
    historyDic = dic
    debug_print(historyDic)
    newDic = {}
    for index in dic:
        formula = dic[index]
        dicIndex = index
        splitResult =  formula.split('=')[1].strip()
        newDic[dicIndex] = splitResult
    debug_print(newDic,1)
    return newDic

def showHistory(dic):
    print("---------- cal history ---------")
    debug_print(dic)
    for index in range(len(dic)):
        print("\033[32m["+str(index)+"] " + str(dic[index]) + "\033[0m")
    print("---------- cal history ---------")


def calSplit(calStr):
    str0 = calStr
    #str0 = '23+(77-33)+(66-(98+2))'
    #str0 = '23+77-33+66-98'
    #print("original cal string is:" + str0)
    #str1 = re.split('\+|\-',str0)
    #print(str1)
    cha = ''
    mylist = []
    for i in range(len(str0)):
        if str0[i] != '+' and str0[i] != '-' and str0[i] != '*' and str0[i] != '(' and str0[i] != ')' :
            cha += str(str0[i])
            #print("cha is:"+cha)
        else:
            if len(cha) != 0:
#                print("add tha num:"+cha)
                mylist.append(cha)
                cha = ''
            mylist.append(str0[i])

        if i == len(str0)-1 and len(cha) != 0:    #添加最后一个数字
            mylist.append(cha)
#        print(mylist)

    #print("after split the cal,ths result is:")
    #print(mylist)
    return mylist

def replace_calListIndex_to_calResult(callist, dic):
    debug_print(fun_name())
    myDic = dic
    debug_print("-------------")
    debug_print(dic)
    debug_print("-------------")
    debug_print(callist,1)
    newCalList = callist
    for i in range(len(callist)):
        if is_number(newCalList[i]):
            currentNum = newCalList[i]
            debug_print("is num:"+ currentNum)
            #print(myDic[int(currentNum)])
            #debug_print("myDic[" + currentNum + "]is:" + myDic[int(currentNum)])
            newCalList[i] = myDic[int(currentNum)]
    debug_print(newCalList,1)
    calStr = ""
    for i in range(len(newCalList)):
        calStr += str(newCalList[i])
    debug_print("the calStr is:-----------:" + calStr)
    debug_print(eval(calStr))
    return calStr

myCalculator()

