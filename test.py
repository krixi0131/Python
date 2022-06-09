numlist=list(map(int,input().split()))
flag=0 #團體數
a=[] #同學統計過與否
friend=[int(x) for x in numlist] #好友編號
a = [0 for i in range(len(friend))]
for j in range(len(friend)):
    if a[j]==0: #從沒算的開始算，算過的變為1
        ff=j #暫存數
        t=[]
        while a[ff]==0:#沒算過就繼續算       
            t.append(ff)
            a[ff]=1 #算過的變為1
            ff=friend[ff] #一直循環到成一團體       
        print(*t)
        flag+=1 #團體數+1
print('小團體數:',flag)
