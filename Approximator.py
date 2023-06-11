import numpy as np
import matplotlib.pyplot as plt

class function_approximator:
    def __init__(self,x):
        self.x = x
    
    @staticmethod
    def f_real(x):
        f_x=np.sin(12*(x+0.2))/(x+0.2)
        return f_x
    
    def y_real(self,x):
        e=np.random.normal(0,1,len(x))
        y=self.f_real(x)+e
        return y
    
    @staticmethod
    def positive_cubic(x,knot):
        y=0
        if x-knot>0:
            y=(x-knot)**3
        return y
    
    def d(self,X,x,k):
        knots=np.sort(x)
        dkx=(self.positive_cubic(X,knots[k])-self.positive_cubic(X,knots[len(x)-1]))/(knots[len(x)-1]-knots[k])
        return dkx

    def create_N(self,x):
        knots=np.sort(x)
        N=np.zeros([len(knots),len(knots)])
        N[:,0]=np.ones(len(knots))
        N[:,1]=x
        for i in range(len(knots)):
            for j in range(len(knots)-2):
                N[i,j+2]=self.d(x[i],knots,j)-self.d(x[i],knots,len(x)-2)
        return N

    @staticmethod
    def I_star(j,k,x):
        knots=np.sort(x)
        a=max(knots[j],knots[k])
        y=(1/3)-(1/2)*(knots[k]+knots[j])+knots[j]*knots[k]-(a**3)/3 + ((a**2)/2)*(knots[k]+knots[j])-a*knots[j]*knots[k]
        return y
    
    def I(self,j,k,x):
        knots=np.sort(x)
        K=len(knots)-1
        y=(36/((knots[K]-knots[j])*(knots[K]-knots[k])))*(self.I_star(j,k,knots)- self.I_star(j,K,knots)- self.I_star(K,k,knots)+ self.I_star(K,K,knots))
        return y
    
    def pointwise_Omega(self,j,k,x):
        knots=np.sort(x)
        K=len(knots)-1
        y=self.I(j-2,k-2,knots)-self.I(j-2,K-1,knots)-self.I(K-1,k-2,knots)+self.I(K-1,K-1,knots)
        return y
    
    def final_Omega(self,x):
        knots=np.sort(x)
        Omega=np.zeros([len(knots),len(knots)])
        for j in range(len(knots)-2):
            for k in range(len(knots)-2):
                Omega[j+2][k+2]=self.pointwise_Omega(j+2,k+2,knots)
        return Omega
    
    def f_hat(self,x,l):
        Omega=self.final_Omega(x)
        N=self.create_N(x)
        y=self.y_real(x)
        Nt=np.transpose(self.create_N(x))
        NtN=np.dot(Nt,N)
        inv=np.linalg.inv(NtN+ l*Omega)
        item=np.dot(N,inv)
        S_lambda=np.dot(item,Nt)
        f_hat=np.dot(S_lambda,y)
        return f_hat
    
    def plot(self, range=100, l=0.0022):

        A=np.linspace(0,1,range)
        plt.scatter(self.x,self.f_real(self.x))

        plt.plot(A,self.f_hat(A,l=l), color='g',label='$\hat{f}_{pred}$')
        plt.plot(A,self.f_real(A), color='b', label='$f_{real}$')

        plt.legend()
        plt.show()
        