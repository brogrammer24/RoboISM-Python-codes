
upper=int(input("Enter upper bound:"))
lower=int(input("Enter lower bound:"))

p=0

for i in range(upper,lower+1):
    if i==1:
        continue

    p=1
    for x in range(2,i):
        if i%x==0:
            p=0
            break


    if p==1:
        print(i)



