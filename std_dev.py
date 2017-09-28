import sys
import math

num_elems=int(sys.stdin.readline())
elems=list(map(int,sys.stdin.readline().split()))

mean=float(sum(elems)/num_elems)

spread_elems=list(map(lambda x: (x-mean)**2, elems))

std_dev = float(sum(spread_elems)/num_elems)**(0.5)
print(round(std_dev,1))
