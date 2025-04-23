def fun():
    print("Function fun() called")

def disp():
    print("Function disp() called")

def msg():
    print("Function msg() called")

func_list = [fun, disp, msg]

for f in func_list:
    f()
