#coding:utf-8

def inputString():  #获取字符串
    paper = list(raw_input('Please input a string:'))
    head = ['*']
    if '*' in paper:
        return paper,False
    paper.append('*')
    paper = head+paper
    #print '*+paper+*',paper         #TEST
    return paper,True

def stringTorF(paper):#bool类型，判定字符串是否是由a,b,c,d四个字母构成
    i = 1
    if (paper[i] == 'a'):
        while (paper[i] != '*'):
            i += 1
            if (paper[i] == 'a'):
                continue
            else:
                if (paper[i] == '*'):
                    return False
                break
        if (paper[i] == 'b'):
            while (paper[i] != '*'):
                i += 1
                if (paper[i] == 'b'):
                    continue
                else:
                    if (paper[i] == '*'):
                        return False
                    break
            if (paper[i] == 'c'):
                while (paper[i] != '*'):
                    i += 1
                    if (paper[i] == 'c'):
                        continue
                    else:
                        if (paper[i] == '*'):
                            return False
                        break
                if (paper[i] == 'd'):
                    while (paper[i] != '*' and paper[i] == 'd'):
                        i += 1
                    if (paper[i] != '*' and paper[i] != 'd'):
                        return False
                    return True
            else:
                return False
        else:
            return False
    else:
        return False

#print stringTorF(['*','a','b','b','c','c','d','d','d','d','*'])

def backA(findABCD,i,paper): #指针后退，返回指定的未读字母a的位置
    while(paper[i]!='@'):
            i -= 1
    return i+1


def backB(findABCD,i,paper): #指针后退，返回指定的未读字母b的位置
    while(paper[i]!='#'):
            i -= 1
    return i+1

def backC(findABCD,i,paper): #指针后退，返回指定的未读字母c的位置
    while(paper[i]!='$'):
            i -= 1
    return i+1

def backD(findABCD,i,paper): #指针后退，返回指定的未读字母d的位置
    while(paper[i]!='%'):
            i -= 1
    return i+1

def back(i,paper):  #回到纸带开始
    i -= 1
    while(paper[i]!='*'):
        i -= 1
    return i+1



def forward(findABCD,i,paper): #指针前进，返回指定未读字母的位置
    while(paper[i]!=findABCD):
        i += 1
    return i



def isFinalD(findABCD,i,paper): #bool型，判定字母d是否读取完毕，是，则返回True和最后一个该字母的位置，否，则返回False和下一个要读的位置
    while(paper[i]!='%' and paper[i]!='*'):        #前进到d
        i += 1
    while(paper[i]=='%'):
        i += 1
    if(paper[i]=='*'):
        return True,i
    else:
        return False,i



def isFinalC(findABCD,i,paper): #bool型，判定字母c是否读取完毕，是，则返回True和最后一个该字母的位置，否，则返回False和下一个要读的位置
    while(paper[i]=='%' or paper[i]=='*'):
        i -= 1
    if(paper[i]=='$'):         #若c已经标记完，指针停留在第一个标记过的d，即$
        return True,i
    else:                       #若c为结束，停留在第一个未标记的c
        return False,i

def isFinalB(findABCD,i,paper): #bool型，判定字母B是否读取完毕，是，则返回True和最后一个该字母的位置，否，则返回False和下一个要读的位置
    i -= 1
    if(paper[i]!='#'):
        while ((paper[i] != '#' and paper[i] == '*')or(paper[i] != '#' and paper[i] == '%') or (paper[i] != '#' and paper[i] == '$')):
            i -= 1
        if(paper[i] == '#'):
            return True, i         #返回最后一个标记过的b的位置
        else:
            return False, i       #返回最后一个未标记的b的位置
    else:
        while(paper[i]=='#'):
            i += 1
        if(paper[i]=='$'):
            return True,i
        else:
            return False,i

def isFinalA(findABCD,i,paper): #bool型，判定字母A是否读取完毕，是，则返回True和最后一个该字母的位置，否，则返回False和下一个要读的位置
    i -=1
    if(paper[i]!='@'):
        while((paper[i]!='@' and paper[i] =='#')or(paper[i]!='@' and paper[i]=='$')or(paper[i]!='@' and paper[i]=='%') or (paper[i]!='@' and paper[i]=='*')):
            i -= 1
        if(paper[i]=='@'):
            return True,i
        else:
            return False,i
    while(paper[i]=='@'):
        i += 1
    if(paper[i]=='#'):
        return True,i
    else:
        return False,i

def reset(i,paper): #对位置i以后的非d字母复原
    print paper
    while(paper[i]=='*' or paper[i]=='a' or paper[i]=='b' or paper[i]=='c' or paper[i]=='d'):
        i += 1
    while(paper[i]=='@'):
        i += 1
    while(paper[i]=='#'):
        paper[i]='b'
        i += 1
    while(paper[i]=='$'):
        paper[i]='c'
        i += 1
    return paper,i

def readPaper(paper): #判断是否符合规则
    i = 1
    while (paper[i] == 'a'):       #第一个a扫描后标记为@，指针后移到第一个未读的b
        paper[i] = '@'
        i = forward('b',i,paper)
        while (paper[i] == 'b'):
            paper[i] = '#'
            i = forward('c',i,paper)
            while (paper[i] == 'c'):
                paper[i] = '$'
                i = forward('d',i,paper)
                paper[i] = '%'
                print paper
                boolC, i = isFinalC('c', i, paper)  # bool,判断C是否读取结束，ii为第一个标记过的d位置
                boolD, i = isFinalD('d',i,paper)  # 若C未结束，D结束，则拒绝该字符串
                print paper[i]
                if (boolD == True and boolC == False):
                    return False
                if (boolC == True):
                    break
                else:
                    i = backC('c', i,paper)
            boolB, i = isFinalB('b',i,paper)  # test B is done,指针停留在最后一个b
            boolD, i = isFinalD('d', i,paper)      #此时指针停留在d最后*或者d
            if (boolD == True and boolB == False):  # 若B未结束，D结束，则拒绝该字符串
                return False
            if (boolB == True):
                break
            if (boolB == False):
                i = backB('b',i,paper)
                paper,i = reset(i,paper)      #此时指针到d
                i = backB('b',i,paper)        #指针退回到未读的b
        boolA, i = isFinalA('a', i,paper)  # Test A id done
        boolD, i = isFinalD('d', i,paper)   # 指针停留在d最后
        if (boolD == True and boolA == False):  # 若B未结束，D结束，则拒绝该字符串
            return False
        if (boolA == True and boolD == True):  # ii  is the finl position of A
            return True
        else:  # ii未读的A的位置
            i = backA('a',i,paper)
            paper,i = reset(i,paper)  #指针在d
            i = backA('a',i,paper)    #指针退回到a
    i = back(i,paper)
    while (paper[i]!='*'):
        if(paper[i]=='@' or paper[i]=='#' or paper[i]=='$' or paper[i]=='%'):
            i += 1
        else:
            break
    if (paper[i] == '*'):
        return True
    else:
        return False


def AcceptOrReject():
    paper ,bool = inputString()  # 把字符串写入纸带
    if(bool == False):
        return False
    if (stringTorF(paper) == True): #判断字符串是否由abcd构成,不是则直接拒绝
        return readPaper(paper) #判断是否符合规则
    else:
        return False

if __name__ == '__main__':
   result = AcceptOrReject()
   if(result==True):
       print "accept!"
   else:print "reject!"














