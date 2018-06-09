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
    import pandas as pd
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
        # let's round and cast to int
        df['_NumberOfSales'] = pd.to_numeric(df['_NumberOfSales'].round(), downcast='integer')
        columns_renamings.pop('NumberOfSales')

    df.rename(index=str, inplace=True, columns=columns_renamings)

    return df


def get_BIP_error(df, already_BIP_format=False):
    """
    It's based on the BIP provided formula.
    Given a dataframe with predictions, **NOT yet summed by month** it return the total error
    done on predictions.

    Required attributes in the dataframe:
        ['StoreID', 'D_Month', 'NumberOfSales', '_NumberOfSales']

    :param df: The data frame
    :param already_BIP_format: If the given dataframe is already into the BIP format.
    :return: Dataframe in the submit format.
    """
    import pandas as pd
    import numpy as np

    def get_regions():
        # starting from the train set, get a dataframe which link the stores to their region
        regions = pd.read_csv('./dataset/train.csv')
        regions = regions[['StoreID', 'Region']]
        regions.drop_duplicates(inplace=True)
        return regions

    # BIP provided code
    def BIP_error(result, regions):
        def regional_error(v):
            y_true = v["Target"]
            y_pred = v["NumberOfSales"]
            return np.sum(np.abs(y_true - y_pred)) / np.sum(y_true)

        def global_error(region_sums):
            return np.mean(region_sums)

        score = global_error(
            pd.merge(result, regions, on="StoreID")[["Region", "Target", "NumberOfSales"]].groupby("Region").apply(
                regional_error))
        return score

    required_attributes = ['StoreID', 'D_Month', 'NumberOfSales', '_NumberOfSales']

    # create a copy of the dataframe to do not change the provided one
    df = df.copy()

    if already_BIP_format:
        result = df[['StoreID','Month', 'Target', 'NumberOfSales']]
    else:
        # Remove useless columns and select all the ones required.
        # Implicit check that all the required columns are present.
        df = df[required_attributes]
        result = apply_BIP_submission_format(df)

    regions = get_regions()

    BIP_total_error = BIP_error(result, regions)
    print("BIP total error: {}".format(BIP_total_error))

    return BIP_total_error
