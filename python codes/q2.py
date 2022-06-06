def func(cardnum):
    i=len(cardnum)
    s=(i-4)*"*"
    ans=s+cardnum[i-4:i]
    print(ans)


a="1234567567557"
func(a)