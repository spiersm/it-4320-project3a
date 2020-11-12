'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal

def isInputValid(self, symbol):
        # Query paramaters
        data = {
            "function":Constants.SYMBOL_SEARCH,
            "keywords":symbol,
            "apikey":Constants.API_KEY
        }

        # Query symbol search API
        apiCall = requests.get(Constants.API_URL, params=data)
        response = apiCall.json()

        # for each returned match
        matches = []
        for match in response["bestMatches"]:
            # if an exact match symbol is valid; return true
            if(match["1. symbol"].upper() == symbol.upper()):
                return True
            else:
                matches.append(match["1. symbol"])


#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

