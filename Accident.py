import pyodbc 
import pandas as pd 
import matplotlib.pyplot as plt 
server_name = 'LAPTOP-TMANHNM8\\SQLEXPRESS01' 
database_name = 'trafficaccident' 
consql = pyodbc.connect('DRIVER={ODBC driver 17 for SQL Server} ;\ 
SERVER=' + server_name + ' ;\ 
DATABASE=' + database_name + ' ;\ 
Trusted_Connection=yes;') 
print(consql) 
print("\nSQL Server Connection is Successful") 
cursor = consql.cursor() 
print("\nCursor object created...") 
cursor.execute("select * from traffic_accidents ") 
print("\nTable records are retrieved from the SQL Server") 
rows = cursor.fetchall() 
columns = [column[0] for column in cursor.description] 
df = pd.DataFrame.from_records(rows, columns=columns) 
print("\nDataFrame Preview:") 
print(df.head()) 
if 'Date' in df.columns: 
df['Date'] = pd.to_datetime(df['Date']) 
df['crash_date'] = pd.to_datetime(df['crash_date'], errors='coerce') 
#Accidents Over Time 
daily = df['crash_date'].value_counts().sort_index() 
daily.plot(kind='line', figsize=(10, 4)) 
plt.title("Line Chart: Accidents Over Time") 
17 
plt.xlabel("Date") 
plt.ylabel("Number of Accidents") 
plt.grid() 
plt.tight_layout() 
plt.show() 
#Accidents by Month 
df['crash_month'].value_counts().sort_index().plot(kind='line', marker='o', 
color='purple') 
plt.title("Line Chart: Accidents by Month") 
plt.xlabel("Month") 
plt.ylabel("Number of Accidents") 
plt.tight_layout() 
plt.show() 
#Top 10 Weather Conditions 
df['weather_condition'].value_counts().head(10).plot(kind='bar', 
color='orange') 
plt.title("Bar Chart: Weather Conditions") 
plt.xlabel("Weather") 
plt.ylabel("Count") 
plt.tight_layout() 
plt.show() 
#Primary Cause of Accidents 
cause = df['prim_contributory_cause'].value_counts().head(5) 
plt.pie(cause, labels=cause.index, autopct='%1.1f%%', startangle=90, 
wedgeprops={'width': 0.4}) 
plt.title("Donut Chart: Primary Cause") 
plt.tight_layout() 
plt.show() 
#Injury Severity 
df['most_severe_injury'].value_counts().plot(kind='pie', 
autopct='%1.1f%%') 
plt.title("Pie Chart: Severity of Accidents") 
plt.ylabel("") 
plt.tight_layout() 
plt.show() 
18 
#Vehicles Involved 
df['num_units'].value_counts().sort_index().head(10).plot(kind='bar', 
color='olive') 
plt.title("Bar Chart: Vehicles Involved per Accident") 
plt.xlabel("Vehicles") 
plt.ylabel("Accident Count") 
plt.tight_layout() 
plt.show() 
#Injuries Over Time 
df_grouped = df.groupby('crash_date')['injuries_total'].sum() 
df_grouped.plot(kind='line', color='red') 
plt.title("Line Chart: Injuries Over Time") 
plt.xlabel("Date") 
plt.ylabel("Total Injuries") 
plt.tight_layout() 
plt.show()