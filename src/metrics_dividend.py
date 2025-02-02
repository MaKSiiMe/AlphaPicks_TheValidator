#!/usr/bin/python3

from utils import get_metric

def calculate_dividend_metrics(info):
    """Calculate dividend-related metrics"""
    metrics = {}

    metrics['Payout Ratio'] = get_metric(info, 'payoutRatio', 'N/A', lambda x: round(x*100, 2))
    metrics['Années dividendes consécutives'] = get_metric(info, 'dividendRate', 'N/A')
    metrics['Croissance divid. 5 ans'] = get_metric(info, 'fiveYearAvgDividendYield', 'N/A', lambda x: round(x*100, 2))
    metrics['Croissance divid. 10 ans'] = 'N/A'  # Non disponible dans yfinance

    return metrics