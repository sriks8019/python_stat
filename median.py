#find quartiles

import sys

def find_median(sortedarr):
    dat=sortedarr
    n=len(dat)
    median=0
    if(n%2==0):
        median= (dat[int(n/2) - 1] + dat[int(n/2)])/2
    else:
        median=dat[int(n/2)]
    return median
line1=sys.stdin.readline()
line2=sys.stdin.readline()

n=int(line1)
elems=list(map(int,line2.split()))
elems.sort()
q_two= find_median(elems)
lower_half=[]
upper_half=[]
if(n%2==0):
    lower_half= elems[0:int(n/2)]
    upper_half=elems[int(n/2):]
else:
    lower_half= elems[0:int(n/2)]
    upper_half=elems[int(n/2) +1:]
q_one= find_median(lower_half)   
q_three= find_median(upper_half)
if(not isinstance(q_one,int) and int(q_one)-q_one == 0.0):
    q_one=int(q_one)
if(not isinstance(q_two,int) and int(q_two)-q_two == 0.0):
    q_two=int(q_two)
if(not isinstance(q_three,int) and int(q_three)-q_three == 0.0):
    q_three=int(q_three)
print(q_one)
print(q_two)
print(q_three)
