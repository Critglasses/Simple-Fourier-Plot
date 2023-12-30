import numpy as np
import matplotlib.pyplot as plt


T = 0.5    #Changes "frequency"
tau = T/30
X = np.linspace(-1,1,1000) #defines the span of x
j = 15   #Determines how accurate the fourier approximation will be. Higher j means better approximation
def f(k):  #Defines f, which is the Fourier coefficient
    w_j = (2*np.pi*k) / T
    f = ((np.exp(1j*2*np.pi*tau*(w_j + 1/tau)) - 1) / (2*T*(-w_j - 1/tau))) - ((np.exp(1j*2*np.pi*tau*(w_j - 1/tau)) - 1) / (2*T*(1/tau - w_j)))
    return f

def sum(x, j):  #A recurrence which determines the value of the function based on chosen j and range x
    b= 0
    for i in range(-j, j + 1):
        w_j = (2 * np.pi * i) / T
        b = b + f(i)* np.exp(-x*1j*w_j)
    return b


def piece(t, tau, T):  #Defines the piecewise function
    p = np.piecewise(t,[((t%T>=0) & (t%T<=2* np.pi*tau)),((t%T>=2*np.pi*tau) & (t%T<=T) )], [lambda t:np.sin(t%T/tau), 0] )
    return p

plt.title(f'Fourier Expansion of p(t) at j = {j}')
plt.plot(X, sum(X, j), 'b', label='Fourier Expansion of p(t)') #Plots the fourier series approximation of the function
plt.plot(X, piece(X, tau, T),'r', label = 'p(t)')   #Plots the function p(t)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.legend()
plt.show()



