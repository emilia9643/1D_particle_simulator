import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

p_values = [0.4, 0.5, 0.6] 
N_values = [200, 500, 1000]
M = 1000
def symulacja(N, p):
    y = np.zeros(N + 1)
    y[0] = 0
    l = 0
    for i in range(1, N + 1):
        r = np.random.rand()
        if r < p:
            l += 1
        else:
            l -= 1
        y[i] = l
    return np.arange(N + 1), y

# przykladowe trajektorie dla p=0.35 i N=100
for i in N_values:
    plt.figure(figsize=(10, 6))
    for j in range(10):
        x_traj, y_traj = symulacja(i, 0.35)
        plt.plot(x_traj, y_traj, label=f'Symulacja {j+1}')
    plt.title(f'Przykładowe trajektorie (p=0.35, N={i})')
    plt.xlabel('Krok')
    plt.ylabel('Pozycja')
    plt.legend()
    plt.show()

#histogramy pozycji koncowych dla roznych p przy N=100
plt.figure(figsize=(12, 5))
N_fix = 100
for idx, p in enumerate(p_values):
    final_positions = []
    for m in range(M):
        m, y = symulacja(N_fix, p)
        final_positions.append(y[-1])
    
    plt.subplot(1, 3, idx+1)
    plt.hist(final_positions, bins=30, density=True, alpha=0.7)
    plt.title(f'Histogram p={p}')
    plt.xlabel('Pozycja końcowa')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))
N_fix = 100
final_positions = []
for idx, N in enumerate(N_values):
    final_positions = []
    for m in range(M):
        m, y = symulacja(N, 0.35)
        final_positions.append(y[-1])
    plt.subplot(1, 3, idx+1)
    plt.hist(final_positions, bins=30, density=True, alpha=0.7)
    plt.title(f'Histogram N={N}')
    plt.xlabel('Pozycja końcowa')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

for p in p_values:
    means = []
    cis = []
    
    for N in N_values:
        final_positions = []
        for _ in range(M):
            _, y = symulacja(N, p)
            final_positions.append(y[-1])
             
        mean_pos = np.mean(final_positions)
        std_dev = np.std(final_positions, ddof=1)
        sem = std_dev / np.sqrt(M)
        ci_width = stats.t.ppf(0.975, df=M-1) * sem
        
        means.append(mean_pos)
        cis.append(ci_width)

    plt.errorbar(N_values, means, yerr=cis, fmt='-o', label=f'p={p}')

plt.title('srednia pozycja końcowa vs N (z 95% CI)')
plt.xlabel('liczba krokow N')
plt.ylabel('srednia pozycja')
plt.legend()
plt.grid(True)
plt.show()