from datetime import datetime
def compare_a():
    x=int(input("enter a number:"))
    print("the number you enter is",x)
def compare_b():
    pass
start=datetime.now()
compare_a()
delta=datetime.now()-start
print("compare_a's cost",delta.microseconds)
start=datetime.now()
start=datetime.now()
compare_b()
delta=datetime.now()-start
print("compare_b's cost",delta.microseconds)

