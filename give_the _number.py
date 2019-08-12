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

def a_smart_fool(funds,initial_wager,game_count):
    wager=initial_wager
    x=[]
    y=[]
    current_game_count=0
    previous_game='win'
    previous_game_wager=initial_wager
    
    while current_game_count<=game_count:
        if previous_game == 'win':
            if give_the_number():
                previous_game='win'
                funds+=wager
                print('earn {}'.format(wager))
                x.append(current_game_count)
                y.append(funds)
            else:
                previous_game='lose'
                funds-=wager
                print('lose {}'.format(wager))
                x.append(current_game_count)
                y.append(funds)

                if funds<0:
                    print('bye,you have played {} games'.format(current_game_count))
                    break              
        elif previous_game == 'lose':
            if give_the_number():
                wager=previous_game_wager*2
                previous_game='win'
                wager=initial_wager
                funds+=wager
                print('earn {}'.format(wager))               
                x.append(current_game_count)
                y.append(funds)
                         
            else:
                wager=previous_game_wager*2
                previous_game='lose'
                funds-=wager
                print('lose {}'.format(wager))               
                x.append(current_game_count)
                y.append(funds)                
                if funds<0:
                    print('bye,you have played {} games'.format(current_game_count))
                    break
       
        current_game_count+=1
    print(funds)
    plt.plot(x,y)

n=0
while n<100:
    a_smart_fool_1=a_smart_fool(10000,1000,100)
    n+=1
plt.xlabel('how many games take part in')
plt.xlabel('Funds')
plt.show()

# =============================================================================
# #定义一个赌徒
# def a_fool(funds,wager,game_count):
#     current_game_count=0
#     x=[]
#     y=[]
#     
#     while current_game_count<game_count:
#         if give_the_number():
#             funds+=wager
#             x.append(current_game_count)
#             y.append(funds)
#         else:
#             funds-=wager
#             x.append(current_game_count)
#             y.append(funds)
# 
#         current_game_count+=1
#         
#     if funds<0:
#         funds='Pennyless'
#     plt.plot(x,y)
#     plt.show()
# #    print('how rich:', funds)
# 
# #从下面的蒙特卡洛仿真来看，玩的次数越多，大家都会亏损。 
# n=0
# while n<=100:
#     a_fool(1000,50,100000)
#     n+=1
# plt.xlabel('how many games take part in')
# plt.xlabel('Funds')
# plt.show()
# =============================================================================
    