# DateFixTool
![](images/BadDates.png)
![](images/GoodDates.png)

## About
This is a project I put together to easily edit messy dates in Excel sheets. 
## How It Works
Using `dateutil.parser', the dateFix() function is able to recognize and pull dates from strings then convert them to datetime objects. 

The ExcelHandler() function reads in an Excel file, finds the column labeled "Date", converts the original values to datetime objects, and finally 
saves a new file with the corrected date format. 
## How to Use This Tool
To edit your Excel sheet be sure to have a column labeled "Date", then paste your file path into the ExcelHandler(). 

