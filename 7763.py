from unittest import skip


firstNum = ['p','q','r','s']
secondNum = ['p','q','r','s']
thirdNum = ['m','n','o']
forthNum = ['d','e','f']

for a in firstNum:
    for b in secondNum:
        for c in thirdNum:
            for d in forthNum:
                theName = a+" "+b+" "+c+" "+d
                print(str.upper(theName))