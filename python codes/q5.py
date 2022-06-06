
arr=[2,1,6,4,2,6,7,2,1,7]
p=""
for i in range(len(arr)):
    n=arr[i]
    count=0
    for j in range(len(arr)):
        if n==arr[j] and not(str(arr[j]) in p):
            count+=1

    p+=str(n)
    if count==2:
        print(n)