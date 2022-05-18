def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
        print("check")
        d=x+y
   # except ZeroDivisionError:
    #    print("division by zero")
   # except NameError:
    #    print("Name Error")
    except Exception as e:
        print("Exception : ",e)
divide(3, 1)