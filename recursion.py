count=0
def function1(count):

    if count == 4:
        return
    print(count)
    function1(count+1)
    print("i'm the function")


function1(0)