# youtube="ARBAJ"

# print("MY Name is "+youtube)

# print("My name is {}".format(youtube))

# print(f"my name is {youtube}")
# adj1=input("Adj: ")
# adj2=input("Adj: ")
# adj3=input("Adj: ")

# madlib=f"compute programmis is so {adj1}! IT makes me so excited all the time because \
# I LOVE {adj2} and also {adj3} like a famous person{adj3}"

# print(madlib)

import random
from sample_madlibs import code,hp,hungergames,zombie
if __name__=="__main__":

    m=random.choice([code,hp,hungergames,zombie])
    m.madlib()
 