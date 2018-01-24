#
#Date: 09/07/2016
##  Class: CS5310
# Assignment: Project
# Author(s): shashank kasinadhuni
#
import random;
import timeit;
import pickle;
def knapsack(val, wt, W, n):
    p = 0;

    # vlwt is the list which will store the val/wt ratio of the items.
    vlwt = [0 for x in range(n)]

    # Assigning the values in vlwt list.
    for i in range(n):
        if wt[i] == 0:continue
        if val == 0: continue
        vlwt[i] = val[i] / wt[i]
    arrange(val, wt, vlwt, n)
    # Calculating the max value
    for i in range(n):
        if (W == 0):
            break

        # If item can put in the knapsack as whole
        elif (wt[i] <= W):
            p = p + val[i]
            W = W - wt[i]

        # When item need to be broken to put it in knapsack
        else:
            p = p + (val[i] * (W / wt[i]))
            W = 0
    return p


# arrange function will arrange the list val
# and wt with respect to non-decreasing order in vlwt
def arrange(val, wt, vlwt, n):
    for i in range(n):
        for j in range(i + 1, n):
            if (vlwt[i] < vlwt[j]):
                temp = vlwt[i]
                vlwt[i] = vlwt[j]
                vlwt[j] = temp
                temp = wt[i]
                wt[i] = wt[j]
                wt[j] = temp
                temp = val[i]
                val[i] = val[j]
                val[j] = temp


# Driver program to test the above function

#fto = open("fto.txt", 'w')
#fso = open("fso.txt", 'w')
twentylakh_onecrore=open("twentylakh_onecrore.txt", 'w')
twentylakh_onecrores=open("twentylakh_onecrores.txt", 'w')
#i=300
s=[]
st=[]
avg1=[]
#for i in range(1000,25000,1000):
   # for j in range(100000,200000,6250):
for i in range(300,2500,100):
    for j in range(2500,500000,10000):
        wt = random.sample(xrange(j), i)
        val = random.sample(xrange(j), i)
        W=sum(wt)
        n=len(val)
        start = timeit.default_timer()
        knapsack(val,wt,W,n)
        stop = timeit.default_timer()
        x=stop-start
        s.append(x)
        st.append(len(wt))
#avg = float(sum(s)) / len(s)
#avg1.insert(0,avg)
#print s
#print avg1
twentylakh_onecrore.writelines("\n".join(map(lambda x: str(x), s)))
twentylakh_onecrores.writelines("\n".join(map(lambda x: str(x), st)))
twentylakh_onecrore.close()
twentylakh_onecrore.close()



