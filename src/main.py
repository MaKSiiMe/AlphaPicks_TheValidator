#!/usr/bin/python3

from data_loader import fetch_data
from plot_generator import plot_data

print("Script started")

def main():
    print("Main function started")
    ticker = input("Enter the stock ticker: ")  # Allow the user to input a stock ticker
    data = fetch_data(ticker)
    if data is not None:
        print(data.head())  # # Display the first few rows of the data
        plot_data(data, ticker)

if __name__ == "__main__":
    print("Executing main function")
    main()
    print("Script finished")
