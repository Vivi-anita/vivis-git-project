import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('**Hello!** Let\'s explore some US bikeshare data!')
    
    cities = ("chicago", "new york city", "washington")
    while True:
        city = input("Which city do you want to analize: _Chicago_, _New York City_, or _Washington_:\n").lower()
        if city in cities:
            break 
        else:
            print("Please type one of the following available cities\n")
    
    months = ("all", "january", "february", "march", "april", "may", "june") 
    while True:
        month = input("Which month do you want review: All, January, February, March, April, May, June:\n").lower()
        if month in months:
            break
        else:
            print("Please type **one** of the following avalable months\n") 
   
    days = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    while True:
        day = input("Which day do you want to explore: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n").lower()
        if day in days:
            break
        else:
            print("Please type one of the following days: all, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday\n")        
        print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    print(len(df['month']))
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print(len(df['month']))
        df = df[df['month'] == months.index(month)]

    if day != 'all':   
        df =df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The **Most** Frequent Times of Travel...\n')
    start_time = time.time()
    
    common_month = df['month'].mode()
    print("The most common month is:", common_month)
    
    common_day = df['day_of_week'].mode()
    print("The most common day is:", common_day)
    
    common_hour = df['hour'].mode()
    print("The most common hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The **Most** Popular Stations and Trip...\n')
    start_time = time.time()
    
    used_start_station = df['Start Station'].mode()
    print("The most commonly used start station iS:", used_start_station)
    
    used_end_station = df['End Station'].mode()
    print("The most commonly used end station is:", used_end_station)
    
    Start_End_Stations = (df['Start Station'] + ['End Station']).mode()
    combination_start_end_stations = str(Start_End_Stations)
    print("The most frequent combination of start station and end station trip is:", combination_start_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating _Trip Duration_ ...\n')
    start_time = time.time()
    
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", round(total_travel_time, 2))
    
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", round(mean_travel_time, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User _Stats_ ...\n')
    start_time = time.time()
    
    user_types = df['User Type'].value_counts()
    print("The counts of user types is:\n", user_types)
    
    try:
        gender_count = df['Gender'].value_counts()
        print("The counts of **gender** is:\n", gender_count)
    except:

        print("There is _no_ avalable gender data for Washignton city.\n")

    
    try:
        earliest_YOB = df['Birth Year'].min()
        print("The **earliest** year of birth is:", round(earliest_YOB))

        recent_YOB = df['Birth Year'].max()
        print("The **most** recent year of birth is:", round(recent_YOB))

        most_common_YOB = df['Birth Year'].mode()
        print("The **most** common year of birth is:", round(most_common_YOB))
    except:
        print("There is **no** available birth data for Washington city.\n")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
     """Displays raw data upon user's request."""
     
     top_data = input("Would you like to see the **top 5** data rows? Enter yes or no.\n").lower()
     x = 0
     pd.get_option('display.max_columns', None)
     while True:
        if top_data == 'no':
            break
        elif top_data == 'yes':
            print(df.iloc[x:x+5])
            top_data = input("Would you like to **continue** analizing data? Enter yes or no.\n").lower()
            x += 5
        else:
            top_data = input("**Invalid input.** Please enter 'yes' or 'no' only.\n").lower()
      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to **restart**? Enter yes or no.\n')
        if restart.lower() != 'yes': 
            break

if __name__ == "__main__":
	main()
