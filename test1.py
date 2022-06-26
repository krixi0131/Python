#n=想拍照貓數量
#m=過動貓數量
def main():
    n,m=map(int,input().split())
    hit=list(input().split()) #過動貓名字
    cats=['鯊魚','hero','mia','黑貓','miu','mogan','mori','melo','小貓']
    gbye(n,hit,cats,[])
    
def gbye(n,hit,cats,photo):
    if n == 0 :#算完就輸出
        print(*photo) #photo=最後輸出的貓咪排列照片
        return
    for i in range(len(cats)) :
        if len(photo) == 0 or (photo[-1] not in hit or cats[i] not in hit): 
        # 照片裡沒貓 or 照片裡最後一貓不是過動貓 or 全部貓裡第i隻貓不是過動貓
            gbye(n-1,hit,cats[:i]+cats[i+1:],photo+[cats[i]])
main()

