import pandas as pd

def clean_data(csv_file):
    data = pd.read_csv(csv_file)

    data['order'] = pd.to_numeric(data['order'], errors='coerce')
    data = data.dropna(subset=['order'])

    data['at'] = pd.to_datetime(data['at'])

    return data

if __name__ == "__main__":
    csv_file = "/Users/sanshubhkukutla/Documents/projects/PokerBot/poker-now-analyzer/poker_now_log_pglJMTPtFPpicExKgMjCS7nqV copyBaseDataCopy.csv"  
    cleaned_data = clean_data(csv_file)

    cleaned_data.to_csv("data/cleaned_data.csv", index=False)
