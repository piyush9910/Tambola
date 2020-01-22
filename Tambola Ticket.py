print("_____________________________________________________TAMBOLA____________________________________________________________                         ")

import random
import numpy as np
import time
ticket=np.full(30,0)
x=1
ticket1=ticket.reshape(3,10)

for c in range(0,10):

    for r in range(0,3):

        ticket1[r][c]=random.randrange(x,x+3)

        if ticket1[r][c]==100:

            ticket1[r][c]=99

        if r==1:

            x=x+4

        else:

            x+=3

print(ticket1)



for i in range(100):

    n=int(input("enter your called number:"))

    for c in range(0,10):

        for r in range(0,3):

                if ticket1[r][c]==n:

                    ticket1[r][c]=0

                    print(ticket1) 
    if ticket1[r][c]==0:
        time.sleep(3)
        print("yeahh!!!! BINGO ")
        time.sleep(10)
        break
                    
                

    if ticket1[r][c]!=n:

        print("enter next number")
        print(ticket1)
        print("*********************************")             
