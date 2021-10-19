
import requests 
import json
import pandas as pd
import sys 


if __name__ == "__main__":
    if (len(sys.argv)!=4):# if user does not pass an input
        print ('Usage python filename csv_file_name')
        sys.exit(1)
        
    try:
        df_country = pd.read_json(sys.argv[1])  ### read data 
        df_city = pd.read_json(sys.argv[2])
        df_language = pd.read_json(sys.argv[3])
        
        ## join two dataframe based on ID and capital
        df = df_city.merge(df_country[df_country.Continent == 'North America'], 
                   left_on='ID', 
                   right_on="Capital", how='inner')
    ### select countries and captical city name
        df_ans = df[['Name_y','Name_x']]
        
        print(df_ans)
        
    
    except ValueError:
        print('error occur')