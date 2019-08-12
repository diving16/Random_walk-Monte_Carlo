import random
import matplotlib.pyplot as plt

def give_the_number():
    number=random.randint(1,100)
    
    if number<=51:
#        print(number,'the number is 1-51.You lose.')
        return False
    else:
#        print(number,'the number is 50-100.You win.')
        return True
    

# =============================================================================
# x=0
# for x in range(100):
#     result=give_the_number()
#     print(result)
# =============================================================================

#定义一个赌徒
def a_fool(funds,wager,game_count):
    current_game_count=0
    x=[]
    y=[]
    
    while current_game_count<game_count:
        if give_the_number():
            funds+=wager
            x.append(current_game_count)
            y.append(funds)
        else:
            funds-=wager
            x.append(current_game_count)
            y.append(funds)

        current_game_count+=1
        
    if funds<0:
        funds='Penny less'
    plt.plot(x,y)
    plt.show()
#    print('how rich:', funds)

#从下面的蒙特卡洛仿真来看，玩的次数越多，大家都会亏损。 
n=0
while n<=100:
    a_fool(1000,50,100000)
    n+=1
plt.xlabel('how many games take part in')
plt.xlabel('Funds')
plt.show()
    