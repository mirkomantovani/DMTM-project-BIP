def get_BIP_error(df):
	"""
	Error on the predictions made. It's based on the BIP provided formula.

	:param df: Data frame
	:return: flaot Percentage of error
	"""
	error_evaluation_columns = ['StoreID', 'D_Month', 'IsOpen', 'Region', 'NumberOfSales', '_NumberOfSales']

	# Remove useless columns and select all those required.
	# Implicit check that all the required attributes to compute the error are
	# present.
	df = df[error_evaluation_columns]

	# let's consider only rows for which the store is open
	df = df[df.IsOpen == 1]

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
