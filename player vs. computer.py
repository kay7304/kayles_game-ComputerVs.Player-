print (' welcome to kayles game! ')
print ('if you like to read the description of this game please press 1, if not press 0')
a=int(input())
if a==1:
    print ('This game begins with an arbitrary number of tokens in a single row, Two players alternate turns During a turn a player may remove either one or two adjacent tokens The player who removes the last token wins')
print ('if you ready to start the game press 1')
print ('if you want to closs the game press 2')
b=int(input())
if b==1:
    import random
    L1 = []
    L2 = []
    p1 = []
    p2 = []
    counter=0
    x = '-'
    size=random.randint(10,20)
    for s in range (size+1):
        L1.append(s)
        L2.append(x)
    print (L1)
    while counter<len(L1):
        print( 'the first player: do you want to remove 1 or 2 tokens?')
        c=int(input())
        if c==1:
            print( 'enter your number')
            d=int(input())
            if d in L1:
                L1[L1.index(d)]=x
                p1.append(d)
                counter=counter+1
                print (L1)
            else:
                print('this number is not in the list, please choose another number')
                d=int(input())
                if d in L1:
                    L1[L1.index(d)]=x
                    p1.append(d)
                    counter=counter+1
                    print (L1)
        if c==2:
            print('enter your first number')
            d=int(input())
            if d in L1:
                print('enter your second number')
                e=int(input())
                if (e==d+1) or (e==d-1):
                    if e in L1:
                        L1[L1.index(e)]=x
                        L1[L1.index(d)]=x
                        p1.append(d)
                        p1.append(e)
                        counter=counter+2
                        print (L1)
                    else:
                        print('this number is not in the list, please choose another number')
                        e=int(input())
                        if (e==d+1) or (e==d-1):
                            if e in L1:
                                L1[L1.index(e)]=x
                                L1[L1.index(d)]=x
                                p1.append(d)
                                p1.append(e)
                                counter=counter+2
                                print (L1)
                else:
                    print('you should select two adjacent numbers')
                    print('enter your first number')
                    n=int(input())
                    if n in L1:
                        print('enter your second number')
                        m=int(input())
                        if m==n+1 or m==n-1:
                            if m in L1:
                                L1[L1.index(m)]=x
                                L1[L1.index(n)]=x
                                p1.append(m)
                                p1.append(n)
                                counter=counter+2
                                print(L1)
                            else:
                                print('this number is not in the list please choose another number')
                                m=int(input())
                                if (m==n+1) or (m==n-1):
                                    if m in L1:
                                        L1[L1.index(n)]=x
                                        L1[L1.index(m)]=x
                                        p1.append(n)
                                        p1.append(m)
                                        counter=counter+2
                                        print (L1)
            else:
                print('this number is not in the list, please choose another number')
                print('enter your first number')
                d=int(input())
                if d in L1:
                    print('enter your second number')
                    e=int(input())
                    if (e==d+1) or (e==d-1):
                        if e in L1:
                            L1[L1.index(e)]=x
                            L1[L1.index(d)]=x
                            p1.append(d)
                            p1.append(e)
                            counter=counter+2
                            print (L1)
                        else:
                            print('this number is not in the list, please choose another number')
                            e=int(input())
                            if (e==d+1) or (e==d-1):
                                if e in L1:
                                    L1[L1.index(e)]=x
                                    L1[L1.index(d)]=x
                                    p1.append(d)
                                    p1.append(e)
                                    counter=counter+2
                                    print (L1)
                    else:
                        print('you should select two adjacent numbers')
                        print('enter your first number')
                        n=int(input())
                        if n in L1:
                            print('enter your second number')
                            m=int(input())
                            if m==n+1 or m==n-1:
                                if m in L1:
                                    L1[L1.index(m)]=x
                                    L1[L1.index(n)]=x
                                    p1.append(m)
                                    p1.append(n)
                                    counter=counter+2
                                    print(L1)
                                else:
                                    print('this number is not in the list please choose another number')
                                    m=int(input())
                                    if (m==n+1) or (m==n-1):
                                        if m in L1:
                                            L1[L1.index(n)]=x
                                            L1[L1.index(m)]=x
                                            p1.append(n)
                                            p1.append(m)
                                            counter=counter+2
                                            print (L1)

        if counter==len(L1):
            print('player 1 wins')
            print('congratulations!')
            break
        print('player2: do you want to delete 1 or 2 numbers?')
        select=random.randint(1,2)
        print (select)
        if select==1:
            print('choose your number')
            choose=random.randint(0,len(L1))
            if choose in L1:
                print(choose)
                L1[L1.index(choose)]=x
                p2.append(choose)
                counter=counter+1
                print (L1)
            else:
                choose=random.randint(0,len(L1))
                if choose in L1:
                    print(choose)
                    L1[L1.index(choose)]=x
                    p2.append(choose)
                    counter=counter+1
                    print (L1)
                else:
                    choose=random.randint(0,len(L1))
                    if choose in L1:
                        print(choose)
                        L1[L1.index(choose)]=x
                        p2.append(choose)
                        counter=counter+1
                        print (L1)
                    else:
                        choose=random.randint(0,len(L1))
                        if choose in L1:
                            print(choose)
                            L1[L1.index(choose)]=x
                            p2.append(choose)
                            counter=counter+1
                            print (L1)
                        else:
                            choose=random.randint(0,len(L1))
                            if choose in L1:
                                print(choose)
                                L1[L1.index(choose)]=x
                                p2.append(choose)
                                counter=counter+1
                                print (L1)
                            else:
                                choose=random.randint(0,len(L1))
                                if choose in L1:
                                    print(choose)
                                    L1[L1.index(choose)]=x
                                    p2.append(choose)
                                    counter=counter+1
                                    print (L1)
                                else:
                                    choose=random.randint(0,len(L1))
                                    if choose in L1:
                                        print(choose)
                                        L1[L1.index(choose)]=x
                                        p2.append(choose)
                                        counter=counter+1
                                        print (L1)
                                    
        if select==2:
            num1=random.randint(0,len(L1))
            if num1 in L1:
                num2=num1+1
                if num2 in L1:
                    print('enter your first number')
                    print(num1)
                    print('enter your second number')
                    print(num2)
                    L1[L1.index(num1)]=x
                    L1[L1.index(num2)]=x
                    p2.append(num1)
                    p2.append(num2)
                    counter=counter+2
                    print(L1)
                else:
                    num2=num1-1
                    if num2 in L1:
                        print('enter your first number')
                        print(num1)
                        print('enter your second number')
                        print(num2)
                        L1[L1.index(num1)]=x
                        L1[L1.index(num2)]=x
                        p2.append(num1)
                        p2.append(num2)
                        counter=counter+2
                        print(L1)
                    else:
                        num1=random.randint(0,len(L1))
                        if num1 in L1:
                            num2=num1+1
                            if num2 in L1:
                                print('enter your first number')
                                print(num1)
                                print('enter your second number')
                                print(num2)
                                L1[L1.index(num1)]=x
                                L1[L1.index(num2)]=x
                                p2.append(num1)
                                p2.append(num2)
                                counter=counter+2
                                print(L1)
                            else:
                                num2=num1-1
                                if num2 in L1:
                                    print('enter your first number')
                                    print(num1)
                                    print('enter your second number')
                                    print(num2)
                                    L1[L1.index(num1)]=x
                                    L1[L1.index(num2)]=x
                                    p2.append(num1)
                                    p2.append(num2)
                                    counter=counter+2
                                    print(L1)
                                else:
                                    num1=random.randint(0,len(L1))
                                    if num1 in L1:
                                        num2=num1+1
                                        if num2 in L1:
                                            print('enter your first number')
                                            print(num1)
                                            print('enter your second number')
                                            print(num2)
                                            L1[L1.index(num1)]=x
                                            L1[L1.index(num2)]=x
                                            p2.append(num1)
                                            p2.append(num2)
                                            counter=counter+2
                                            print(L1)
                                        else:
                                            num2=num1-1
                                            if num2 in L1:
                                                print('enter your first number')
                                                print(num1)
                                                print('enter your second number')
                                                print(num2)
                                                L1[L1.index(num1)]=x
                                                L1[L1.index(num2)]=x
                                                p2.append(num1)
                                                p2.append(num2)
                                                counter=counter+2
                                                print(L1)
                            
            else:
                num1=random.randint(0,len(L1))
                if num1 in L1:
                    num2=num1+1
                    if num2 in L1:
                        print('enter your first number')
                        print(num1)
                        print('enter your second number')
                        print(num2)
                        L1[L1.index(num1)]=x
                        L1[L1.index(num2)]=x
                        p2.append(num1)
                        p2.append(num2)
                        counter=counter+2
                        print(L1)
                    else:
                        num2=num1-1
                        if num2 in L1:
                            print('enter your first number')
                            print(num1)
                            print('enter your second number')
                            print(num2)
                            L1[L1.index(num1)]=x
                            L1[L1.index(num2)]=x
                            p2.append(num1)
                            p2.append(num2)
                            counter=counter+2
                            print(L1)
                        else:
                            num1=random.randint(0,len(L1))
                            if num1 in L1:
                                num2=num1+1
                                if num2 in L1:
                                    print('enter your first number')
                                    print(num1)
                                    print('enter your second number')
                                    print(num2)
                                    L1[L1.index(num1)]=x
                                    L1[L1.index(num2)]=x
                                    p2.append(num1)
                                    p2.append(num2)
                                    counter=counter+2
                                    print(L1)
                                else:
                                    num2=num1-1
                                    if num2 in L1:
                                        print('enter your first number')
                                        print(num1)
                                        print('enter your second number')
                                        print(num2)
                                        L1[L1.index(num1)]=x
                                        L1[L1.index(num2)]=x
                                        p2.append(num1)
                                        p2.append(num2)
                                        counter=counter+2
                                        print(L1)
                                    else:
                                        num1=random.randint(0,len(L1))
                                        if num1 in L1:
                                            num2=num1+1
                                            if num2 in L1:
                                                print('enter your first number')
                                                print(num1)
                                                print('enter your second number')
                                                print(num2)
                                                L1[L1.index(num1)]=x
                                                L1[L1.index(num2)]=x
                                                p2.append(num1)
                                                p2.append(num2)
                                                counter=counter+2
                                                print(L1)
                                            else:
                                                num2=num1-1
                                                if num2 in L1:
                                                    print('enter your first number')
                                                    print(num1)
                                                    print('enter your second number')
                                                    print(num2)
                                                    L1[L1.index(num1)]=x
                                                    L1[L1.index(num2)]=x
                                                    p2.append(num1)
                                                    p2.append(num2)
                                                    counter=counter+2
                                                    print(L1)
                                                else:
                                                    num1=random.randint(0,len(L1))
                                                    if num1 in L1:
                                                       num2=num1+1
                                                       if num2 in L1:
                                                           print('enter your first number')
                                                           print(num1)
                                                           print('enter your second number')
                                                           print(num2)
                                                           L1[L1.index(num1)]=x
                                                           L1[L1.index(num2)]=x
                                                           p2.append(num1)
                                                           p2.append(num2)
                                                           counter=counter+2
                                                           print(L1)
                                                       else:
                                                           num2=num1-1
                                                           if num2 in L1:
                                                                print('enter your first number')
                                                                print(num1)
                                                                print('enter your second number')
                                                                print(num2)
                                                                L1[L1.index(num1)]=x
                                                                L1[L1.index(num2)]=x
                                                                p2.append(num1)
                                                                p2.append(num2)
                                                                counter=counter+2
                                                                print(L1)     

        if counter==len(L1):
            print('player 2 wins')
            print('congratulations!')
            break
print ('goodbye!')

