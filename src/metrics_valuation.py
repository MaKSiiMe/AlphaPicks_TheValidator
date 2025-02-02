#!/usr/bin/python3

from utils import get_metric
import yfinance as yf
import numpy as np
import logging

logger = logging.getLogger(__name__)

def calculate_valuation_metrics(info, ticker):
    """Calculate valuation-related metrics."""
    metrics = {}
    metrics['PER'] = get_metric(info, 'trailingPE', 'N/A', lambda x: round(x, 2))
    metrics['PEG'] = get_metric(info, 'pegRatio', 'N/A', lambda x: round(x, 2))
    
    try:
        if isinstance(ticker, str):
            stock = yf.Ticker(ticker.upper())
            shares_data = stock.history(period="max")['Close']
            
            if not shares_data.empty and len(shares_data) >= 2:
                trend = np.polyfit(np.arange(len(shares_data)), shares_data.values, 1)[0]
                metrics['Tendance actions'] = f"{trend:.2%}/an" + (" ↗" if trend > 0 else " ↘")
            else:
                metrics['Tendance actions'] = 'N/A (Insufficient data)'
        else:
            metrics['Tendance actions'] = 'N/A (Invalid ticker)'
    except Exception as e:
        logger.error(f"Error calculating share trend: {str(e)}")
        metrics['Tendance actions'] = 'N/A'
    
    metrics['P/FCF'] = get_metric(info, 'priceToFreeCashFlow', 'N/A', lambda x: round(x, 2))
    
    return metrics