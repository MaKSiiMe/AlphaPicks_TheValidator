#!/usr/bin/python3

from data_loader import fetch_data
from metrics_calculator import calculate_metrics

print("Script started")


def main():
    print("Main function started")
    ticker = input("Enter the stock ticker symbol: ")  # Allow the user to input a stock ticker symbol
    info, hist, financials, cashflow = fetch_data(ticker)
    if info is not None and hist is not None and financials is not None and cashflow is not None:
        metrics = calculate_metrics(info, hist, financials, cashflow)
        for key, value in metrics.items():
            print(f"\033[1m{key}:\033[0m {value}")  # Afficher les informations en gras


if __name__ == "__main__":
    print("Executing main function")
    main()
    print("Script finished")
