import pandas as pd

# Read data from the CSV file
csv_file = "/Users/sanshubhkukutla/Documents/projects/PokerBot/poker-now-analyzer/poker_now_log_pglJMTPtFPpicExKgMjCS7nqV copyBaseDataCopy.csv" 
data = pd.read_csv(csv_file)

# Clean the 'order' column by removing non-numeric rows
data['order'] = pd.to_numeric(data['order'], errors='coerce')
data = data.dropna(subset=['order'])

# Convert the 'at' column to datetime format
data['at'] = pd.to_datetime(data['at'])

# Print the cleaned data
print(data)
