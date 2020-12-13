from dateparser.search import search_dates 
from pandas import ExcelWriter, read_excel
import xlrd
import openpyxl
import datetime
import dateutil.parser as dparser

# Reads and writes Excel files 
# Calls 'dateFix' to edit column labled "Dates"
def ExcelHandler(FileName):
    ExcelInput = read_excel(FileName, converters={'Date':dateFix})
    with ExcelWriter('Fixed_File.xlsx', engine='xlsxwriter') as writer:
        ExcelInput.to_excel(writer)
        
# Parses dates from strings and makes them datetime objects ready for import 
def dateFix(bdate):
    if type(bdate) is datetime.datetime:
        return bdate 
    matches = dparser.parse(bdate,fuzzy=True)
    return matches

ExcelHandler('BadDates.xlsx')