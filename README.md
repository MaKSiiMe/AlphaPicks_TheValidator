# The Validator 🧮

**The Validator** is a Python project that allows you to retrieve and visualize stock market data for a given ticker. The project uses [yfinance](https://pypi.org/project/yfinance/) to fetch the data, [pandas](https://pypi.org/project/pandas/) to analyse the data and [matplotlib](https://pypi.org/project/matplotlib/) to plot the closing price charts.
In its final version, **The Validator** will be a financial analysis and valuation tool designed to automate the extraction and analysis of company data.

![coverage](https://img.shields.io/badge/coverage-10%25-orangered)

---
**Table of Contents**

- [Installation](#Installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Project Structure](Project-Structure)
- [Contribution](#contribution)
- [Author](#author)
- [Change log](#change-log)
- [License](#license)

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
    Entrez le ticker de l'action : AAPL
    Fetching data for AAPL...
    [*********************100%***********************]  1 of 1 completed
    Data for AAPL fetched successfully.
    Price          Close      High       Low      Open       Volume
    Ticker          AAPL      AAPL      AAPL      AAPL         AAPL
    Date                                                           
    1980-12-12  0.098834  0.099264  0.098834  0.098834  469033600.0
    1980-12-15  0.093678  0.094108  0.093678  0.094108  175884800.0
    1980-12-16  0.086802  0.087232  0.086802  0.087232  105728000.0
    1980-12-17  0.088951  0.089381  0.088951  0.088951   86441600.0
    1980-12-18  0.091530  0.091959  0.091530  0.091530   73449600.0
    Plotting data for AAPL...
    Data for AAPL plotted successfully.
    Script finished
```

---

## Technologies
- [![Python](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)

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
    │   ├── main.py                         # The main file that runs the script, asks the user to input a ticker, fetches the data, and displays the chart
    │   │       └── main()                          # Entry point to execute the application
    │   ├── data_loader.py                  # Contains the fetch_data function that retrieves stock market data for a given ticker
    │   │       └── fetch_data()                    # Fetch stock market data for a given ticker
    │   └── plot_generator.py               # Contains the plot_data function that plots the stock market data
    │           └── plot_data()                     # Plot the stock market data
    ├── requirements.txt                    # Lists all Python dependencies required for the project
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
- 0.0.1
    - First working version
- ... 

---

## License 📄
This project is licensed under the MIT License. See the [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) file for details.

---

## About 💡
Created by [@MaKSiiMe](https://x.com/MaKSiiMe12) to automate and simplify financial analysis. For questions, reach out at maxime.truel@holbertonstudents.com