# The Validator 🧮

**The Validator** is a Python project that allows you to retrieve and visualize stock market data for a given ticker. The project uses [yfinance](https://pypi.org/project/yfinance/) to fetch the data and calculates various financial metrics.

In its final version, **The Validator** will be a financial analysis and valuation tool designed to automate the extraction and analysis of company data.

![coverage](https://img.shields.io/badge/coverage-25%25-yellow)

---

**Table of Contents**

- [Installation](#installation-️)
- [Execution / Usage](#execution--usage-)
- [Technologies](#technologies)
- [Features](#features-)
- [Project Structure](#project-structure-)
- [Contribution](#contribution-)
- [Author](#author)
- [Change log](#change-log-)
- [License](#license-)
- [About](#about-)

---

## Installation 🛠️
### Prerequisites
- Python 3.8 or later
- pip

### Installation Steps
1. Clone this repository:
```bash
   git clone https://github.com/your-username/AlphaPicks_TheValidator.git
   cd AlphaPicks_TheValidator
```
2. Create and activate a virtual environment:
```bash
    python3 -m venv env
    source env/bin/activate
```
3. Install the dependencies:
```bash
   pip install -r requirements.txt
```

---

## Execution / Usage 🚀
### Quick Exemple
  1. Open the main.py file and run it to analyse a company:
```bash
    python3 src/main.py
```
2. Enter the stock ticker when prompted (e.g., AAPL)

### Exemple Output
```plaintext
    Enter the stock ticker symbol (or 'exit' to quit): aapl
    INFO:data_loader:Fetching data for AAPL...

    📊 Analysis for AAPL
    Pays d'opération.............. United States
    Score ESG..................... N/A (Data not available)
    Performance 10 ans vs S&P500.. 594.41%
    Performance 20 ans vs S&P500.. 19700.03%
    PER........................... 37.46
    PEG........................... N/A (Data not available)
    Tendance actions.............. 1.05%/an ↗
    P/FCF......................... N/A (Data not available)
    Payout Ratio.................. 15.71%
    Années dividendes consécutives 1.00
    Croissance divid. 5 ans....... 61.00
    Croissance divid. 10 ans...... N/A (Data not available)
    Marge brute................... 46.21
    Marge nette................... 23.97
    FCF Margin.................... N/A (Invalid revenue data)
    ROCE.......................... N/A (Data not available)
    ROE........................... 157.41%
    ROA........................... 21.46%
    Années CA croissant........... 2
    CA CAGR 5 ans................. N/A (Data not available)
    CA CAGR 10 ans................ N/A (Data not available)
    Années résultat net croissant. 1
    Résultat net CAGR 5 ans....... N/A (Data not available)
    Années FCF croissant.......... 2
    FCF CAGR 5 ans................ N/A (Data not available)
    Interest Coverage............. N/A (Data not available)
    Debt/Equity................... 209.06x
    Debt/EBITDA................... N/A (Data not available)
```

---

## Technologies 🖥️
- [![Python](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)

### Dependencies
- yfinance==0.2.52
- pandas==2.0.3
- numpy==1.24.4
- matplotlib==3.7.5
- logging (built-in)

---

## Features ✨
- [x] 📊 **Financial Analysis**: Extract key data such as P/E ratio, net margin, debt-to-equity ratio, and more.
- [ ] 🔍 **Customizable Criteria**: Evaluate companies based on growth, momentum, dividends, and other metrics.
- [ ] 📈 **Global Scoring**: Calculate a score out of 20 to compare multiple companies.
- [ ] 💾 **Export Results**: Save analyses to a CSV file for easy tracking.

---

## Project Structure 📂
```filetree
    ├── src
    │   ├── __init__.py
    │   ├── main.py                             # Main script to fetch data and analyze stock metrics
    │   ├── data_loader.py                      # Retrieves stock market data for a given ticker
    │   ├── metrics_calculator.py               # Calculates financial metrics
    │   ├── metrics_macro.py                    # Macro-level metrics such as ESG score and market performance
    │   ├── metrics_valuation.py                # Valuation metrics like P/E and PEG ratio
    │   ├── metrics_dividend.py                 # Dividend-related metrics
    │   ├── metrics_profitability.py            # Profitability metrics like margins and FCF
    │   ├── metrics_rentability.py              # Return-based metrics such as ROE and ROA
    │   ├── metrics_growth.py                   # Growth metrics (CAGR, revenue growth, etc.)
    │   ├── metrics_health.py                   # Financial health indicators (Debt/Equity, Interest Coverage)
    │   ├── utils.py                            # Helper functions for data extraction and formatting
    ├── requirements.txt                        # Lists all Python dependencies
    ├── rating_criteria.txt                        # Lists all Python dependencies
    └── README.md
```

---

## Contribution 🤝
Contributions are welcome! If you have ideas or improvements, feel free to submit an **issue** or a **pull request**.

---

## Author 👤
[@MaKSiiMe](https://github.com/MaKSiiMe)

---

## Change log 🚧
- **0.0.3**
  - Improved error handling and data validation.
  - Added better support for missing financial metrics.
- **0.0.2**
  - Initial working version with basic functionality to fetch and calculate stock data metrics.
  - Improved data cleaning and error handling.
- **0.0.1**
  - First working version

---

## License 📄
This project is licensed under the MIT License. See the [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) file for details.

---

## About 💡
Created by [@MaKSiiMe](https://x.com/MaKSiiMe12) to automate and simplify financial analysis. For questions, reach out at maxime.truel@holbertonstudents.com
