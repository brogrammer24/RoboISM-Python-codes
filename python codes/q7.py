arr=[1,2,3,4,5,1,2,3,5,6,3,7,7]
p=""
freq=0
store=arr[0]
for i in range(len(arr)):
    n=arr[i]
    count=0
    for j in range(i,len(arr)):
        if n==arr[j] and not(str(n) in p):
            count+=1
    p = p + str(n)
    l=freq
    freq=max(freq,count)
    if l<freq:
        store=n


print(store)