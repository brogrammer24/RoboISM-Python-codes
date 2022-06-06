
word="h20 15 wa73r"
sum=0
for i in range(len(word)):

    if word[i].isnumeric():


        sum=sum+int(word[i])
       


print(sum)