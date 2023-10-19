# fetch-receipt-processor
Fetch backend exercise for a receipt processor written by Albert Men.

# Installation
Things you'll need to install:
Python3
Flask


To install python3, first check if you have it installed using 
```
python3 --version
```
If not, please download the installer here: https://www.python.org/downloads/ and verify using the command above

To install flask, run
```
pip3 install Flask
```
You can also verify that you have flask installed with
```
flask --version
```

# Running the Code
```
python3 main.py
```

# Testing
```
python3 tests.py
```
Some edge cases and assumptions considered:
Date/time/price is properly formatted with no invalid dates (eg. 2024-02-59) or times (26:01) when getting passed in.

A time is right on 2pm/4pm: 2pm is considered within the time frame, 4pm is not.

I did my rest api testing using Postman, sending the example jsons (and creating my own tests).
An alternative is to use curl.


