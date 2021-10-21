#  Data Pipeline: Basketball Reference 

## Note: See file "project_ETL.docx" for further description of the project)


## Basketball Reference Data Pipeline
- Created a data pipeline that can scrape and clean tabular statistical data from BasketballReference.com and store it in a local MySQL server and/or Excel workbook. 
- The pipeline was used to store over 16,000 rows of per-game statistics of players in the National Basketball Association (NBA) spanning 31 years (from 1990-2021)
- The stored data was then used in several machine learning projects namely regression and classification (see [Predicting Turnovers](https://github.com/favourumeh/Multiple_Linear_Regression---Predicting-Turnovers-) project and [Identifying Player Position](https://github.com/favourumeh/Identifying-Player-Position) project)  
- The NBA is the top professional basketball league in North America. It was founded in 1947 and is currently home to the best basketball players in the world. 
- Basketball Reference is an online depository of basketball statistics, game logs etc for different basketball leagues.  
- Feel free to try out the pipeline by cloning the repository and opening the 'data_pipeline_bball_reference_to_SQL_or_EXCEL.py' file (see the flowchart below for further details).
 

## Python version and packages 
Python Version: **3.8.3**

Packages: pandas, numpy, Bs4 (BeautifulSoup),	sqlalchemy, requests


## An overview of the processes undergone 
![](/Cleaning%20Actions.png)
![](https://github.com/favourumeh/DATA-PIPELINE/blob/main/Excel%20file%20example.png)

## How to use the tool developed 
To use the tool developed simply follow the flowchart below:

![](https://github.com/favourumeh/DATA-PIPELINE/blob/main/Pipeline%20tool%20flowchart.png)



