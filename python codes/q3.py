def func(a,opt,b):
    if opt=="+":
        return a+b
    elif opt=="-":
        return a-b
    elif opt=="*":
        return a*b
    else:
        return a/b




print(func(2,'/',7))