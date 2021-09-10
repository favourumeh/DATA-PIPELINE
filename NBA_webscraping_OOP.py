# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:14:14 2021

@author: favou
"""
import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd

class per_game_stats():
    def __init__(self, year_range):
        
        self.year_range = year_range #list of years to extract: [starting_year, final_year]
       
#genrating list of years in specified year range        
    def generate_year_list(self):
        if len(self.year_range) == 1:
            self.year_range = [self.year_range[0], self.year_range[0]]
            
        self.year_list = [year for year in range(self.year_range[0], self.year_range[1]+1)]
    
#genrating the Beautiful soup object of the per game stats webpage
    def generate_BS_object(self):
        url = f"https://www.basketball-reference.com/leagues/NBA_{self.year}_per_game.html"
        r = requests.get(url)
        self.soup= bs(r.text, "html5lib")

#generating a list of column headings
    def generate_column_heading_list(self):
        table_headings = self.soup.select("div #div_per_game_stats thead th")  #--element.ResultSet (list)
        self.table_heading_list = [heading.text for heading in table_headings ]
            
#selecting (list of) the tables row elements from the table
    def generate_table_row_elements(self):
        self.table_rows = self.soup.select("div #div_per_game_stats tbody tr") #--element.ResultSet (list)

#Storing table rows in the pandas df
    def generate_raw_pandas_df(self):
        per_game_stats_df = pd.DataFrame(columns = self.table_heading_list) #empty df skeleton
        
        for row in self.table_rows :
            fields = row.find_all(["td","th"])
            fields_list = [field.text for field in fields]
        
            series = pd.Series(fields_list, index = self.table_heading_list)
            per_game_stats_df = per_game_stats_df.append(series, ignore_index = True)
        
        self.per_game_stats_df = per_game_stats_df
        
        
#deleting the rows where the headings are repeated using the Age column 
    def deleting_repeated_headings(self):
        #df1 = df..index(df[df["column"] == "string"].index)
        self.cleaned_pg_stats = self.per_game_stats_df.drop(self.per_game_stats_df[self.per_game_stats_df["Age"] == "Age"].index) #--df    
             

#dropping rank column 
    def dropping_rank_column(self):
        self.pg_stats = self.cleaned_pg_stats.drop('Rk', 1) # 0 to delete rows, 1 to delete columns

#Adding a year column 
    def adding_year_column(self):
        self.pg_stats["Year"] = self.year
        return self.pg_stats
    
#iterating through different years 
    def iterate_year(self):
        per_game_stats.generate_year_list(self)
        
        for i,year in enumerate(self.year_list):
            self.year = year

            per_game_stats.generate_BS_object(self)
            per_game_stats.generate_column_heading_list(self)
            per_game_stats.generate_table_row_elements(self)
            per_game_stats.generate_raw_pandas_df(self)
            per_game_stats.deleting_repeated_headings(self)
            per_game_stats.dropping_rank_column(self)
            
            if i == 0:
                df = per_game_stats.adding_year_column(self)
            else:
                df1 = per_game_stats.adding_year_column(self)
                df = df.append(df1, ignore_index = True)
        
        df = per_game_stats.cleaning_df(self,df)
        return df 

#Perfoming various cleaning operation to make data SQL friendly
    def cleaning_df(self, df):
        
    #1)Replacing empty fields with nans with
        from numpy import nan
        df.replace('', nan, inplace=True)
    
    #2)Replacing the "%" symbol from the column headings with "_per
        column_list = list(df.columns)
        col_list = []
        for i in column_list:
            ind =i
            if "%" in i:
                ind = i.replace("%", "_per")
            col_list.append(ind)
        
        df.columns = col_list
    #3) Removing all 'TOT' teams
        df = df.drop(df[df["Tm"]== 'TOT'].index)
        return df
    

#Testing(keep commented to avoid accidental run)
# A = per_game_stats([2021])

# B = A.iterate_year()





