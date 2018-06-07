import pandas as pd
import numpy as np

def drop_zero_sales_rows(df):
    df = df.drop(df[df.NumberOfSales == 0].index)
    return df

def drop_closed_store_rows(df):
    df = df.drop(df[df.IsOpen == 0].index)
    return df

# Get a fake test dataframe based on the months and the year to be used as test
def get_fake_test(df, test_months=(1, 2), test_year=2018):
    return df.loc[((df['D_Month'] == test_months[0]) | (df['D_Month'] == test_months[1])) & (df['D_Year'] == test_year)]

# Get a fake train dataframe based on the months and the year to be used as test
def get_fake_train(df, test_months=(1, 2), test_year=2018):
    return df.loc[((df['D_Month'] != test_months[0]) & (df['D_Month'] != test_months[1])) | (df['D_Year'] != test_year)]
