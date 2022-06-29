def xx(numx,listx):
    if numx.count('?')==0: #x.count=計算X有幾個問號
        listx.append(numx) #數字放進list
    for i in range(len(numx)): #把numx每個字元跑一次    
        if numx[i]=='?':
            for j in range(10):
                tmp=numx
                tmp=tmp[:i]+str(j)+tmp[i+1:]  # replace tmp[i] with str(j)
                xx(tmp,listx)
            break

def yy(numy,listy): 
    if numy.count('?')==0: 
        listy.append(numy) 
    for i in range(len(numy)):     
        if numy[i]=='?':
            for j in range(10):
                tmp=numy
                tmp=tmp[:i]+str(j)+tmp[i+1:] 
                yy(tmp,listy)
            break
 
def zz(numz,listz):
    if numz.count('?')==0: 
        listz.append(numz) 
    for i in range(len(numz)):   
        if numz[i]=='?':
            for j in range(10):
                tmp=numz
                tmp=tmp[:i]+str(j)+tmp[i+1:]  
                zz(tmp,listz)
            break
            
def jia(listx,listy,listz):  #x+y=z的話就印出
    for i in range(len(listx)):
        for ii in range(len(listy)):
            ans=str(int(listx[i])+int(listy[ii]))
            if ans in listz:
                print(int(listx[i]),int(listy[ii]),int(listx[i])+int(listy[ii]))
              
def main():
    numx,numy,numz=map(str,input().split()) 
    listx=[]
    listy=[]
    listz=[]
    xx(numx,listx)
    yy(numy,listy)
    zz(numz,listz)
    jia(listx,listy,listz)

main()