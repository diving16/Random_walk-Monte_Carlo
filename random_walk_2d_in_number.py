import random
import matplotlib.pyplot as plt

#改进代码
def random_walk_2(n):
    x,y=0,0
    
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(0,-1),(-1,0),(1,0)])
        x+=dx
        y+=dy
    
    return (x,y)


# =============================================================================
# for i in range(100):
#     one_walk=random_walk_2(20)
#     print(one_walk,'how far:',abs(one_walk[0])+
#           abs(one_walk[1]))
# 
# =============================================================================
 
#写一个计数器
toofar_counter=0
how_many_simulations=50
far_limit=50
x=[]
y=[]
    
for i in range(how_many_simulations):
     one_walk=random_walk_2(30)
     
     x.append(one_walk[0])
     y.append(one_walk[1])
     print(x,y,'onewalk')
#    print(one_walk)
     how_far=int(one_walk[0])**2+int(one_walk[1]**2)
     if how_far>=far_limit:
#         print(one_walk,how_far,'It is too far away from home.')
         toofar_counter+=1
     else:
         pass
#         print(one_walk,how_far,'Ok.')
     print(x,y)
     plt.plot(x,y,'x')
     plt.show()    


#得到模拟中的比例
print('% of too far:',
      toofar_counter/how_many_simulations)

# =============================================================================
# def random_walk(n):
#     x=0
#     y=0
#     for i in range(n):
#         step=random.choice(['N','S','W','E'])
#         if step == 'N':
#             y=y+1
#         elif step == 'S':
#             y=y-1
#         elif step == 'W':
#             x=x-1
#         else:
#             x=x+1
#     return(x,y)
# 
#    
# for i in range(100):
#     one_walk=random_walk(10)
#     
# #    print(one_walk)
#     how_far=int(one_walk[0])**2+int(one_walk[1]**2)
#     if how_far>=50:
#         print(one_walk,how_far,'It is too far away from home.')
#     else:
#         print(one_walk,how_far,'Ok.')
# =============================================================================
   
    
   