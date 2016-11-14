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
lam = 1

pb = FunctTyp1(1,5,10)

tStop = 30.
tInc = 0.05
t = np.arange(0, tStop, tInc)



#########################
# visualization


fig = plt.figure()
plt.suptitle('Animation 4 - $q_k$ from 0 to 1')
ax1=fig.add_subplot(2,1,1)
plt.ylabel('Total reflux [ml/s]')
plt.grid(True)
ax2=fig.add_subplot(2,1,2)
plt.ylabel('Pressure [Pa]')
plt.xlabel('Time [s]')

x = np.arange(-9, 10)
y = np.arange(-9, 10).reshape(-1, 1)
base = np.hypot(x, y)
ims = []
for i in np.arange(200):
	qk = 0.005 + 0.005*i
	print(qk)
	Q, T1, T2 = Model1(b, ai, a0, l, dh, lh, kw, qk, my, lam, pb, t)
	im0, = ax1.plot(t, Q, 'k')
	im1, = ax2.plot(t, T1, 'b')
	im2, = ax2.plot(t, T2, 'r')	
    
	ims.append([im0, im1, im2])

im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000, blit=True)
im_ani.save('animation/Animation4.gif', writer='imagemagick', fps=30)

plt.show()
