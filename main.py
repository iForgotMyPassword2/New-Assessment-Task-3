import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def matplotlib_NSW_Train_patronage():
    df = pd.read_csv("monthly_usage_pattern_train_data-june-2024.csv")
    df = df[df["Trip"] != "Less than 50"]
    df = df[df['MonthYear'] == '2024-06']
    df['Trip'] = df['Trip'].astype(int)
    df = df.groupby("Station", as_index=False)["Trip"].sum()
    filtered_df = df.copy()
    filtered_df = filtered_df.sort_values(by='Trip', ascending=False)
    density_df = pd.read_csv('suburb_density_data.csv')
    density_df = density_df.iloc[:, [0, 1]]
    density_df.columns = ['Station', 'Population_Density']
    filtered_df = pd.merge(filtered_df, density_df, on='Station', how='left')
    
    plt.scatter(filtered_df['Population_Density'], filtered_df['Trip'])
    plt.ylabel('Train Patronage (to nearest million trips/month)')
    plt.xlabel('Estimated Population Density (per sq km)')
    plt.title('Patronage vs Population Density for NSW Stations')

    plt.grid(True)
    plt.show()



def pandas_dataframe_NSW_Train_patronage():
    # Load spreadsheet
    df = pd.read_csv("monthly_usage_pattern_train_data-june-2024.csv")
    df = df[df["Trip"] != "Less than 50"]
    df = df[df['MonthYear'] == '2024-06']
    df['Trip'] = df['Trip'].astype(int)
    df = df.groupby("Station", as_index=False)["Trip"].sum()
    filtered_df = df.copy()
    filtered_df = filtered_df.sort_values(by='Trip', ascending=False)
    density_df = pd.read_csv('suburb_density_data.csv')
    density_df.columns = ['Station', 'Population_Density']
    filtered_df = pd.merge(filtered_df, density_df, on='Station', how='left')
    
    
    Format = input('This dataset is too large for full printout, would you like to see the busiest or least busy stations?' \
    '\n 1. Busiest\n 2. Least Busy\n')
    if Format == '1':
        number_of_stations = int(input('How many of the busiest stations would you like to see? (max 100) '))
        if number_of_stations > 100:
            number_of_stations = 100
        filtered_df = filtered_df.head(number_of_stations)
        print(filtered_df)
    elif Format == '2':
        number_of_stations = int(input('How many of the least busy stations would you like (please note that densities aren\'t available for this)'))
        if number_of_stations > 100:
            number_of_stations = 100    
        filtered_df = filtered_df.tail(number_of_stations)
        print(filtered_df)
        print('\n')
        print('Note: Population density data is not available for some of the least busy stations, likely due to them being in less populated or rural areas.')
        intro()
    else:
        print('Invalid choice, returning to homepage.')
        intro()
    print('\n')
    print('What can you see about the transit ridership in relation to the population density of the suburb?')
    print('Thats right, stations with more transit ridership are usually in suburbs with higher population density.')
    intro()

def intro():
    print('== Homepage ===')
    choice = input(' 1. a) View data as matplotlib graph'
          '\n 2. b) View data as pandas dataframe'
          '\n 3. c) View data as a chart'
          '\n 4. f) Exit')
    
    if choice == '1' or choice.lower() == 'a':
        matplotlib_NSW_Train_patronage()
        print('\n This shows a fresh perspective on how density impacts public transport usage.')
        print('While the effects aren\'t as pronounced as I expected, there is a clear trend that stations in higher density areas have more patronage.')
        press = input('Press enter to return to homepage...')
        intro()
    elif choice == '2' or choice.lower() == 'b':
        pandas_dataframe_NSW_Train_patronage()
    elif choice == '3' or choice.lower() == 'c':
        print('place holder')
    elif choice == '4' or choice.lower() == 'f':
        print('Exiting program...')
        exit()
    else:
        print('Invalid choice, please try again.')
        intro()

print('Thesis Question:"Suburbs with higher density yield better public transport usage"')
input('press enter to continue...')
intro()