from stent import *
import numpy as np

#########################
# parameters
b = 4
ai = 1
a0 = 1.67

l = 240
dh = 60
lh = 120

kw = 0.8
qk = 0.05

my = 1
lam = 14

pb = FunctTyp1(1,5,10)
#pb = FunctTyp3(1,15,20,25)

tStop = 30.
tInc = 0.05
t = np.arange(0, tStop, tInc)


#########################
# calculation
Q, pk, pb = Model1(b, ai, a0, l, dh, lh, kw, qk, my, lam, pb, t)


#########################
# visualization

plt.figure(1)
plt.suptitle('Example 1')

plt.subplot(211)
plt.ylabel('Total reflux [ml/s]')
plt.plot(t,Q, 'k')
#plt.plot([0, tStop], [qk, qk], 'k--')
plt.grid(True)

plt.subplot(212)
plt.plot(t,pk, 'b')
plt.plot(t,pb, 'r')
plt.ylabel('Pressure [Pa]')
plt.xlabel('Time [s]')

plt.show()
