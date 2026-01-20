import numpy as np
import pandas as pd
from scipy.stats import t
from data_downloader import get_data

def linear_reg(symbol:str, start:str,end:str, confidence: float)->bool:
    df=pd.DataFrame()
    df=get_data(symbol,start,end)
    price= pd.to_numeric(df['Close'].squeeze(), errors='coerce').values
    t_sum=0
    y=0
    n=len(price)
    for i in range(0,n):
        t_sum+=i
        y=y+price[i]

    t_bar=t_sum/n
    y_bar=y/n
    cov=0
    var=0
    beta=0
    for i in range(0,n):
        cov+= (i-t_bar)*(price[i]-y_bar)

    for i in range(0,n):
        var+=(i-t_bar)**2

    beta=cov/var
    print(cov)
    print(var)
    alpha_hat = y_bar- beta* t_bar
    residual=0.0
    for i in range(0,n):
        residual+=(price[i]-alpha_hat-beta*i)**2

    residual=residual/(n-2)
    print(residual)
    SD=np.sqrt(residual/var)
    print(beta)
    print(SD)
    T= abs(beta/SD)
    alpha=1-confidence
    t_score=t.ppf(1-alpha/2,n-2)

    print(T)
    print(t_score)

    if T>t_score:
        return True
    else:
        return False

    
    
        
    
    