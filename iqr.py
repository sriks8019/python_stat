import sys
def find_median(sortedarr):
    dat=sortedarr
    n=len(dat)
    median=0
    if(n%2==0):
        median= float((dat[int(n/2) - 1] + dat[int(n/2)])/2)
    else:
        median=dat[int(n/2)]
    return float(median)
num_elems= int(sys.stdin.readline())
elems=list(map( int, sys.stdin.readline().split()))
elem_reps=list(map( int, sys.stdin.readline().split()))

elem_list=[]

for i in range(num_elems):
    elem_list += [elems[i] for k in range(elem_reps[i])]

elem_list.sort()
elems=elem_list

q_two= find_median(elems)
lower_half=[]
upper_half=[]
numf_elems=len(elems)
if(numf_elems%2==0):
    lower_half= elems[0:int(numf_elems/2)]
    upper_half=elems[int(numf_elems/2):]
else:
    lower_half= elems[0:int(numf_elems/2)]
    upper_half=elems[int(numf_elems/2) +1:]
q_one= find_median(lower_half)   
q_three= find_median(upper_half)

print(q_three - q_one)
