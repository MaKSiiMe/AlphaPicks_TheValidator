#!/usr/bin/python3

import numpy as np


def calculate_metrics(info, hist):
    """Calcule les métriques nécessaires à partir des informations et des données historiques."""
    metrics = {}

    # Score Macro - Objectif: evaluver l'impact de la société sur le monde
    metrics['Number of Countries'] = info.get('country', 'N/A')
    metrics['ESG Score'] = info.get('esgScores', {}).get('totalEsg', 'N/A')
    metrics['10-Year Performance'] = round((hist['Close'][-1] / hist['Close'][-252*10] - 1) * 100) if len(hist) > 252*10 else 'N/A'
    metrics['20-Year Performance'] = round((hist['Close'][-1] / hist['Close'][-252*20] - 1) * 100) if len(hist) > 252*20 else 'N/A'

    # Score Valorisations - Objectif: evaluer le prix et a valeur intrinsèque de l'action en bourse
    metrics['P/E Ratio'] = info.get('trailingPE', 'N/A')
    metrics['PEG Ratio'] = info.get('pegRatio', 'N/A')

    if 'Shares Outstanding' in info:
        shares_outstanding = info['Shares Outstanding']
        if len(shares_outstanding) > 1:
            metrics['Shares Buyback Trend'] = round((shares_outstanding[-1] / shares_outstanding[0] - 1) * 100)
        else:
            metrics['Shares Buyback Trend'] = 'N/A'
    else:
        metrics['Shares Buyback Trend'] = 'N/A'

    metrics['P/FCF'] = info.get('priceToFreeCashFlow', 'N/A')

    # Score Dividendes - Objectif: evaluer la solidité du dividende
    metrics['Payout Ratio'] = round(info.get('payoutRatio', 0) * 100) if info.get('payoutRatio') is not None else 'N/A'
    metrics['Consecutive Years of Dividends'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['5-Year Dividend Growth'] = round(info.get('fiveYearAvgDividendYield', 0) * 100) if info.get('fiveYearAvgDividendYield') is not None else 'N/A'
    metrics['10-Year Dividend Growth'] = 'N/A'  # Nécessite des données supplémentaires

    # Score Profitabilité - Objectif: mesure les profits de la société
    metrics['Gross Margin'] = round(info.get('grossMargins', 0) * 100) if info.get('grossMargins') is not None else 'N/A'
    metrics['Net Margin'] = round(info.get('profitMargins', 0) * 100) if info.get('profitMargins') is not None else 'N/A'
    metrics['FCF Margin'] = 'N/A'  # Nécessite des données supplémentaires

    # Score Rentablité - Objectif: mesure la rentabilité de la société
    metrics['ROCE'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['ROE'] = round(info.get('returnOnEquity', 0) * 100) if info.get('returnOnEquity') is not None else 'N/A'
    metrics['ROA'] = round(info.get('returnOnAssets', 0) * 100) if info.get('returnOnAssets') is not None else 'N/A'

    # Score Croissance - Objectif: mesure la croissance interne de l'entreprise
    metrics['Consecutive Years of Revenue Growth'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['5-Year Revenue CAGR'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['10-Year Revenue CAGR'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['Consecutive Years of Net Income Growth'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['5-Year Net Income CAGR'] = 'N/A'  # Nécessite des données supplémentaires

    # Score Santé Financière - Objectif: evaluer la solvabilité de l'entreprise et son flux de trésorerie disponible
    metrics['Consecutive Years of FCF Growth'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['5-Year FCF CAGR'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['Interest Coverage'] = 'N/A'  # Nécessite des données supplémentaires
    metrics['Debt/Equity'] = round(info.get('debtToEquity', 0) * 100) if info.get('debtToEquity') is not None else 'N/A'
    metrics['Debt/EBITDA'] = info.get('debtToEbitda', 'N/A')

    return metrics
