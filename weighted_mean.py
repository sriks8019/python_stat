#weighted mean
import sys

line1=sys.stdin.readline()
line2=sys.stdin.readline()
line3=sys.stdin.readline()
n=int(line1)
X=list(map(int,line2.split()))
W=list(map(int,line3.split()))
wx_sum=0.0
w_sum=0.0
for i in range(n):
    wx_sum += W[i] * X[i]
    w_sum += W[i]
w_mean= float(wx_sum/w_sum)

print(round(w_mean,1))
