def main():
    money,target,species=map(int,input().split())
    prices=list(map(int,input().split()))
    if min(prices)*target>money:
        print('無法買滿')
    else:
        cash(money,target,species,prices)

def cash(money,target,species,prices):
    buy(money,target,species,prices,0,[])
    
def buy(money,target,species,prices,num,list):
    if num==species:
        if target==0:
            print(*list)
        return
    for i in range(min(target,money//prices[num]),-1,-1):
        buy(money-i*prices[num],target-i,species,prices,num+1,list+[i])
main()