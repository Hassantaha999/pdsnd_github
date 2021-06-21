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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("which city do you want to explore? (please choose one from the following cities: chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else: 
            print("invalid input please try again!")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("which month do you want to explore? (all, january, february, ... , june): ").lower()
        if month in ["all", "january", "february", "march", "april", "may", "june"]:
            break
        else: 
            print("invalid input please try again!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("which month do you want to explore? (all, monday, tuesday, ... sunday): ").lower()
        if day in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            break
        else: 
            print("invalid input please try again!")

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_com_mth = df["month"].mode()[0]
    print("the most common month: ", most_com_mth)

    # display the most common day of week
    most_com_dy = df["day_of_week"].mode()[0]
    print("the most common day of week: ", most_com_dy)

    # display the most common start hour
    most_com_st_hr = df["Start Time"].mode()[0]
    print("the most common start hour: ", most_com_st_hr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_st_st = df["Start Station"].mode()[0]
    print("the most commonly used start station: ", most_st_st)

    # display most commonly used end station
    most_en_st = df["End Station"].mode()[0]
    print("the most commonly used end station: ", most_en_st)

    # display most frequent combination of start station and end station trip
    most_st_comb = (df["Start Station"] + " (start station)" + " (AND) " + df["End Station"] + " (end station)").mode()[0]
    print("the most frequent combination of start station and end station trip: ", most_st_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_tr_t = df['Trip Duration'].sum() / 60 # to get the total travel time in minutes
    print("the total travel time: ", round(tot_tr_t, 2), "min", "(in hours: {})".format(round(tot_tr_t/60, 2)))

    # display mean travel time
    me_tr_t = df['Trip Duration'].mean() / 60 # to get the mean travel time in minutes
    print("the mean travel time: ", round(me_tr_t, 2), "min", "(in hours: {})".format(round(me_tr_t/60, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("counts of user types: ", user_types, sep="\n", end="\n\n")

    # Display counts of gender
    if "Gender" in df:
        genders = df['Gender'].value_counts()
        print("counts of gender: ", genders, sep="\n", end="\n\n")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest = df['Birth Year'].min()
        most_rec = df['Birth Year'].max()
        most_comm = df['Birth Year'].mode()[0]
        print("the earliest year of birth: ", int(earliest))
        print("the most recent year of birth: ", int(most_rec))
        print("the most common year of birth: ", int(most_comm))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
            
def raw_data(df):
    """prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes'"""
    raw = input('\nWould you like to diplay 5 lines of raw data? Enter yes or no\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Would you like to see the next 5 raws?')
            if ask.lower() != 'yes':
                break
                
                
               
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Been a pleasure to serve you")
            print("See you next time!")
            break



if __name__ == "__main__":
    main()
