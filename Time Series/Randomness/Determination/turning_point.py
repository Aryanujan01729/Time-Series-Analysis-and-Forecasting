import numpy as np
import pandas as pd
from data_downloader import get_data
from scipy.stats import norm

def turning_test(symbol:str,start:str,end:str,confidence:float)->bool:
    df=get_data(symbol,start,end)
    price=pd.to_numeric(df['Close'].squeeze(),errors='coerce').values
    n=len(price)
    U=0
    for i in range(1,n-1):
        if (price[i-1]>price[i] and price[i+1]>price[i]) or (price[i-1]<price[i] and price[i+1]<price[i]):
            U+=1
    E=(2/3)*(n-2)
    V= (16*n-29)/90
    z_score=abs((U-E))/np.sqrt(V)
    alpha=1-confidence
    z_crit=norm.ppf(1-alpha/2)
    print(U)
    print(z_score)
    print(z_crit)
    if z_score > z_crit:
        return True
    else:
        return False