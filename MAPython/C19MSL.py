
import matplotlib.pyplot as plt
import numpy as np
g= 0
y= 0

with open('MT750057USAU.txt') as f1, open('MT750058USAU.txt') as f2, open('xyz.txt', 'w') as L1, open('zxy.txt', 'w') as L2:
    for lineno, (line1, line2) in enumerate(zip(f1, f2), 1):
        if line1 != line2:
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    #y = y + 1
                    #g= (g+i)*lineno
                    #print(i/2)#print i, a[i], b[i]
                    L1.write(line1)
                    L2.write(line2)
                    g=(i)+((lineno-1)*60)
                    print ('mismatch in line no:', lineno, ', location in line:', i, ', overall location', g)
                    #print(i/2)
                    #print(g)\
    L1.close()
    L2.close()


a1 = np.loadtxt("xyz.txt") #MT750057USAU.txt
#print(a1)
a2 = np.loadtxt("zxy.txt") #MT750058USAU.txt
#print("First", a1)
#print("Second", a2)
asd = a2 - a1
fig, (ax0, ax1, ax2) = plt.subplots(3, 1)
c = ax0.pcolor(a1)
ax0.set_title('MT750057 (a)')
c = ax1.pcolor(a2)#, edgecolors='k', linewidths=4)
ax1.set_title('MT750058 (b)')
c = ax2.pcolor(asd)#, edgecolors='k', linewidths=4)
ax2.set_title('Mutation (c)')
#print("Third", asd)
#plt.pcolormesh(asd)
#plt.title('matplotlib.pyplot.pcolormesh() function Example', fontweight="bold")
fig.tight_layout()
#plt.show()
fig.savefig('Updated_COVID-19_Genome_Mutation_SL.pdf')

