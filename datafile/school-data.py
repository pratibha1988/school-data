import os
from csv import DictReader
root_path = os.path.abspath(os.path.dirname(__file__))
# file_location = os.path.join(root_path, '/school_data.csv')


class Reader():

    @staticmethod
    def read_file():
        '''
        read the location and return the dta of the file
        convert the dictReader format file to dictionary to perform operation
        :return:
        '''
        school_dict = {}
        file_location = root_path + '/school_data.csv'
        # file_location = os.path.join(root_path, '/school_data.csv')
        f = open(file_location, 'r', encoding='ISO-8859-1')
        dict_reader = DictReader(f)
        column_names = dict_reader.fieldnames
        for c in column_names:
            school_dict[c] = []
        for row in dict_reader:
            for c in column_names:
                school_dict[c].append(row[c])

        return school_dict
