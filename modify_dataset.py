import pandas as pd
import numpy as np

def drop_zero_sales_rows(df):
    df = df.drop(df[df.NumberOfSales == 0].index)
    return df

def drop_closed_store_rows(df):
    df = df.drop(df[df.IsOpen == 0].index)
    return df

# Testing on January and February 2018 
def get_fake_test(df):
    return df.loc[((df['D_Month'] == 1) | (df['D_Month'] == 2)) & (df['D_Year'] == 2018)]

def get_fake_train(df):
    return df.loc[((df['D_Month'] != 1) & (df['D_Month'] != 2)) | (df['D_Year'] != 2018)]

# Testing on March and April 2017 instead
def get_fake_test2(df):
    return df.loc[((df['D_Month'] == 3) | (df['D_Month'] == 4)) & (df['D_Year'] == 2017)]

def get_fake_train2(df):
    return df.loc[((df['D_Month'] != 3) & (df['D_Month'] != 4)) | (df['D_Year'] != 2017)]

# Testing on March and April 2016 instead
def get_fake_test3(df):
    return df.loc[((df['D_Month'] == 3) | (df['D_Month'] == 4)) & (df['D_Year'] == 2016)]

def get_fake_train3(df):
    return df.loc[((df['D_Month'] != 3) & (df['D_Month'] != 4)) | (df['D_Year'] != 2016)]

# Testing on January and February 2017 instead
def get_fake_test4(df):
    return df.loc[((df['D_Month'] == 1) | (df['D_Month'] == 2)) & (df['D_Year'] == 2017)]

def get_fake_train4(df):
    return df.loc[((df['D_Month'] != 1) & (df['D_Month'] != 2)) | (df['D_Year'] != 2017)]

# Testing on April and May 2017 instead
def get_fake_test5(df):
    return df.loc[((df['D_Month'] == 4) | (df['D_Month'] == 5)) & (df['D_Year'] == 2017)]

def get_fake_train5(df):
    return df.loc[((df['D_Month'] != 4) & (df['D_Month'] != 5)) | (df['D_Year'] != 2017)]