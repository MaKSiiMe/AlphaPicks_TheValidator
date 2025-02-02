import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_metric(data, key=None, default='N/A', formatter=None, is_series=False):
    """Helper function to safely get metrics with formatting."""
    try:
        if is_series:
            if isinstance(data, pd.Series) and not data.empty:
                value = data.iloc[-1]  # Take the most recent value
            else:
                return default
        else:
            value = data.get(key, default) if isinstance(data, dict) else default

        if pd.isna(value) or value == default:
            return default
        
        # Convert to float if possible
        try:
            value = float(value)
        except (ValueError, TypeError):
            pass
        
        return formatter(value) if formatter else value
    except Exception as e:
        logger.error(f"Error getting metric: {str(e)}")
        return default

def calculate_cagr(start_value, end_value, years):
    """Calculate Compound Annual Growth Rate"""
    try:
        if start_value <= 0 or end_value <= 0:
            return 'N/A'
        return round(((end_value / start_value) ** (1/years) - 1) * 100, 2)
    except:
        return 'N/A'

def get_consecutive_years(series):
    """Calculate consecutive years of growth"""
    try:
        growth = series.pct_change().dropna() > 0
        return sum(np.diff(np.where(growth, 1, 0)) == 1) + 1
    except:
        return 'N/A'