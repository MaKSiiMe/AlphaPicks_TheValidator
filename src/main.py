import logging
from typing import Dict, Any
import pandas as pd
from data_loader import fetch_data
from metrics_calculator import calculate_metrics

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_valid_ticker(ticker: str) -> bool:
    """Check if the ticker has a valid format."""
    return len(ticker) >= 2 and ticker.isalnum()

def display_metrics(metrics: Dict[str, Any]) -> None:
    """Format and display metrics with units and explanations."""
    units = {
        "10-Year Performance": "%",
        "20-Year Performance": "%",
        "Payout Ratio": "%",
        "5-Year Dividend Growth": "%",
        "Gross Margin": "%",
        "Net Margin": "%",
        "ROE": "%",
        "ROA": "%",
        "Debt/Equity": "x",
        "Market Cap": "B",  # Billions
        "Dividend Yield": "%",
    }
    
    for key, value in metrics.items():
        unit = units.get(key, "")
        if value == "N/A" or pd.isna(value):
            print(f"{key:.<30} N/A (Data not available)")
        elif isinstance(value, float):
            print(f"{key:.<30} {value:.2f}{unit}")
        else:
            print(f"{key:.<30} {value}{unit}")

def main() -> None:
    """Main execution flow."""
    logger.info("Starting The Validator")
    
    while True:
        ticker = input("\nEnter the stock ticker symbol (or 'exit' to quit): ").strip().upper()
        if ticker == 'EXIT':
            break
        if not is_valid_ticker(ticker):
            print("❌ Invalid ticker. Use only letters/numbers (ex: AAPL).")
            continue
            
        try:
            # Fetch data
            info, hist, financials, cashflow = fetch_data(ticker)
        except Exception as e:
            logger.error(f"Data fetch failed for {ticker}: {str(e)}")
            continue
            
        # Validate data
        if (
            info is None or hist is None or financials is None or cashflow is None
            or hist.empty or financials.empty or cashflow.empty
        ):
            logger.warning(f"Partial or empty data for {ticker}. Some metrics may be missing.")
            continue
            
        # Calculate metrics
        try:
            metrics = calculate_metrics(ticker, info, hist, financials, cashflow)
            print(f"\n📊 Analysis for {ticker}")
            display_metrics(metrics)
        except Exception as e:
            logger.error(f"Error calculating metrics for {ticker}: {str(e)}")
            continue
    
    logger.info("Script terminated successfully")

if __name__ == "__main__":
    main()
