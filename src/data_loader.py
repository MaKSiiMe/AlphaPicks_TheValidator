#!/usr/bin/python3

import yfinance as yf
import pandas as pd
from typing import Tuple, Dict, Optional, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_data(ticker: str) -> Tuple[Optional[Dict[str, Any]], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Fetch stock market data for a given ticker.
    """
    logger.info(f"Fetching data for {ticker}...")
    try:
        stock = yf.Ticker(ticker)

        # Basic Info
        try:
            info = stock.info
        except Exception as e:
            logger.error(f"Error fetching info for {ticker}: {e}")
            info = None

        # Historical Data
        try:
            hist = stock.history(period="max")
            hist = hist.fillna(0)
            hist = hist.astype(float)
        except Exception as e:
            logger.error(f"Error fetching historical data for {ticker}: {e}")
            hist = pd.DataFrame()

        # Financial Statements
        try:
            financials = stock.financials.T.fillna(0)
        except Exception as e:
            logger.error(f"Error fetching financials for {ticker}: {e}")
            financials = pd.DataFrame()

        # Cash Flow Statements
        try:
            cashflow = stock.cashflow.T.fillna(0)
        except Exception as e:
            logger.error(f"Error fetching cashflow for {ticker}: {e}")
            cashflow = pd.DataFrame()

        if hist.empty:
            logger.warning(f"No historical data found for {ticker}.")
        if financials.empty:
            logger.warning(f"No financial data found for {ticker}.")
        if cashflow.empty:
            logger.warning(f"No cashflow data found for {ticker}.")

        return info, hist, financials, cashflow

    except Exception as e:
        logger.error(f"Unexpected error fetching data for {ticker}: {e}")
        return None, pd.DataFrame(), pd.DataFrame(), pd.DataFrame()