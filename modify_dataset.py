import pandas as pd
import numpy as np

def drop_zero_sales_rows(df):
    df = df.drop(df[df.NumberOfSales == 0].index)
    return df

def drop_closed_store_rows(df):
    df = df.drop(df[df.IsOpen == 0].index)
    return df


def get_fake_test(df):
    return df.loc[((df['D_Month'] == 1) | (df['D_Month'] == 2)) & (df['D_Year'] == 2018)]

def get_fake_train(df):
    return df.loc[((df['D_Month'] != 1) & (df['D_Month'] != 2)) | (df['D_Year'] != 2018)]