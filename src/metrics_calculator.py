#!/usr/bin/python3

from metrics_macro import calculate_macro_metrics
from metrics_valuation import calculate_valuation_metrics
from metrics_dividend import calculate_dividend_metrics
from metrics_profitability import calculate_profitability_metrics
from metrics_rentability import calculate_rentability_metrics
from metrics_growth import calculate_growth_metrics
from metrics_health import calculate_health_metrics
import logging

logger = logging.getLogger(__name__)

def calculate_metrics(ticker, info, hist, financials, cashflow):
    """Calculate all stock evaluation metrics."""
    metrics = {}
    
    try:
        metrics.update(calculate_macro_metrics(info, hist))
        metrics.update(calculate_valuation_metrics(info, ticker))
        metrics.update(calculate_dividend_metrics(info))
        metrics.update(calculate_profitability_metrics(info, financials, cashflow))
        metrics.update(calculate_rentability_metrics(info))
        metrics.update(calculate_growth_metrics(financials))
        metrics.update(calculate_health_metrics(info, cashflow))
    except Exception as e:
        logger.warning(f"Error calculating metrics: {str(e)}")
    
    return metrics