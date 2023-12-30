# Simple-Fourier-Plot
This code showcases a simple demonstration of how the Fourier series can approximate a piecewise function. 

The code is a simple application of the libraries numpy and matplotlib, which are scientific libraries used for mathimatical calculations and plotting. The plot for the Fourier series approximation of the piecewise function takes values from the **sum** function which is then plotted. The accuracy of the approximation is determined by a constant j, which increases the amount of "waves" which are summed together to create a composite which approximates the piecewise functions.

The piecewise function is calculated using the **piecewise** function from the library **numpy**.


![Picture](https://github.com/Critglasses/Simple-Fourier-Plot/blob/main/Figure_1.png?raw=true)
![Picture](https://github.com/Critglasses/Simple-Fourier-Plot/blob/main/Figure_2.png?raw=true)
![Picture](https://github.com/Critglasses/Simple-Fourier-Plot/blob/main/Figure_3.png?raw=true)


# The Math
The function is defined as

$p(t) = \sin(t/\tau )$ for  $0 \leq t \leq 2 \pi \tau$ and

$p(t) = 0$ for $2\pi \tau \leq t \le T$

which is periodically repeated outside the interval $[0,T)$ with period $T$ and $\tau = T/30$. 

Calculation for the Fourier expansion begins with the constant $a_j$ as

$a_j = \int _0 ^T sin \left ( \frac{t}{\tau} \right )e^{i\omega t} = \frac{e^{i2\pi \tau (\omega _j + \frac{1}{\tau})}- 1}{2T(-\omega _j - \frac{1}{\tau})} -  \frac{e^{i2\pi \tau (\omega _j - \frac{1}{\tau})}- 1}{2T(\frac{1}{\tau }- \omega _j )}$,

which is then plugged into the Fourier series to yield  

```math
p(t) =  \sum_{j=0}^T \left( \frac{e^{i2\pi \tau(\omega _j + \frac{1}{\tau})}- 1}{2T(-\omega _j - \frac{1}{\tau})} -  \frac{e^{i2\pi \tau (\omega _j - \frac{1}{\tau})}- 1}{2T(\frac{1}{\tau  }- \omega _j )}\right )e^{-\omega _j t}. 
```


