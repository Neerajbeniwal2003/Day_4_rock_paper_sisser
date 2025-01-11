print("welcome to rock paper sisser:)")
import random
sisser='''

    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/ 
  
  '''
paper=''' 
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----' '''
rock='''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''
win='''
8b        d8 ,ad8888ba,   88        88    I8,        8        ,8I 88 888b      88  
 Y8,    ,8P d8"'    `"8b  88        88    `8b       d8b       d8' 88 8888b     88  
  Y8,  ,8P d8'        `8b 88        88     "8,     ,8"8,     ,8"  88 88 `8b    88  
   "8aa8"  88          88 88        88      Y8     8P Y8     8P   88 88  `8b   88  
    `88'   88          88 88        88      `8b   d8' `8b   d8'   88 88   `8b  88  
     88    Y8,        ,8P 88        88       `8a a8'   `8a a8'    88 88    `8b 88  
     88     Y8a.    .a8P  Y8a.    .a8P        `8a8'     `8a8'     88 88     `8888  
     88      `"Y8888Y"'    `"Y8888Y"'          `8'       `8'      88 88      `888  
'''
lose='''
8b        d8 ,ad8888ba,   88        88    88          ,ad8888ba,    ad88888ba  88888888888  
 Y8,    ,8P d8"'    `"8b  88        88    88         d8"'    `"8b  d8"     "8b 88           
  Y8,  ,8P d8'        `8b 88        88    88        d8'        `8b Y8,         88           
   "8aa8"  88          88 88        88    88        88          88 `Y8aaaaa,   88aaaaa      
    `88'   88          88 88        88    88        88          88   `"""""8b, 88"""""      
     88    Y8,        ,8P 88        88    88        Y8,        ,8P         `8b 88           
     88     Y8a.    .a8P  Y8a.    .a8P    88         Y8a.    .a8P  Y8a     a8P 88           
     88      `"Y8888Y"'    `"Y8888Y"'     88888888888 `"Y8888Y"'    "Y88888P"  88888888888 
'''
user_chose=int(input("choose 0 for rock, 1 for paper or 2 for sisser:"))#0(rock)<1(paper)<2(sisser)
com_chose=random.randint(0,2)
choices=[rock,paper,sisser]
if user_chose>=3:
    print("i said 0 ,1 or 2 :)")
elif user_chose==0 and com_chose==2:
    print(win)
elif user_chose==2 and com_chose==0:
    print(lose)
elif user_chose<com_chose:
    print(lose)
elif user_chose>com_chose:
    print(win)
else:
    print("its a draw")
print(f"coputer chose:{choices[com_chose]}")
print(f"you chose:{choices[user_chose]}")








