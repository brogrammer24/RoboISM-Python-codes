

def func(numbers,string):
    if string =="asc":
        numbers.sort()
        print(numbers)
    elif string=="desc":
        numbers.sort()
        i=len(numbers)
        while i>=0:
            print(numbers[i])
            i=i-1
    elif string=="none":
        print(numbers)
    else:
        print("Invalid input")



numbers=[2,1,54,21,43,23]
func(numbers,"asc")
