# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:55:08 2021

@author: favou
"""
from Key_Function import append_df_to_excel

from NBA_webscraping_OOP import per_game_stats

class pgstats_to_localSQL(per_game_stats):
    def __init__(self, year_range, host, username, password, dbname, table_name, save_to ="Excel"):
        super().__init__(year_range)
        self.host = host              #server hostname
        self.username = username      #connection username
        self.password = password      #server password 
        self.dbname = dbname          #name of database (has to be existing)
        self.table_name = table_name  #name of table inside database (can exist already otherwise will be created)
        self.save_to = save_to        #can save extracted data to: "SQL", "Excel", "both"
    
#1) Establishing connection to MySQL database
    def engine(self):
        #https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
        from sqlalchemy import create_engine
        
        connecting_string = f"mysql+pymysql://{self.username}:{self.password}@{self.host}/{self.dbname}"
        self.con = create_engine(connecting_string)
        
        #testing connection to local sql server 
        try:
            connection = self.con.connect()
            connection.close()
        except :
            print("One of the following parameters(username, password, host, dbname) maybe written incorrectly:")
            print("""To correctly enter the parameters of the connecting string go on MySQL: \n
                  a)click "database" tab,\n 
                  b)click "connect to database""")
    
            self.username = str(input("username:"))
            self.password = str(input("password:"))
            self.host = str(input("hostname:"))
            self.dbname = str(input("database name:"))


#2) sending content from df to SQL and EXCEL
    def df_to_SQL_EXCEL(self):
        
        
        #1) Generating dataframe for the specified year range (via webscraping)
        df = pgstats_to_localSQL.iterate_year(self)
        
       
        #2)df--------->Excel file "Data_store.xlsx" in current directory 
        if self.save_to in ("both", "Excel"):
            append_df_to_excel("Data_store.xlsx", df, sheet_name='Sheet1', header = None, index = False)

        
        #3)df-------->SQL database table
        if self.save_to in ("both", "SQL"):
            call = pgstats_to_localSQL.engine(self) #establishing connection to SQL server
            df.to_sql(self.table_name, self.con, index = False, if_exists="append") 
        
        return df


##################Testing######################################################

#Specify year(s) you want to extract points per-game (ppg) data from 
year_range = [2021] # is only one year then just put [year], otherwise [year1, year2] (year1<year2)

#Specify where you want to load the data to 
save_to = "Excel" # alternatives: "both" or "SQL" (default = "Excel")


#if you want to save to a local SQL server. then specify the following 
host = "...1"
username ="..."
password = "..."
dbname = "nba1"
table_name = "nba_table3"


#Call class above
A = pgstats_to_localSQL(year_range, host,username,password,dbname,table_name, save_to)

#B is the dataFrame that is appended to the Excel file: "Data_store.xlsx"
B = A.df_to_SQL_EXCEL() 
