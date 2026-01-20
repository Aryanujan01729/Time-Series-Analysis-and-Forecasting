import numpy as np
import pandas as pd
import yfinance as yf
from pathlib import Path

def get_data(symbol:str, start: str, end: str, save:bool=True)->pd.DataFrame:
    path= Path('data')/f"{symbol}.csv"
    if path.exists():
        data=pd.read_csv(path,index_col=0,parse_dates=True)
    else:
        data=yf.download(symbol,start,end)
        if save:
            path.parent.mkdir(exist_ok=True)
            data.to_csv(path)

    return data
    

    
    