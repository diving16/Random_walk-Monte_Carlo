import random

def give_the_number():
    number=random.randint(1,100)
    
    if number<=70:
        print(number,'the number is 1-70.You lose.')
        return False
    else:
        print(number,'the number is 50-100.You win.')
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
    
    while current_game_count<game_count:
        if give_the_number():
            funds+=wager
        else:
            funds-=wager
        current_game_count+=1
        if funds<0:
            funds='Penny less'
            break
    print('how rich:', funds)
    
a_fool(1000,100,30)
    