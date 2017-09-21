import sys

line1= sys.stdin.readline() #num of elements
line2= sys.stdin.readline() #input data, numbers separated by spaces

num_elems= int(line1)
elems= list(map(int,line2.split()))
sum_elems = 0
for i in range(num_elems):
    sum_elems+=elems[i]
    
sorted_elems=elems
sorted_elems.sort()
median=0.0
if(num_elems%2 == 0):
    median= float((sorted_elems[int(num_elems/2) -1]+ sorted_elems[int(num_elems/2)])/2)
else:
    median= float(sorted_elems[((num_elems+1)/2) -1])
mode=0.0
counts={}
for j in range(0,num_elems):
    if(elems[j] not in counts):
        counts[elems[j]]=1
    else:
        counts[elems[j]]+=1
max_count= max(counts.values())
max_count_elems=[]
for key, value in counts.items():
    if value == max_count :
        max_count_elems.append(key)
mode=min(max_count_elems)
print(round(float(sum_elems/num_elems),1))
print(round(median,1))
print(round(mode,1))
