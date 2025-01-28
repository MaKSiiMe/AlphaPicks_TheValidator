# The Validator 🧮

**The Validator** is a Python project that allows you to retrieve and visualize stock market data for a given ticker. The project uses [yfinance](https://pypi.org/project/yfinance/) to fetch the data and calculates various financial metrics.
In its final version, **The Validator** will be a financial analysis and valuation tool designed to automate the extraction and analysis of company data.

![coverage](https://img.shields.io/badge/coverage-10%25-orangered)

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
2. Create and
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
    Script started
    Executing main function
    Main function started
    Enter the stock ticker symbol: AAPL
    Fetching data for AAPL...
    Number of Countries: United States
    ESG Score: N/A
    10-Year Performance: 842.1973845667312
    20-Year Performance: 21637.275297384524
    P/E Ratio: 37.805923
    PEG Ratio: N/A
    Shares Outstanding Trend: N/A
    P/FCF: N/A
    Payout Ratio: 0.1612
    Consecutive Years of Dividends: N/A
    5-Year Dividend Growth: 0.61
    10-Year Dividend Growth: N/A
    Gross Margin: 0.46206
    Net Margin: 0.23971
    FCF Margin: N/A
    ROCE: N/A
    ROE: 1.5741299
    ROA: 0.21464
    Consecutive Years of Revenue Growth: N/A
    5-Year Revenue CAGR: N/A
    10-Year Revenue CAGR: N/A
    Consecutive Years of Net Income Growth: N/A
    5-Year Net Income CAGR: N/A
    Consecutive Years of FCF Growth: N/A
    5-Year FCF CAGR: N/A
    Interest Coverage: N/A
    Debt/Equity: 209.059
    Debt/EBITDA: N/A
    Plotting data for AAPL...
    Data for AAPL plotted successfully.
    Script finished
```

---

## Technologies
- [![Python](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)

### Dependencies
- yfinance==0.2.52
- pandas==2.0.3

---

## Features ✨
- [ ] 📊 **Financial Analysis**: Extract key data such as P/E ratio, net margin, debt-to-equity ratio, and more.
- [ ] 🔍 **Customizable Criteria**: Evaluate companies based on growth, momentum, dividends, and other metrics.
- [ ] 📈 **Global Scoring**: Calculate a score out of 20 to compare multiple companies.
- [ ] 💾 **Export Results**: Save analyses to a CSV file for easy tracking.

---

## Project Structure 📂
```filetree
    ├── src
    │   ├── __init__.py
    │   ├── main.py                             # The main file that runs the script, asks the user to input a ticker, fetches the data, and calculates the financial metrics.
    │   │       └── main()
    │   ├── data_loader.py                      # Contains the fetch_data function that retrieves stock market data for a given ticker.
    │   │       └── fetch_data()
    │   └── metrics_calculator.py               # Contains the calculate_metrics function that calculates the financial metrics.
    │           └── calculate_metrics()
    ├── requirements.txt                        # Lists all Python dependencies required for the project
    └── README.md
```

---

## Contribution 🤝
Contributions are welcome! If you have ideas or improvements, feel free to submit an **issue** or a **pull request**.

---

## Author
[@MaKSiiMe](https://github.com/MaKSiiMe)

---

## Change log 🚧
- 0.0.2
    - Initial working version with basic functionality to fetch and calculate stock data metrics.
    - Improved data cleaning and error handling.
- 0.0.1
    - First working version
- ... 

---

## License 📄
This project is licensed under the MIT License. See the [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) file for details.

---

## About 💡
Created by [@MaKSiiMe](https://x.com/MaKSiiMe12) to automate and simplify financial analysis. For questions, reach out at maxime.truel@holbertonstudents.com
