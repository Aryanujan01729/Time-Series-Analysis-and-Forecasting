import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
from data_downloader import get_data

def trend_deter(symbol:str,start:str,end:str,confidence:float)->bool:
    df=get_data(symbol,start,end)
    price= pd.to_numeric(df['Close'].squeeze(), errors='coerce').values
    n=len(price)
    time=df.index
    plt.plot(time,price)
    plt.ylabel('price')
    plt.xlabel('time')
    plt.show()

    Q=0
    for i in range(0,n):
        for j in range(i+1,n):
            if price[i]>price[j]:
                Q+=1

    tau=1-((4*Q)/(n*(n-1)))
    var= (2*(2*n+5))/(9*n*(n-1))

    z_score= (tau-0)/np.sqrt(var)
    z_score=abs(z_score)
    Z=norm.ppf(confidence)

    if z_score> Z:
        return True
    else:
        return False
    

    