import csv,itertools,time
from collections import defaultdict

import os
from datafile.school_data import Reader
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
# app_ROOT = os.path.abspath(os.path.dirname(__file__))
# File_location = os.path.join(app_ROOT, '../datafile/school_data.csv')
file_location = '/Users/pratibhapatro/Desktop/school/data_file/school_data.csv'
index_column = "SCHNAM05"
city_column  = "LCITY05"
state_column = "LSTATE05"
metro_centric_locale_column = "MLOCALE"

def print_counts():

    schoolData = Reader().read_file()
    s = school(schoolData)
    count_all = s._count_all()
    total_count = count_all[0]
    count_by_state = count_all[1]
    count_by_city = count_all[2]
    count_by_metro_locale = count_all[3]

    print("The total number of school is {}".format(total_count))
    print("The total number of school by state is {}".format(dict(count_by_state)))
    # print("the total number of schools per city is {}".format(dict(count_by_city)))
    print("Unique cities have at least one school is {}".format(len(count_by_city)))
    print("The total number of school per metro centric locale {}".format(dict(count_by_metro_locale)))
    print("The city having highest number of schools is {} and the total number of schools is {}".format(count_by_city[0][0], count_by_city[0][1]))



class school:
    def __init__(self, datafile):
        self.datafile = datafile

    def _count_all(self):

        index_values = self.datafile[index_column]
        state_values = self.datafile[state_column]
        city_values = self.datafile[city_column]
        metro_centric_locale_values = self.datafile[metro_centric_locale_column]
        total_count = self.total_count(index_values)
        state_count = self.count_by_state(state_values)
        city_count = self.count_by_city(city_values)
        metro_centric_locale_count = self.count_by_metro_centric_locale(metro_centric_locale_values)
        return total_count, state_count, city_count, metro_centric_locale_count

    def total_count(self, data_file):
        '''

        :param file_name:
        :return: return the total count
        it will return total count to filelines-1 as first line is header
        '''
        school_dict = {}
        for l in data_file:
            if l not in school_dict:
                school_dict[l]=1

        return (len(school_dict))
    
    def count_by_state(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to state
        '''
        state_dict= defaultdict(int)
        for state in data_file:
            state_dict[state] += 1
        return state_dict

    def count_by_city(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to city,length of total city having schools
        '''

        city_dict = defaultdict(int)

        for city in data_file:
            city_dict[city] +=1
        city_dict_sort = sorted(city_dict.items(), key=lambda t: t[1], reverse=True)
        return city_dict_sort

    def count_by_metro_centric_locale(self, data_file):
        '''

        :param file_name:
        :return: return the total count of schools according to metro centric locale
        '''
        metro_centric_locale_dict = defaultdict(int)

        for metro_centric_locale in data_file:
            metro_centric_locale_dict[metro_centric_locale] +=1
        return metro_centric_locale_dict

print_counts()
