import numpy as np
import matplotlib.pyplot as plt

N=100

def symulacja(N, p):
    x=np.arange(N)
    y=np.zeros(N)
    l=0
    for i in range(N):
        r=np.random.rand()
        if r<p:
            y[i]=l+1
            l+=1
        else:
            y[i]=l-1
            l=l-1
    return x,y
result=[]
for i in range(10000):
    x,y=symulacja(100, 0.5)
    result.append((y[-1]))

print(max(result), min(result), sum(result)/len(result))
result = np.array(result)
low_bound = np.percentile(result, 2.5)
high_bound = np.percentile(result, 97.5)
filtered_result = np.array(result[(result >= low_bound) & (result <= high_bound)])
fig, axs = plt.subplots(1, sharey=True, tight_layout=True)
axs.hist(filtered_result, bins=75)
plt.show()