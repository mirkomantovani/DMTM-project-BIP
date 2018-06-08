def get_BIP_error(df):
    """
    Error on the predictions made. It's based on the BIP provided formula.

    :param df: Data frame
    :return: flaot Percentage of error
    """
    error_evaluation_columns = ['StoreID', 'D_Month', 'Region', 'NumberOfSales', '_NumberOfSales']

    # Remove useless columns and select all those required.
    # Implicit check that all the required attributes to compute the error are
    # present.
    df = df[error_evaluation_columns]

    # let's consider only rows for which the store is open
    # df = df[df.IsOpen == 1]  #Not needed anymore since we dropped it

    # let's keep only march and april
    # df = df.loc[df['D_Month'].isin([3, 4])] No. let's just evaluate months provided

    # sum everything keeping distinguished: Month, Store and Region
    df_sum_by_month = df.groupby(['D_Month', 'StoreID', 'Region']).sum()

    # compute the difference between actual and predicted NumberOfSales and do the abs
    df_sum_by_month['abs_diff'] = df_sum_by_month. \
        apply(lambda x: abs(x['NumberOfSales'] - x['_NumberOfSales']), axis=1)

    # Let's sum over the region
    df_sums_by_region = df_sum_by_month.groupby(['Region']).sum()

    # Divide the difference between actual and predicted NumberOfSales by the sum of actual
    df_sums_by_region['E_r'] = \
        df_sums_by_region['abs_diff'] / df_sums_by_region['NumberOfSales']

    df_sums_by_region.head(20)

    # Get the number of regions
    N_regions = len(df.Region.unique())

    print("Number of regions identified: {}".format(N_regions))

    BIP_total_error = df_sums_by_region['E_r'].sum() / N_regions

    print("BIP total error: {}".format(BIP_total_error))

    return BIP_total_error


def apply_BIP_submission_format(df, real_submit=False):
    """
    Given a dataframe with predictions, **NOT yet summed by month** it returns a dataframe which
    format is exactly the one required for the submission.

    If real_submit is set to False (default), the function will require (and also include in the
    outputted dataframe) the value of the *true* NumberOfSale.

    Required attributes (real_submit=False):
        ['StoreID', 'D_Month', 'NumberOfSales', '_NumberOfSales']

    Required attributes (real_submit=True):
        ['StoreID', 'D_Month', '_NumberOfSales']


    :param df: The data frame
    :param real_submit: Whether the dataframe returned is for the real submit or not.
    :return: Dataframe in the submit format.
    """
    submission_features = ['StoreID', 'D_Month', 'NumberOfSales', '_NumberOfSales']

    if real_submit:
        submission_features.remove('NumberOfSales')

    # create a copy of the dataframe to do not change the provided one
    df = df.copy()

    # Remove useless columns and select all the ones required.
    # Implicit check that all the required columns are present.
    df = df[submission_features]

    # sum _NumberOfSales (and NumberOfSales) by the store and month
    df = df.groupby(['StoreID', 'D_Month']).sum()

    df.reset_index(inplace=True)

    # name conversion from our standard to BIP submission standard
    columns_renamings = {
        'D_Month': 'Month',
        'NumberOfSales': 'Target',
        '_NumberOfSales': 'NumberOfSales'
    }
    # remove NumberOfSales renaming in case of real_submit
    if real_submit:
        columns_renamings.pop('NumberOfSales')

    df.rename(index=str, inplace=True, columns=columns_renamings)

    return df
