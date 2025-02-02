#!/usr/bin/python3

from utils import get_metric

def calculate_rentability_metrics(info):
    """Calculate rentability-related metrics"""
    metrics = {}

    # Critère 16: ROCE
    metrics['ROCE'] = get_metric(info, 'returnOnCapitalEmployed', 'N/A', lambda x: round(x*100, 2))
    
    # Critère 17: ROE
    metrics['ROE'] = get_metric(info, 'returnOnEquity', 'N/A', lambda x: round(x*100, 2))
    
    # Critère 18: ROA
    metrics['ROA'] = get_metric(info, 'returnOnAssets', 'N/A', lambda x: round(x*100, 2))

    return metrics
