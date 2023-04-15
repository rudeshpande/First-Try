from pylab import *; from numpy import *; random.seed(3)

T = 500
alpha = 0.1
sigma = 0.3
theta = pi/4.0
aspect_ratio = 3.0

ap = sigma*random.randn(T,1)
bp = sigma*random.randn(T,1)/aspect_ratio

a = ap*cos(theta)-bp*sin(theta)
b = ap*sin(theta)+bp*cos(theta)

wA = zeros(T)
wB = zeros(T)

wA[0] = random.randn()*sigma
wB[0] = random.randn()*sigma

for t in range(1,T):
    r = wA[t-1]*a[t]+wB[t-1]*b[t]

    wA[t] = wA[t-1]+alpha*r*(a[t]-r*wA[t-1])
    wB[t] = wB[t-1]+alpha*r*(b[t]-r*wB[t-1])

eVal,eVec = linalg.eig(cov(a.transpose(),b.transpose()))

F = figure()
f = F.add_subplot(111)
f.plot(a,b,"o")
f.plot(wA,wB,"-")
show()
