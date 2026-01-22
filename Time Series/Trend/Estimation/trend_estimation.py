import numpy as np
import pandas as pd
from data_downloader import get_data
import cvxpy as cp

def estimate(symbol:str,start:str,end:str,K:int)->pd.Series:
    df=get_data(symbol,start,end)
    price=pd.to_numeric(df['Close'].squeeze(),errors='coerce')
    price=price.dropna()
    price=price.values
    print(price)
    n=len(price)
    t=np.linspace(-1,1,n)
    X = np.column_stack([t**k for k in range(K+1)])
    beta=cp.Variable(K+1)

    objective=cp.Minimize(cp.sum_squares(X@beta-price))
    cp.Problem(objective).solve()
    trend=X@beta.value
    
    return pd.Series(trend,name="trend")
    
    