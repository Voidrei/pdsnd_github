import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Function to get the user input
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington: ").lower()
        if city in (CITY_DATA.keys()):
            break
        else:
            print("input invalid. Please choose from the cities above")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month you Would like to filter by (from January to June) or all: ")
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('input invalid. Please choose from the months above or all')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day you Would like to filter by (from Monday to Sunday) or all: ").lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print('input invalid. Please choose from the days above')

    print()
    print()
    print('-'*40)
    print()
    print()
    return city, month, day

#Loads data for the specified city and filters by month and day
def load_data(city, month, day):

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
    df['month'] = df['Start Time'].dt.strftime('%B')
    cm = df['month'].mode()[0]
    print('The Most Common Month Is:', cm)

    # display the most common day of week
    df['day'] = df['day_of_week']
    cd = df['day'].mode()[0]
    print('The Most Common Day of the Week Is:', cd)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    comm_ss = df['Start Station'].mode()[0]
    print('Commonly used Start Station:', comm_ss)

    # display most commonly used end station
    comm_es = df['End Station'].mode()[0]
    print('Commonly Used End Station:', comm_es)

    # display most frequent combination of start station and end station trip
    df['Req Comb'] = df['Start Station'] + df['End Station']
    req_comb = df['Req Comb'].mode()[0]
    print('Most Frequent Combination Trip:', req_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_tt = df['Trip Duration'].sum()
    print('Total Travel Time:', tot_tt)

    # display mean travel time
    avg_tt = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_tt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if "Gender" in df.columns:
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print('User Types:', user_types)
        print()
        
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print('Gender Count:', gender)
        print()
        
        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]

        print('Earliest:', earliest)
        print('Recent:', recent)
        print('Common:', common)
    else:
        print("Gender column does not exists")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print()
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
    while True:
        fraws = input("Would you like to see 5 more raws? Enter yes or no.\n").lower()
        if fraws in ("yes"):
            print(df.iloc[0:5])
        else:
            break


if __name__ == "__main__":
	main()
