import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['Chicago', 'New York City', 'Washington']
months = ['all months','january','february','march','april','may','june']
days = ['all days','saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def get_filters():

  print('\nHello! Let\'s explore some US bikeshare data!\n')
  print('\nHello!,what is your name?\n')
  name = (str(input('\nEnter your name:'))).title()
  print('\nWellcome', name.title(),   'Let\'s explore some US bikeshare data!\n')

  city = ' '
  while city not in CITY_DATA:
        print('\nchoose one of those cities to explore : \n\n chicago  \n new york city \n washington\n')
        city =(input ('\nEnter a city to explore:  ')).lower()

  print(city)
  print('-'*40)

  month = " "
  while month not in months:
        print('\nif you want to filter by month, type one of months: \n\n all months \n january \n february \n march \n april \n may \n june \n')
        month = (input ("\nEnter name of month to explore: ")).lower()
  print(month)
  print('-'*40)

  day = " "
  while day not in days:
        print('\nIf you want to filter by day, Type one of days:\
         \n\n all days \n saturday \n sunday \n monday \n tuesday \n wednesday \n thursday \n friday')
        day = (input ('\njust one step, Select a day in the week: ')).lower()
  print(day)
  print('-'*40)
  print('-'*40)
  print("\n\nYou choose to view City :{}, with Selected Months : {}, and Selected Day : {}".format(city.title(),month.title(),day.title()))

  return city, month, day, name

def load_data(city,month,day,name):

    df = pd.read_csv(CITY_DATA[city.lower()])
   #convert start time table to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['trips'] = 'From:'+ df['Start Station']+'---> To:'+ df['End Station']
    print(df.head())
    print('-'*40)
    if month !='all months':
         df = df[df['month'] == month.title()]
    if day !='all days':
         df = df[df['day_of_week'] == day.title()]

    print(df.head())
    return df

def time_stats(df,city,month,day,name):
     common_month_to_travel = df['month'].mode()[0]
     common_day_to_travel = df['day_of_week'].mode()[0]
     common_hour_to_travel = df['hour'].mode()[0]
     common_start_station = df['Start Station'].mode()[0]
     common_end_station = df['End Station'].mode()[0]
     common_trip = df['trips'].mode()[0]

     message_common = '\n\n{},do you know that , Generally in {}, \n the most common month to travel is :{}.\n while the most common day to travel is :{}.\n and guess what, the most common start hour to travel is : {}!.'
     print(message_common.format(name.title(),city.title(),common_month_to_travel.title(),common_day_to_travel.title(),common_hour_to_travel))
     print('-'*40)
##############################################################
     print('-'*40)
     print('\n For the filtered data : \n')
     print('\nCalculating The Most Frequent Times of Travel...\n')
     start_time = time.time()
     common_month_to_travel_filter = df['month'].mode()[0]
     common_day_to_travel_filter = df['day_of_week'].mode()[0]
     common_start_hour_filter =df['hour'].mode()[0]
     print('-'*40)
     message_fitler = '\n\n{},in {} , for the filtered month of {} :\nThe most common day of the week to travel in the filtered data is :{}.\nThe most common Start hour to travel in the filtered data is : {} !.'
     print(message_fitler.format(name.title(),city.title(),month.title(),common_day_to_travel_filter.title(),str(common_start_hour_filter)))
     print("\nThis calcauation took %s seconds." % (time.time() - start_time))
     print('-'*40)
#######################################################################
def station_stats(df,city,month,day,name):

     print('\nCalculating The Most Popular Stations and Trip...\n')
     start_time = time.time()
     common_start_station_filter = df['Start Station'].mode()[0]
     common_end_station_fitler = df['End Station'].mode()[0]
     common_trip_filter = df['trips'].mode()[0]
     message_Station_fitler = '\n\n{},in {}:\nThe most commonly used Start Station :\
      {}\nThe most commonly used End Station : {}\nThe most frequent combination of start station and end station trip :{}.'
     print(message_Station_fitler.format(name.title(),city.title(),common_start_station_filter.title(),\
     common_end_station_fitler.title(),common_trip_filter.title()))
     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)
######################################################################
def trip_duration_stats(df,city,month,day,name):

     print('\nCalculating Trip Duration...\n')
     start_time = time.time()
     total_travel_time = df['Trip Duration'].sum()
     print("\nThe total travel time from the given fitered data is: " + str(total_travel_time))
     average_travel_time = df['Trip Duration'].mean()
     print("\nThe average travel time from the given fitered data is: " + str(average_travel_time))
     message_travel_filter = '\n\n{},in {}:\nThe total travel Time in hours :\
      {}\nThe average Travel Time in hours : {}.'
     print(message_travel_filter.format(name.title(),city.title(),total_travel_time,average_travel_time))
     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)
##############################################
def user_stats(df,city,month,day,name):

     print('\nCalculating User Stats...\n')
     start_time = time.time()

     counts_user_types = df['User Type'].value_counts()

     print('in {}:\nThe Total Count of all User Types is:\n\n{}'.format(city.title(),str(counts_user_types)))

     if 'Gender' in df.columns and 'Birth Year' in df.columns:
        counts_gender = df['Gender'].value_counts().to_frame()
        print("\nThe Counts of gender is:\n{}".format(str(counts_gender)))
        common_year = df['Birth Year'].mode()[0]
        most_year =  df['Birth Year'].max()
        earlist_year = df['Birth Year'].min()
        print('\nThe most common year of birth is: {}\n'.format(int(most_year)))
        print('\nThe common year of birth is: {}\n'.format(int(common_year)))
        print('\nThe ealiest year of birth is: {}\n'.format(int(earlist_year)))
     else:
        print("\n\n\nthere is no data available for birth years and gender type")


     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)

def raw_data(city):

    df = pd.read_csv(CITY_DATA[city])
    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('\nTo View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
        if display_opt not in ['yes', 'no']:
            print('\nThat\'s invalid choice, pleas type yes or no\n')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break
def main():
    while True:
        city, month, day, name = get_filters()

        df = load_data(city,month,day,name)
        time_stats(df,city,month,day,name)
        station_stats(df,city,month,day,name)
        trip_duration_stats(df,city,month,day,name)
        user_stats(df,city,month,day,name)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
           print('\n\n\nice to have you here, that is my first python code , wish me luck')
           print('-'*40)
           break
if __name__ == "__main__":
    main()
