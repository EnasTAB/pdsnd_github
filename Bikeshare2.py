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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        city_num = input("Which city's data would you like to see?\n \
                 Select:\n \
                 1 for Chicago\n \
                 2 for New York City\n \
                 3 for Washington\n")
        
        if(city_num == '1'):
            city = 'chicago'
            break
        elif(city_num == '2'):
            city = 'new york city'
            break
        elif(city_num == '3'):
            city = 'washington'
            break
        else:
            print('Invalid input. Please enter number 1 or 2 or 3\n')


    month_filter = False
    day_filter = False
    both_filter = False
    none_filter = False
    
    while True:
        filter_type = input('What filter would you like to apply? month, day, both, none\n')
        filter_type = filter_type.lower()
        if(filter_type == 'month'):
            month_filter = True
            break
        elif(filter_type == 'day'):
            day_filter = True
            break
        elif(filter_type == 'both'):
            both_filter = True
            break
        elif(filter_type == 'none'):
            none_filter = True
            break
        else:
            print('Invalid input. Enter month or day or both (all lowercase)')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'all'
    if(month_filter==True or both_filter==True):
        
        while True:
            month_raw = input('Which month data would you like to see?\nSelect one month from: All, Jan, Feb, Mar, Apr, May, Jun\n')
            month_raw = month_raw.lower()
            if(month_raw == 'jan'):
                month = 'january'
                break
            elif(month_raw == 'all'):
                month = 'all'
                break
            elif(month_raw == 'feb'):
                month = 'february'
                break
            elif(month_raw == 'mar'):
                month = 'march'
                break
            elif(month_raw == 'apr'):
                month = 'april'
                break
            elif(month_raw == 'may'):
                month = 'may'
                break
            elif(month_raw == 'jun'):
                month = 'june'
                break
            else:
                print('Invalid input. Please enter the word among listed below(Case insensitive):')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'
    if(day_filter==True or both_filter==True):
        
        while True:
            day_raw = input('Which day data would you like to see?\nSelect one day from: All, Mon, Tue, Wed, Thu, Fri, Sat, Sun\n')
            day_raw = day_raw.lower()
            if(day_raw == 'all'):
                day = 'all'
                break
            elif(day_raw == 'mon'):
                day = 'Monday'
                break
            elif(day_raw == 'tue'):
                day = 'Tuesday'
                break
            elif(day_raw == 'wed'):
                day = 'Wednesday'
                break
            elif(day_raw == 'thu'):
                day = 'Thursday'
                break
            elif(day_raw == 'fri'):
                day = 'Friday'
                break
            elif(day_raw == 'sat'):
                day = 'Saturday'
                break
            elif(day_raw == 'sun'):
                day = 'Sunday'
                break
            else:
                print('Invalid input. Please enter the exact word among listed below:')

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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if (month != 'all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['month'].mode()[0]
    print('Most popular month is : '+ str(months[popular_month-1]))
    

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day is : '+ str(popular_day))
    


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour is : '+ str(popular_hour))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is : '+ str(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station is : '+ str(common_end_station))



    # TO DO: display most frequent combination of start station and end station trip
    most_freq_trip = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print('Most frequent trip is from '+str(most_freq_trip.index[0][0])+' to '+most_freq_trip.index[0][1])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total travel time is: '+str(total_duration)+' seconds')


    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Mean travel time is: '+str(mean_duration)+' seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of the user:')
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    if(city != 'washington'):    
        print('\nCounts of the gender:')
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Gender information not available for Washington city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if(city != 'washington'):
        
        df['Birth Year'] = pd.to_numeric(df['Birth Year'])
        earliest_dob = df['Birth Year'].min()
        recent_dob = df['Birth Year'].max()
        popular_dob = df['Birth Year'].mode()[0]
    
        print('Earliest year of birth is: '+str(earliest_dob))
        print('Most recent year of birth is: '+str(recent_dob))
        print('Most common year of birth is: '+str(popular_dob))
    else:
        print('Birth year information not available for Washington city.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

pd.set_option('display.max_columns',None)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        df_raw = load_data(city,'all','all')
        df_raw = df_raw.drop(['hour','day_of_week','month'],axis=1)
        i=0
        while True:
            view_data = input('\n Would you like to view rows of the data? yes or no\n')
            if(view_data=='yes'):
                print(df_raw[i:i+5])
                i = i+5
            elif(view_data == 'no'):
                break
            else:
                print('Invalid input.')
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
