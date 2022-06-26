def ecup(d,k): 
    for i in range(10**(d-1),10**(d)):        
        p=str(i)
        judge = True
        for j in range(1,len(p)):          
            if abs(int(p[j])-int(p[j-1]))>k:
                judge = False
                break
        if judge:
            print(i)
#d=代表數字有幾位數
#k=代表限制距離
def main():
    d,k=map(int,input().split()) 
    ecup(d,k)
main()   
  
'''
def jdua(number,k):
    for j in range(1,len(number)):
        if abs(int(number[j])-int(number[j-1]))>k:
            return False 
    return True    
'''       

