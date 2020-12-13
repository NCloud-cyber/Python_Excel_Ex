from dateparser.search import search_dates 
from pandas import ExcelWriter, read_excel
import xlrd
import openpyxl
import datetime
import dateutil.parser as dparser

def ExcelHandler(FileName):
    ExcelInput = read_excel(FileName, converters={'Date':dateFix})
    with ExcelWriter('Fixed_File.xlsx', engine='xlsxwriter') as writer:
        ExcelInput.to_excel(writer)
        

def dateFix(bdate):
    if type(bdate) is datetime.datetime:
        return bdate 
    matches = dparser.parse(bdate,fuzzy=True)
    return matches

    # matches = re.findall(r"[0-9]{1,5}\/[0-9]{2}\/[0-9]{2,5}", bdate)
    # if matches:
    #     result = datetime.datetime.strptime(matches[0],'%x')
    #     return result

    # matches = search_dates(bdate)
    # print(matches)
    # firstMatch =  matches[0]
    # goodDate = firstMatch[1]
    # return goodDate.strftime('%Y-%m-%d')

ExcelHandler('BadDates.xlsx')
# This will return something
#   re.findall(r"[0-9]{1,5}\/[0-9]{2}\/[0-9]{2,5}", "bought 10/23/96")
# That you can pass to this
#   datetime.datetime.strptime('10/23/96', '%m/%d/%y')
# to get a Date Object and then return that