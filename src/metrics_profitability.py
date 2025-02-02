#!/usr/bin/python3

import logging
from utils import get_metric

def calculate_profitability_metrics(info, financials, cashflow):
    """Calculate profitability-related metrics"""
    metrics = {}

    metrics['Marge brute'] = get_metric(info, 'grossMargins', 'N/A', lambda x: round(x*100, 2))
    metrics['Marge nette'] = get_metric(info, 'profitMargins', 'N/A', lambda x: round(x*100, 2))

    try:
        revenue = get_metric(financials, 'Total Revenue', is_series=True)
        fcf = get_metric(cashflow, 'Free Cash Flow', is_series=True)
        
        if isinstance(revenue, (int, float)) and isinstance(fcf, (int, float)) and revenue > 0:
            metrics['FCF Margin'] = f"{(fcf / revenue * 100):.2f}%"
        else:
            metrics['FCF Margin'] = 'N/A (Invalid revenue data)'
    except Exception as e:
        logging.error(f"Error calculating FCF Margin: {str(e)}")
        metrics['FCF Margin'] = 'N/A'

    return metrics
