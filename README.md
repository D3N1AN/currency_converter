# currency_converter
This efficient, streamlined Python code showcases the ability to consume a currency exchange rate API and perform currency conversions. The purpose of creating this code is to demonstrate Python skills to potential employers.

# Requirements:

* Python 3.x
* requests library (install using `pip install requests`)

# What does it do?

* The code takes user input for the amount to convert, the currency to convert from, and the currency to convert to.
* exchangerate-api.com is used to fetch the latest exchange rates based on the provided API key.
* The code then calculates the converted amount using the provided exchange rate.
* If successful, the converted amount is returned and displayed. If not, a failure message is displayed.

# How does it work?
* The requests library sends HTTP requests to the API endpoint.
* Once the API response is received, the status code is checked to ensure a successful connection.
* The JSON response is then parsed to extract the conversion rates.
* The provided amount is multiplied by the conversion rate to calculate the converted amount.
* Finally, the program displays the converted amount or a failure message based on the outcome.

# Usage

* Ensure Python 3.x and the requests library are installed.
* Run the script in a terminal or command prompt: $ python currency_converter.py
* Follow on-screen prompts to enter the amount, currency to convert from, and currency to convert to.
* Ensure currency codes are written using the ISO 4217 Three Letter Currency Code (e.x. USD = United States Dollar).
* The converted amount will be displayed on the console. If the conversion fails, a failure message will appear.
  
# Listed below is an example of what a succesful input/output may look like:
* Enter the amount to convert: 100
* Enter the currency to convert from: USD
* Enter the currency to convert to: EUR
* 100.0 USD is equal to 90.14 EUR.

# Listed below is an example of what a failed input/output may look like:
* Enter the amount to convert: 100
* Enter the currency to convert from: Dollars
* Enter the currency to convert to: Euros
* Conversion failed. Please check your input.
