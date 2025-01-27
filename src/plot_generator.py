#!/usr/bin/python3

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def plot_data(data, ticker):
    """Trace les données boursières."""
    try:
        print(f"Plotting data for {ticker}...")
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label=f'Prix de clôture de {ticker}')
        plt.title(f'Prix de clôture de {ticker} au fil du temps')
        plt.xlabel('Date')
        plt.ylabel('Prix de clôture')
        plt.legend()
        plt.show()
        print(f"Data for {ticker} plotted successfully.")
    except Exception as e:
        print(f"Error plotting data for {ticker}: {e}")