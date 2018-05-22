# Shared features of the dataset

attributes_names = [
    'StoreID',
    'Date',
    'IsHoliday',
    'IsOpen',
    'HasPromotions',
    'StoreType',
    'AssortmentType',
    'NearestCompetitor',
    'NumberOfCustomers',
    'NumberOfSales',
    'Region_AreaKM2',
    'Region',
    'Region_GDP',
    'Region_PopulationK',
    'CloudCover',
    'Events',
    'Max_Dew_PointC',
    'Max_Gust_SpeedKm_h',
    'Max_Humidity',
    'Max_Sea_Level_PressurehPa',
    'Max_TemperatureC',
    'Max_VisibilityKm',
    'Max_Wind_SpeedKm_h',
    'Mean_Dew_PointC',
    'Mean_Humidity',
    'Mean_Sea_Level_PressurehPa',
    'Mean_TemperatureC',
    'Mean_VisibilityKm',
    'Mean_Wind_SpeedKm_h',
    'Min_Dew_PointC',
    'Min_Humidity',
    'Min_Sea_Level_PressurehPa',
    'Min_TemperatureC',
    'Min_VisibilitykM',
    'Precipitationmm',
    'WindDirDegrees',
]

# Categorical attributes names
categorical = [
    'StoreID',
    'Date',
    'IsHoliday',
    'IsOpen',
    'HasPromotions' ,
    'StoreType',
    'AssortmentType',
    'Region',
    'Events'
]

# Numerical attributes identifiers
numerical = list( set(attributes_names).difference(categorical) )
