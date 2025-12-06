#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import matplotlib.pyplot as plt


# In[91]:


#SETTING UP INITAL FUNCTION
def function(x):
    return (-x**5)+(4*x**4)-(4*x**3)+(x**2*np.exp(x))-(2*x**2)-(4*x*np.exp(x))+(8*x)+(4*np.exp(x))-8

f=function(x)


# In[71]:


#FIXED POINT ITERATION

#checking f(x) and g(x) plot with y=x
x=np.linspace(-2,5,100)
y=x

def g(x):
    return (function(x)-8*x)/(-8)

fig,axs=plt.subplots(1,3,figsize=(10,4))
ax1,ax2,ax3=axs

ax1.axhline(0,linestyle="--",color="r")
ax1.plot(x,function(x))
ax1.set_title("f(x) plot")
ax1.grid()

ax2.axhline(0,linestyle="--", color="r")
ax2.plot(x,function(x))
ax2.set_title("f(x) plot zoomed in on -2<x<5")
ax2.set_ylim(-0.5,0.5)
ax2.grid()

ax3.plot(x,y,label="y=x")
ax3.plot(x,g(x),label="g(x)")
ax3.legend()
ax3.set_title("g(x) and y=x")
ax3.grid()


# In[ ]:


# There are 3 roots to the function as shown in the figures above.


# In[78]:


def fixedpoint(g,x_old,k_max=200,tol=1.e-8):
    for k in range(1,k_max):
        x_new=g(x_old)

        x_diff=x_new-x_old
        print("{0:2d} {1:1.16f} {2:1.16f}".format(k,x_new,x_diff))

        if abs(x_diff/x_new)<tol:
            break

        x_old=x_new
    else:
        x_new=None

    return x_new


# In[76]:


#first root
for x_old in (-1.2,-1.1):
    x_roots=fixedpoint(g,x_old)
    print(x_roots)


# In[77]:


#second root
for x_old in (1.99,2.2):
    x_roots=fixedpoint(g,x_old)
    print(x_roots)


# In[84]:


#third root (No roots found)
for x_old in (4.3,4.5):
    x_roots-fixedpoint(g,x_old)
    print(x_roots)


# In[93]:


#BISECTION METHOD
def bisection(f,x0,x1,k_max=200,tol=1.e-8):
    f0=function(x0)
    for k in range(1,k_max):
        x2=(x0+x1)/2
        f2=function(x2)

        if f0*f2<0:
            x1=x2
        else:
            x0,f0=x2,f2

        x2_new=(x0+x1)/2
        xdiff=abs(x2_new-x2)
        rowf="{0:2d} {1:1.16f} {2:1.16f} {3:1.16f}"
        print(rowf.format(k,x2_new,xdiff,abs(function(x2_new))))

        if abs(xdiff/x2_new)<tol:
            break
    else:
        x2_new=None

    return x2_new


# In[94]:


#first root
root=bisection(f,-2,0)
print(root); print("")


# In[101]:


#second root (No roots found)
root=bisection(f,1,3)
print(root); print("")


# In[100]:


#third root
root=bisection(f,4,5)
print(root); print("")


# In[118]:


#NEWTON'S METHOD
def newtons(f,x0,x1,k_max=200,tol=1.e-8):
    f0=function(x0)
    for k in range(1,k_max):
        f1=function(x1)
        f1prime=(-5*x1**4)+(16*x1**3)-(12*x1**2)+(x1**2*np.exp(x1))-(2*x1*np.exp(x1))-(4*x1)+8
        ratio=f1/f1prime
        x2=x1-ratio

        xdiff=abs(x2-x1)
        x0,x1=x1,x2
        f0=f1

        rowf="{0:2d} {1:1.16f} {2:1.16f} {3:1.16f}"
        print(rowf.format(k,x2,xdiff,abs(function(x2))))

        if abs(xdiff/x2)<tol:
            break

    else:
        x2=None

    return x2


# In[119]:


#first root
root=newtons(f,-1.5,-1)
print(root); print("")


# In[120]:


#second root
root=newtons(f,1.7,2.3)
print(root); print("")


# In[121]:


#third root
root=newtons(f,4,5)
print(root); print("")


# In[106]:


#SECANT METHOD
def secant(f,x0,x1,k_max=200,tol=1.e-8):
    f0=function(x0)
    for k in range(1,k_max):
        f1=function(x1)
        ratio=(x1-x0)/(f1-f0)
        x2=x1-f1*ratio

        xdiff=abs(x2-x1)
        x0,x1=x1,x2
        f0=f1

        rowf="{0:2d} {1:1.16f} {2:1.16f} {3:1.16f}"
        print(rowf.format(k,x2,xdiff,abs(function(x2))))

        if abs(xdiff/x2)<tol:
            break

    else:
        x2=None

    return x2


# In[107]:


#first root
root=secant(f,-1.5,1)
print(root); print("")


# In[111]:


#second root
root=secant(f,1.7,2.3)
print(root); print("")


# In[115]:


#third root
root=secant(f,4.1,4.5)
print(root); print("")

