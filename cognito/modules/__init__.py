"""
Data checking module
"""
from __future__ import print_function
import os
import sys
import pandas as pd
import numpy as np


class Check():
    """
    Check class helps us to identify the types of
    variables categorical | Continuous | Discrete
    """
    def __ini__(self):
        pass

    @staticmethod
    def is_working(column="Cognito!"):
        """
        Determines whether the specified command is working.
        :param      column:  The column
        :type       column:  string
        """
        return "Hello, %s! How are you %s?"%(column, column)


    @staticmethod
    def is_categorical(column):
        """
        Determines whether the specified col is categorical.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_categorical(data['Age'])
            >> True
        """
        try:
            return bool(True) if column.dtypes == 'object' else bool(False)

        except AttributeError:
            print("Method only supported pandas.cores.series")


    @staticmethod
    def is_continuous(column):
        """
        Determines whether the specified col is continuous.

        :param      col:  column name
        :type       col:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_continuous(data['Age'])
            >> False
        """


    @staticmethod
    def is_discrete(column):
        """
        Determines whether the specified column is discrete.

        :param      column:  column name
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_discrete(data['Age'])
            >> True
        """


    @staticmethod
    def is_identifier(column):
        """
        Determines whether the specified column is identifier.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_identifier(data['Age'])
            >> True

        """


    @staticmethod
    def is_missing(column):
        """
        Determines whether the specified column is having missing.

        :param      column:  The column
        :type       column:  { pandas.series | list | tuple }
        :return     boolean: True | False

        Usage:
        ======
            >> Check.is_missing(data['Price'])
            >> False

        """
        try:
            return bool(True) if column.isnull().values.any() == bool(True) else bool(False)

        except AttributeError:
            print("Method only supported pandas.cores.series")


    @staticmethod
    def percentage_missing(dataframe):
        """
        Calculates the percentage of missing value in each column of dataframe.

        :param       dataframe:  The dataframe
        :type        dataframe:  { pandas.dataframe }
        :return      dictionary:  Dictionary of column name with percentage of missing values

        Usage:
        ======
        >> Check.perc_missing(data)
        >> {Price:0.00, Age:10.00}

        """
        missing = dataframe.isnull().sum()
        row_size = len(dataframe.index)
        missing_dict = {}
        for i in list(dataframe.columns):
            perc = round(missing[i] / row_size * 100.0, 2)
            missing_dict.update({i:perc})
        return missing_dict

    @staticmethod
    def remove_columns(dataframe):
        """
        Removes the column containing 60% or more missing data.

        :param      dataframe:  The dataframe
        :type       dataframe:  { pandas.dataframe }
        :return     dataframe:  Dataframe with the columns dropped

        Usage:
        ======
        >>Check.remove_col(data)
        >>dataframe

        """
        missing_dict = Check.percentage_missing(dataframe)
        for column in missing_dict:
            if missing_dict[column] >= 60.00:
                dataframe.drop([column], axis=1, inplace=True)
        return dataframe

    @staticmethod
    def remove_records(dataframe):
        """
        Removes the rows where if a column has 20 % to 30 % of missing data.

        :param      dataframe:  The dataframe
        :type       dataframe:  { pandas.dataframe }
        :return     dataframe:  Dataframe with the rows dropped

        Usage:
        ======
        >>Check.remove_col(data)
        >>dataframe

        """
        missing_dict = Check.percentage_missing(dataframe)
        for column in missing_dict:
            if missing_dict[column] >= 20.00 and missing_dict[column] < 30.00:
                dataframe = dataframe[dataframe[column].isnull() != bool(True)]
        return dataframe
