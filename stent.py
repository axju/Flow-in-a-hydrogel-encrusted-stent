import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy.linalg import inv
from scipy.integrate import odeint
from math import log, pi, sqrt, exp


class FunctTyp1:
	"""Model equation: Typ 1"""
	
	def __init__(self, pb, t1, t2):
		self.pb = pb
		self.t1 = t1
		self.t2 = t2

	def f(self, t):
		if 0<=t and t<=self.t1:
			return self.pb*t/self.t1
		elif self.t1<t and t<=self.t2:
			return self.pb - (self.pb/(self.t2-self.t1))*(t-self.t1)
		else:
			return 0
			

class FunctTyp2:
	"""Model equation: Typ 2"""
	
	def __init__(self, pb, t1, t2, t3):
		self.pb = pb
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3

	def f(self, t):
		if 0<=t and t<=self.t1:
			return self.pb*t/self.t1
		elif self.t1<t and t<=self.t2:
			return self.pb
		elif self.t2<t and t<=self.t3:
			return self.pb - (self.pb/(self.t3-self.t2))*(t-self.t2)
		else:
			return 0
		
		
class FunctTyp3:
	"""Model equation: Typ 3"""
	
	def __init__(self, pb, t1, t2, t3):
		self.pb = pb
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3

	def f(self, t):
		if 0<=t and t<=self.t1:
			return 0
		elif self.t1<t and t<=self.t2:
			return (self.pb/(self.t2-self.t1))*(t-self.t1)
		elif self.t2<t and t<=self.t3:
			return self.pb - (self.pb/(self.t3-self.t2))*(t-self.t2)
		else:
			return 0
			
		
				

 
def Model1(b, ai, a0, l, dh, lh, kw, qk, my, lam, pb, t):
	
	def f(y, t, params):
		pk = y                              
		A, M1, M2, pb = params            
		return M1*pk + M2*pb.f(t) + A
	
	d = a0**4-b**4+2*((b**2-a0**2)**2/log(b**2/a0**2))

	a = (8*lam*my*(d-ai**4))/(pi*d*ai**4)
	c = (64*lam*my**2)/(pi**2*d*ai**4)

	l1 = dh
	l2 = dh + lh
		
	# Matrix
	M = np.zeros((8,8))
	
	M[0,0] = ai**4/d
	M[0,1] = ai**4/d
	M[0,2] = c/a

	M[1,0] = 1
	M[1,1] = 1
	M[1,2] = c/a

	M[2,0] = (pi*sqrt(a)*ai**4*exp(sqrt(a)*(l1/l)))/8
	M[2,1] = -(pi*sqrt(a)*ai**4*exp(-sqrt(a)*(l1/l)))/8
	M[2,2] = 0
	M[2,3] = (pi*d*c)/(8*a)

	M[3,0] = exp(sqrt(a)*(l1/l))
	M[3,1] = exp(-sqrt(a)*(l1/l))
	M[3,2] = c/a
	M[3,3] = (c/a + 8/(pi*ai**4))*(l1/l)
	M[3,4] = -1

	M[4,3] = (pi*c*d)/(8*a)
	M[4,4] = 0
	M[4,5] = (pi*sqrt(a)*ai**4*exp(sqrt(a)*(l2/l)))/8
	M[4,6] = -(pi*sqrt(a)*ai**4*exp(-sqrt(a)*(l2/l)))/8

	M[5,3] = (b/a + 8/(pi*ai**4))*(l2/l)
	M[5,4] = -1
	M[5,5] = exp(sqrt(a)*(l2/l))
	M[5,6] = exp(-sqrt(a)*(l2/l))
	M[5,7] = b/a

	M[6,3] = c/a
	M[6,4] = 0
	M[6,5] = (ai**4*exp(sqrt(a)))/d
	M[6,6] = (ai**4*exp(-sqrt(a)))/d
	M[6,7] = b/a

	M[7,3] = c/a
	M[7,4] = 0
	M[7,5] = exp(sqrt(a))
	M[7,6] = exp(-sqrt(a))
	M[7,7] = b/a
	
	M0 = inv(M)
	
	A = kw*qk
	M1 = -kw*(M0[3,0]+M0[3,1])
	M2 = -kw*(M0[3,6]+M0[3,7])	

	pk = odeint(f, [0], t, args=([A, M1, M2, pb],))
	
	Q = []
	Pb = []
	for t0 in t:
		i=int(t0/t[len(t)-1]*(len(t)-1))
		Q.append((M0[3,6]+M0[3,7])*pb.f(t0)+(M0[3,0]+M0[3,1])*pk[i])
		Pb.append(pb.f(t0))

	
	return Q, pk, Pb
	
