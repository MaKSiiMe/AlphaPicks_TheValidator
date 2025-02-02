#!/usr/bin/python3

from utils import get_metric, calculate_cagr
import yfinance as yf
import logging

def calculate_macro_metrics(info, hist):
    """Calculate macro-related metrics"""
    metrics = {}

    # Critère 1: Nombre de pays
    metrics['Pays d\'opération'] = get_metric(info, 'country', 'N/A')

    # Critère 2: Note ESG
    metrics['Score ESG'] = get_metric(info.get('esgScores', {}), 'totalEsg', 'N/A')

    # Critères 3-4: Performance relative vs S&P500
    sp500 = yf.Ticker('^GSPC').history(period='max')['Close'].values
    metrics['Performance 10 ans vs S&P500'] = calculate_sp500_comparison(hist['Close'], 10)
    metrics['Performance 20 ans vs S&P500'] = calculate_sp500_comparison(hist['Close'], 20) if len(hist) >= 252*20 else 'N/A (Insufficient data)'

    return metrics

def calculate_sp500_comparison(ticker_hist, years):
    """Compare performance with S&P 500"""
    try:
        sp500 = yf.Ticker('^GSPC').history(period=f"{years}y")
        common_dates = ticker_hist.index.intersection(sp500.index)
        if len(common_dates) < 1:
            return 'N/A (No common trading days)'

        ticker_return = (ticker_hist[common_dates[-1]] / ticker_hist[common_dates[0]] - 1) * 100
        sp500_return = (sp500['Close'][common_dates[-1]] / sp500['Close'][common_dates[0]] - 1) * 100

        return f"{ticker_return - sp500_return:.2f}%"
    except Exception as e:
        logging.error(f"SP500 comparison failed: {str(e)}")
        return 'N/A'
