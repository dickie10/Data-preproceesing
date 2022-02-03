import pandas as pd
import datetime
from datetime import timedelta   
ex = datetime.datetime.strptime('11:30AM', '%I:%M%p') #Intializing time 11:30 to ex
empty_dict = {} 
def conv(x,y,z):  
    if x.time() == ex.time():
        empty_dict[(str(y.date()), str(y.time()))] = z #wind power forecast at 11:30 for a particular date
  
def cal(x,y,z):   
            final_val = z - empty_dict[str(x.date()),str(x.time())] 
            return final_val

def su(x,y): #su funtion subtracts delivery_start date and time stamp date
    val = x - y 
    return val 

df = pd.read_csv("data cleaning/test_data.csv") 
df['timestamp'] = pd.to_datetime(df['timestamp'])  #converting timestamp to datetime 
df['delivery_start'] = pd.to_datetime(df['delivery_start']) #converting delivery_start to datetime 
condition1 = ((su(df['delivery_start'].dt.date ,df['timestamp'].dt.date)) == '1 days') & (df['timestamp'].dt.time >= ex.time()) #vectorized condition  
condition2 = ((su(df['delivery_start'].dt.date,df['timestamp'].dt.date)) == '0 days') #vectorized condition
df = df[condition1|condition2]  #cleaning the data,as asked in Task1
df.apply(lambda x: conv(x['timestamp'],x['delivery_start'],x['wind forecast in MW']), axis=1) #Calls the conv function with dataframes as attributes of function
df["ID Position"] = df.apply(lambda x: cal(x['delivery_start'], x['timestamp'], x['wind forecast in MW']), axis=1)#ID position calculated, according to task2
df.to_csv("data cleaning/final.csv")  



