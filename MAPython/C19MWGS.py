import matplotlib.pyplot as plt
import numpy as np

a1 = np.loadtxt("MT750057USAU.txt")
a2 = np.loadtxt("MT750058USAU.txt")

mut = a2 - a1
fig, (ax0, ax1, ax2) = plt.subplots(3, 1)
c = ax0.pcolor(a1)
ax0.set_title('MT750057 (a)')
c = ax1.pcolor(a2)#, edgecolors='k', linewidths=4)
ax1.set_title('MT750058 (b)')
c = ax2.pcolor(mut)#, edgecolors='k', linewidths=4)
ax2.set_title('Mutation (c)')
fig.tight_layout()
#plt.show()
fig.savefig('COVID-19_Genome_Mutation_Whole_Sequences.pdf')

