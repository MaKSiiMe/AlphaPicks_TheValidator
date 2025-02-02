#!/usr/bin/python3

from utils import get_metric, calculate_cagr, get_consecutive_years

def calculate_health_metrics(info, cashflow):
    """Calculate financial health-related metrics"""
    metrics = {}

    metrics['Années FCF croissant'] = get_consecutive_years(cashflow['Free Cash Flow'])
    
    try:
        fcf_5y = cashflow['Free Cash Flow'].iloc[-5:]
        metrics['FCF CAGR 5 ans'] = calculate_cagr(fcf_5y.iloc[0], fcf_5y.iloc[-1], 5)
    except:
        metrics['FCF CAGR 5 ans'] = 'N/A'
    
    metrics['Interest Coverage'] = get_metric(info, 'interestCoverage', 'N/A', lambda x: round(x, 2))
    metrics['Debt/Equity'] = get_metric(info, 'debtToEquity', 'N/A', lambda x: round(x, 2))
    metrics['Debt/EBITDA'] = get_metric(info, 'debtToEbitda', 'N/A', lambda x: round(x, 2))

    return metrics