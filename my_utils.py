import numpy as np
import pandas as pd

def get_tax(x):
    """ref: https://www.ato.gov.au/Rates/Individual-income-tax-rates/
    """
    tax = 0
    th0 = 18200
    th1 = 45000
    th2 = 120000
    th3 = 180000
    
    tranche1 = (th1-th0+1)*0.19
    tranche2 = (th2-th1+1)*0.325
    tranche3 = (th3-th2+1)*0.37
    
    if th0 < x < (th1+1):
        tax = (x - th0)*0.19
    if th1 < x < (th2+1):
        tax = ((x - th1)*0.325) + tranche1
    if th2 < x < (th3+1):
        tax = ((x - th2)*0.37) + tranche2 + tranche1
    if x > th3:
        tax = ((x - th3)*0.45) + tranche3 + tranche2 + tranche1

    return(tax)
        
        