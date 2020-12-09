from dateparser.search import search_dates 
from pandas import ExcelWriter, read_excel
import xlrd
import openpyxl

badDate = "bought on September 9th 20"

def ExcelHandler(FileName):
    ExcelInput = read_excel(FileName)
    with ExcelWriter('Fixed_File.xlsx', engine='xlsxwriter') as writer:
        ExcelInput.to_excel(writer)

def dateFix(bdate): 
    matches = search_dates(bdate) 
    firstMatch =  matches[0]
    goodDate = firstMatch[1]
    print(goodDate) 

dateFix(badDate)
ExcelHandler('BadDates.xlsx')