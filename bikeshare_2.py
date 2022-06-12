import time
import pandas as pd
import numpy as np
import datetime as dt

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
        city = input('Please enter city name: ').lower()
        if city=='chicago' or city=='new york city' or city=='washington':
            break
        else:
            print('Please enter a valid city name: ')


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter the month: ').lower()
        if month in ['all','january','february','march','april','may','june','july','august','september','october','november','december']:
            break
        else:
            print('Please enter a valid month: ')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter the day of the week: ').lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('Please enter a valid day: ')


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
    #read the file
    bike_data = pd.read_csv(city.replace(" ", "_")+'.csv')

    #convert user entry to month number and day of the week number
    if month != 'all':
        datetime_object = dt.datetime.strptime(month, "%B")
        m = datetime_object.month

    if day != 'all':
        d = time.strptime(day, "%A").tm_wday

    bike_data['Start Time'] = pd.to_datetime(bike_data['Start Time'], format='%Y-%m-%d')

    if month != 'all' and day != 'all':

        df = bike_data.loc[(bike_data['Start Time'].dt.month == m) & (bike_data['Start Time'].dt.dayofweek == d)]

    if month == 'all' and day !='all':

        df = bike_data.loc[(bike_data['Start Time'].dt.dayofweek == d)]

    if month != 'all' and day == 'all':

         df = bike_data.loc[(bike_data['Start Time'].dt.month == m)]

    if month == 'all' and day == 'all':

         df = bike_data

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    print('Most common month in number: ', df['Start Time'].dt.month.value_counts().index[0],'\n')


    # display the most common day of week

    print('Most common day in number (0=monday): ', df['Start Time'].dt.dayofweek.value_counts().index[0] , '\n')

    # display the most common start hour

    print('Most common start hour: ', df['Start Time'].dt.hour.value_counts().index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    print('Most common start station: ', df['Start Station'].value_counts().index[0], '\n')


    # display most commonly used end station

    print('Most common end station: ', df['End Station'].value_counts().index[0], '\n')


    # display most frequent combination of start station and end station trip

    print('Most common start-end station trip: ', df.groupby(['Start Station','End Station']).size().idxmax(), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print('Total travel time:\n' ,df['Trip Duration'])


    # display mean travel time

    print('Mean travel time: ' ,df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('Counts of each user type:\n',df['User Type'].value_counts())


    # Display counts of gender

    try:
        print('counts of gender: ' ,df['Gender'].value_counts())
    except:
        print('in washington table there is no gender column')


    # Display earliest, most recent, and most common year of birth

    try:
        print('earliest birth date:\n' , df['Birth Year'].min())
        print('most recent birth date:\n', df['Birth Year'].max())
        print('most common birth date:\n',df['Birth Year'].value_counts().index[0])
    except:
        print('washington has no birth year column\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_data(df):
    answer = input('would you like to see first 5 rows of data: ')
    start_loc = 0
    while True:
        if answer.lower() == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
            answer = input('would you like to see 5 more rows of data: ')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
