import re

debug_config = 1
def debug_print(debugStr , debug_level = 0):
    if debug_config == 0:
        return

    level = debug_level

    #print("debug__status = " + str(status))
    if level == 0:
        #print(type(status))
        print("\033[33m[DEBUG][LEVEL=" + str(level) + "]" + str(debugStr) + "\033[0m")
    else:
        print("\033[31m[DEBUG][LEVEL=" + str(level) + "]" + str(debugStr) + "\033[0m")
    #if status == 0:
    #    print("debug__status = " + status)
    #    print("\033[31m[DEBUG] " + str(debugStr) + "\033[0m")
    #else:
    #    print("\033[33m[DEBUG] " + str(debugStr) = "\033[0m")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def calSplit(calStr):
    str0 = calStr
    #str0 = '23+(77-33)+(66-(98+2))'
    #str0 = '23+77-33+66-98'
    print("original cal string is:" + str0)
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

#    print("after split the cal,ths result is:")
#    print(mylist)
    return mylist

def replace_calListIndex_to_calResult(callist):
    myDic = {1:111, 2:222, 3:333, 4:444, 5:455}
    newCalList = callist
    for i in range(len(callist)):
        if is_number(newCalList[i]):
            currentNum = newCalList[i]
            debug_print("is num:"+ currentNum)
            #debug_print("myDic["+currentNum+"]is:"+myDic[currentNum])
            newCalList[i] = myDic[int(currentNum)]
        else:
            pass
    debug_print(newCalList,1)
    calStr = ""
    for i in range(len(newCalList)):
        calStr += str(newCalList[i])
    debug_print(eval(calStr))


myCal = input("please input your r_cal:")
print(calSplit(myCal))
calList = calSplit(myCal)
print("------")
debug_print("calList is:"+str(calList))
print(calList)
replace_calListIndex_to_calResult(calList)

