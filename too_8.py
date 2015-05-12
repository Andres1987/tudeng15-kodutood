
# coding: utf-8

# In[1]:

#!/usr/bin/env python3

# funktsioon arvutab inimese vanuse p2evades

__author__ = "Andres Maser"

def main():
    print("Millal on su sünnipäev(dd/mm/yyyy)?")
    text = input()
    import datetime
    aasta = int(text[6:10])
    kuu = int(text[3:5])
    p2ev = int(text[0:2])
    t2na = datetime.datetime.now()  
    synnip2ev = datetime.datetime(aasta,kuu,p2ev)
    p2evi = t2na - synnip2ev
    print(p2evi.days)

if __name__ == "__main__":

   main()


# In[ ]:



