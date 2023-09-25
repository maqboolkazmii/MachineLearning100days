def greeting(name):
  print("Hello, " + name)


def sum_product(x,y):
    p=x*y
    s=x+y
    if (p>= 1000):
        return p
    else:
        return s


def sum_prev_curent_no(x):
    
    prev_no=0
    for i in range(x):
        #print(i)
        current_no=i
        summ= prev_no + current_no
        print("Current Number", current_no, "Previous Number ", prev_no, " Sum: ", summ)

        prev_no=i