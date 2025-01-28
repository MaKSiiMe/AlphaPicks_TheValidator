#!/usr/bin/python3

import yfinance as yf
import pandas as pd


def fetch_data(ticker):
    """Récupère les données boursières pour un ticker donné et nettoie les données."""
    try:
        print(f"Fetching data for {ticker}...")
        stock = yf.Ticker(ticker)

        # Récupérer les informations de base
        info = stock.info

        # Récupérer les données historiques
        hist = stock.history(period="max")

        # Filtrer les données pour les 20 dernières années
        twenty_years_ago = pd.Timestamp.now() - pd.DateOffset(years=20)
        hist = hist[hist.index >= twenty_years_ago]

        # Récupérer les données financières annuelles
        financials = stock.financials.T  # Transposer pour avoir les années en index
        financials = financials[financials.index >= twenty_years_ago.year]

        # Récupérer les données de flux de trésorerie annuelles
        cashflow = stock.cashflow.T  # Transposer pour avoir les années en index
        cashflow = cashflow[cashflow.index >= twenty_years_ago.year]

        # Nettoyer les données
        hist = hist.dropna()  # Supprimer les lignes avec des valeurs manquantes
        hist = hist.astype(float)  # Convertir toutes les colonnes en float

        return info, hist, financials, cashflow
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None, None, None, None
