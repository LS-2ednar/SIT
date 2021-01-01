import matplotlib.pyplot as plt
import numpy as np
# import math as m

#Definition of a recursiv function to describe the deterministic model
def SIT(N0, Br, Dr, S, K, GN=0): 
    """
    (S)terile (I)nsect (T)echnique:
    
    Variables:
        N0 = Inital number of fertile male insects
        Br = Birthrate
        Dr = Deathrate
        S  = Sterile male insects introduced
        K  = Carrying Capacity of the environment
        GN = Generation number
    Notes:
        Rr = Reproductionratio takes probability 
    """
    
    
    #Checking if there is no change observable over time
    if (Br/Dr)*(N0/(N0+S)) == 1:
        return print('No population change')
    
    #Reproductionratio
    if GN == 0:
        Rr = Br/Dr
    else:
        Rr = (Br*N0*(N0/(N0+S)))/(Dr*N0)
        
    #Population after one Generation
    Nt = N0*Rr*(N0/(N0+S))  
    
    #Generation number incresses by 1 
    GN += 1  
    
    #------------#
    # Plot setup #
    #------------#
    #Over Carrying Capacity
    if Nt >= K:
        x = range(0,GN)
        y =  np.arange(len(x))
        y[:] = K
        plt.plot(x,y,'r--')
        plt.xlim(0,GN)
        plt.xticks(np.arange(0,GN+1))
        plt.ylim(0,round(K*1.05))
        plt.xlabel('Generation [-]')
        plt.ylabel('Number of fertile male insects')
        plt.title(f'After {GN} generations the carrying capacitiy is reached')
        plt.show()
        return print(f'{Nt:7} fertile male insects after {GN:3} generations the carring capacity of {K} was reached !!!')
    
    #Species extinquished
    elif Nt <= 10E-5:
        plt.plot(GN,0,'k.')
        plt.xlabel('Generation [-]')
        plt.ylabel('Number of fertile male insects')
        plt.ylim(0)
        plt.xticks(np.arange(0,GN+1))
        plt.xlim(0,GN)
        plt.title(f'After {GN} generations the insects are extinguished')
        plt.show()
        
        return print(f'         Population is no longer existing after {GN:3} generations')
    
    #Calculating new population
    else:
        plt.plot(GN,Nt,'k.') 
        
        if GN == 1:
            print(f'{Nt:20.10} fertile male insects after {GN:3} generation')
        else:
            print(f'{Nt:20.10} fertile male insects after {GN:3} generations')
        return SIT(Nt,Br,Dr,S,K,GN)




# #Stochastische Berechnugnen :s
# ak = (1/(K-1))+(Br*N0*(N0/(N0+S)))/(Dr*N0)*((K-1)/(S+K-1))*ak


# Table 5.3

SIT(200,4,1,1000,1000)
# # Examples
# print('-------')
# print('Species extinguishes')
# print('-------')
# SIT(1000,12,16,100,500_000)   # Species extinguishes
# print('-------')
# print()
# print('-------')
# print('Species stays constant')
# print('-------')
# SIT(1000,12, 8,500,500_000)  # Species stays constant
# print('-------')
# print()
# print('-------')
# print("Species can't be controlled")
# print('-------')
# SIT(1000, 5, 2,200,500_000)  # Species can't be controlled
# print('-------')
