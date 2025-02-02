#!/usr/bin/python3

from utils import get_metric, calculate_cagr, get_consecutive_years

def calculate_growth_metrics(financials):
    """Calculate growth-related metrics"""
    metrics = {}

    metrics['Années CA croissant'] = get_consecutive_years(financials['Total Revenue'])
    
    try:
        rev_5y = financials['Total Revenue'].iloc[-5:]
        metrics['CA CAGR 5 ans'] = calculate_cagr(rev_5y.iloc[0], rev_5y.iloc[-1], 5)
        
        rev_10y = financials['Total Revenue'].iloc[-10:]
        metrics['CA CAGR 10 ans'] = calculate_cagr(rev_10y.iloc[0], rev_10y.iloc[-1], 10)
    except:
        metrics['CA CAGR 5 ans'] = 'N/A'
        metrics['CA CAGR 10 ans'] = 'N/A'
    
    metrics['Années résultat net croissant'] = get_consecutive_years(financials['Net Income'])
    
    try:
        ni_5y = financials['Net Income'].iloc[-5:]
        metrics['Résultat net CAGR 5 ans'] = calculate_cagr(ni_5y.iloc[0], ni_5y.iloc[-1], 5)
    except:
        metrics['Résultat net CAGR 5 ans'] = 'N/A'

    return metrics