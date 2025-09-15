import pandas as pd
import matplotlib

def pandas_dataframe_NSW_Train_patronage():
    # Load spreadsheet
    df = pd.read_csv("monthly_usage_pattern_train_data-june-2024.csv")

    # Keep only 2023–2024 data
    df = df[df['MonthYear'].between('2023-01', '2024-12')].copy()

    # Function to convert Trip categories to numeric midpoints
    def convert_trip_to_number(trip):
        if "Less than 50" in trip:
            return 25
        if "or more" in trip:  # e.g. "1,000,000 or more"
            num = int(trip.split()[0].replace(",", ""))
            return num  # lower bound
        if "–" in trip:
            low, high = trip.split("–")
            low = int(low.replace(",", ""))
            high = int(high.replace(",", ""))
            return (low + high) // 2
        return None

    # Convert Trip column to numeric
    df['Patronage'] = df['Trip'].apply(convert_trip_to_number)

    # Group by station and sum entry + exit across all months
    result = df.groupby('Station')['Patronage'].sum().reset_index()

    # Rename columns
    result.columns = ['Station name', 'Patronage']

    print(result)


def intro():
    print('Thesis Question:"Suburbs with higher density yield better public transport usage"')
    input('press enter to continue...')
    print('== Homepage ===')
    choice = input(' 1. a) View data as matplotlib graph'
          '\n 2. b) View data as pandas dataframe'
          '\n 3. c) View data as a chart'
          '\n 6. f) Exit')
    if choice == '1' or choice.lower() == 'a':
        print('later')

pandas_dataframe_NSW_Train_patronage()
