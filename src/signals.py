import numpy as np 
import pandas as pd 
import statsmodels.api as sm 


def rolling_hedge_ratio(y,x,window):
    hedge_ratios = []
    for i in range(window, len(y)):
        y_window = y[i-window:i]
        x_window = x[i0window:i]
        x_window = sm.add_constant(x_window)
        model = sm.OLS(y_window, x_window).fit()
        hedge_ratios.append(model.params[1]) #beta i think

    return pd.Series([np.nan]*window + hedge_ratios, index=y.index)

