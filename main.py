import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# set pandas to display all rows and columns despite the size

def matplotlib_NSW_Train_patronage():
    df = pd.read_csv("monthly_usage_pattern_train_data-june-2024.csv") # Load the csv file into a DataFrame
    df = df[df["Trip"] != "Less than 50"] # Remove rows where 'Trip' is 'Less than 50'
    df = df[df['MonthYear'] == '2024-06'] # Filter for June 2024 data
    df['Trip'] = df['Trip'].astype(int) # Convert the 'trip' column into integers
    df = df.groupby("Station", as_index=False)["Trip"].sum() # Sum up entry/exit values for each station
    filtered_df = df.copy() # Create a copy of the DataFrame to work with (just in case)
    filtered_df = filtered_df.sort_values(by='Trip', ascending=False)# Sort the DataFrame by 'Trip' in descending order``
    density_df = pd.read_csv('suburb_density_data.csv')
    density_df.columns = ['Station', 'Population_Density']
    filtered_df = pd.merge(filtered_df, density_df, on='Station', how='left') # Merge the population density data with the train patronage data

    choice = input('Would you like to view the stations with a scatter plot or a line graph? \n 1. Scatter Plot \n 2. Line Graph \n')
    if choice == '2':
        station = filtered_df['Station'].tolist()
        trip = filtered_df['Population_Density'].tolist()
        # creates x and y lists for the bar chart ('tolist()' converts pandas series to regular lists)
        plt.bar(station, trip, color='skyblue') # Create a bar chart
        plt.xlabel('Station Names (organised from busiest to least busy)') # Label x-axis
        plt.ylabel('Population Density (per sq km)') # Label y-axis
        plt.title('Train Patronage for NSW Stations') # Title of the graph
        plt.show() # Display the graph

    elif choice == '1':
        plt.scatter(filtered_df['Population_Density'], filtered_df['Trip'])
        plt.ylabel('Train Patronage (to nearest million trips/month)')
        plt.xlabel('Estimated Population Density (per sq km)')
        plt.title('Patronage vs Population Density for NSW Stations')
        plt.grid(True)
        plt.show()
        # Similar steps as above, but for a scatter plot instead of a bar chart
    else:
        print('Invalid choice, returning to homepage.')
        intro()



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
          '\n 3. c) View data as as full dataframe (only for the bravest...)'
          '\n 4. f) Exit \n')
    
    if choice == '1' or choice.lower() == 'a':
        matplotlib_NSW_Train_patronage()
        print('\n This shows a fresh perspective on how density impacts public transport usage.')
        print('While the effects aren\'t as pronounced as I expected, there is a clear trend that stations in higher density areas have more patronage.')
        input('Press enter to return to homepage...\n')
        intro()
    elif choice == '2' or choice.lower() == 'b':
        pandas_dataframe_NSW_Train_patronage()
    elif choice == '3' or choice.lower() == 'c':
        input('Press enter to view full dataframe (warning: very large output)\n')
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
        print(filtered_df)
        print('\n')
        input('Press enter to return to homepage...\n')
        intro()
        
    elif choice == '4' or choice.lower() == 'f':
        print('Exiting program...')
        exit()
    else:
        print('Invalid choice, please try again.')
        intro()

print('Thesis Question:"Suburbs with higher density yield better public transport usage"')
input('press enter to continue...\n')
intro()