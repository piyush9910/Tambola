import random

import time



l1=[12,3,27,63,55,39,78,85,35,5,57,60,21,72,83,26,80,19,44,69,22,93,64,36,67,89,43,2,46,87,95,6,16,56,9,11,10,17,1,61,42,31,33,14,30,90,52,81,7,18,48,75,40,23,20,4,92,51,79,76,62,50,86,66,41,45,24,94,82,37,65,53,70,58,29,47,13,28,38,59,74,91,73,49,34,54,32,25,15,8,84,77,88,71,68]

l2=[]



while len(l2)!=95 :

    a=random.randrange(0,95)

    if a not in l2:

        l2+=[a]

        time.sleep(1)

        print("calling a number",l1[a])

time.sleep(1)
print("calling a number 99")        
time.sleep(1)
print("calling a number 96")
time.sleep(1)
print("calling a number 98")
time.sleep(1)
print("calling a number 97")
