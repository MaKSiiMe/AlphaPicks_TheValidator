#!/usr/bin/python3

import yfinance as yf

def fetch_data(ticker):
    """Récupère les données boursières pour un ticker donné et nettoie les données."""
    try:
        print(f"Fetching data for {ticker}...")
        data = yf.download(ticker)
        print(f"Data for {ticker} fetched successfully.")
        
        # Nettoyer les données
        data = data.dropna()  # Supprimer les lignes avec des valeurs manquantes
        data = data.astype(float)  # Convertir toutes les colonnes en float
        
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None