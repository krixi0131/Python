https://163.22.17.112/problem/1101%20exam5?fbclid=IwAR1ROOuazNIfIU0wjKu8WN-WTNUQgn2GUUpZ36nW0L4atn8G3uh1NBqlnMQ
def main():
    n=int(input()) #矩陣邊長
    t=list(map(int,input().split()))
    row=t[0]
    col=t[1]    #row,col為起點，其必定為在有擺棋子的位置
    gg = []
    for i in range(n):
        gg.append(list(map(int,input().split()))) #輸入跳棋盤矩陣    
    k=jump(row,col,n,gg,0,0)#num=跳棋最多可以跳幾下
    print(k)
    
def jump(row,col,n,gg,num,maxnum): 
    flag=0
    if row-2>=0 and col-2>=0:#左上
        if gg[row-1][col-1]==1 and gg[row-2][col-2]==0:               
            flag=1
            gg[row][col]=0
            gg[row-1][col-1]=0                
            new_num=jump(row-2,col-2,n,gg,num+1,0)                
            gg[row][col]=1
            gg[row-1][col-1]=1
            if new_num>maxnum:
                maxnum=new_num
    if row-2>=0:#上
        if gg[row-1][col]==1 and gg[row-2][col]==0:                
            flag=1
            gg[row][col]=0
            gg[row-1][col]=0                
            new_num=jump(row-2,col,n,gg,num+1,0)                 
            gg[row][col]=1
            gg[row-1][col]=1
            if new_num>maxnum:
                maxnum=new_num
    if row-2>=0 and col+2<n:#右上
        if gg[row-1][col+1]==1 and gg[row-2][col+2]==0:
            flag=1
            gg[row][col]=0
            gg[row-1][col+1]=0                
            new_num=jump(row-2,col+2,n,gg,num+1,0)
            gg[row][col]=1
            gg[row-1][col+1]=1
            if new_num>maxnum:
                maxnum=new_num
    if col-2>=0:#左
        if gg[row][col-1]==1 and gg[row][col-2]==0:               
            flag=1
            gg[row][col]=0
            gg[row][col-1]=0
            new_num=jump(row,col-2,n,gg,num+1,0)
            gg[row][col]=1
            gg[row][col-1]=1
            if new_num>maxnum:
                maxnum=new_num                
    if col+2<n:#右
        if gg[row][col+1]==1 and gg[row][col+2]==0:                
            flag=1
            gg[row][col]=0
            gg[row][col+1]=0
            new_num=jump(row,col+2,n,gg,num+1,0)
            gg[row][col]=1
            gg[row][col+1]=1
            if new_num>maxnum:
                maxnum=new_num                
    if row+2<n and col-2>=0:#左下
        if gg[row+1][col-1]==1 and gg[row+2][col-2]==0:                
            flag=1
            gg[row][col]=0
            gg[row+1][col-1]=0
            new_num=jump(row+2,col-2,n,gg,num+1,0)
            gg[row][col]=1
            gg[row+1][col-1]=1
            if new_num>maxnum:
                maxnum=new_num                
    if row+2<n:#下
        if gg[row+1][col]==1 and gg[row+2][col]==0:                                
            flag=1
            gg[row][col]=0
            gg[row+1][col]=0
            new_num=jump(row+2,col,n,gg,num+1,0)
            gg[row][col]=1
            gg[row+1][col]=1
            if new_num>maxnum:
                maxnum=new_num                
    if row+2<n and col+2<n: #右下
        if gg[row+1][col+1]==1 and gg[row+2][col+2]==0:              
            flag=1
            gg[row][col]=0
            gg[row+1][col+1]=0
            new_num=jump(row+2,col+2,n,gg,num+1,0)
            '''g[row][col]=1
            gg[row+1][col+1]=1'''
            if new_num>maxnum:
                maxnum=new_num    
    if flag==0:
        return num
    return maxnum
main()    
    
