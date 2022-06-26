def rr(n):
    return know(n,0,[True for i in range(n)],[True for i in range(2*n-1)],[True for i in range(2*n-1)],[[0 for i in range(n)]for i in range(n)])
#n=皇后數量
#a=負責編號
#b直線是否可放皇后
#c右上
#d右下
def know(n,a,b,c,d,picture):
    if n == a : #已經擺上n個皇后
        for i in picture :
            print(*i)
        print("---------------")
    for k in range(n): #k去試每一欄
        if b[k] and c[a+k] and d[a-k+n-1]: #直、右上斜、右下斜 
            picture[a][k]=1
            b[k],c[a+k],d[a-k+n-1]=False,False,False #直、右上斜、右下斜都不能放
            know(n,a+1,b,c,d,picture)
            b[k],c[a+k],d[a-k+n-1]=True,True,True #恢復初始資料
            picture[a][k]=0
def main():
    n=int(input())
    if n == 2 or n == 3:
        print('找不到解')
    rr(n)
    
main()