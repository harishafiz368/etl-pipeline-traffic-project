import requests
import pandas as pd

local_authorities_url = "https://roadtraffic.dft.gov.uk/api/local-authorities"

response = requests.get(local_authorities_url)

local_authorities_data = response.json()

local_authorities_list = local_authorities_data

df_local_authorities = pd.DataFrame(local_authorities_list)

unnecessary_columns = ['ita_id', 'ons_code']

df_local_authorities.drop(columns=unnecessary_columns, inplace=True)

"""print(df_local_authorities)"""

url = "https://roadtraffic.dft.gov.uk/api/average-annual-daily-flow"

response = requests.get(url)
data = response.json()

records = data

"""print(type(records))
print(records.keys())"""


if "data" in records:
    records_list = records["data"]

    df = pd.DataFrame(records_list)

else:
    print("The Key 'data' was not found in the API response")

"""unique_years = df['year'].unique()
print("Unique years in the dataset:", unique_years)"""


unnecessary_columns = ['count_point_id', 'start_junction_road_name', 'end_junction_road_name', 'easting', 'northing', 'latitude', 'longitude', 'link_length_km', 'link_length_miles', 'estimation_method',
                       'estimation_method_detailed', 'hgvs_2_rigid_axle', 'hgvs_3_rigid_axle', 'hgvs_4_or_more_rigid_axle', 'hgvs_3_or_4_articulated_axle', 'hgvs_5_articulated_axle', 'hgvs_6_articulated_axle']

df.drop(columns=unnecessary_columns, inplace=True)

"""def filter_data(df, year=None, region_id=None, name=None, road_name=None, road_type=None):

    filtered_df = df.copy()

    if year is not None:
        filtered_df = filtered_df[filtered_df['year'] == year]
    
    if region_id is not None:
        filtered_df = filtered_df[filtered_df['region_id'] == region_id]
    
    if name is not None:
        filtered_df = filtered_df[filtered_df['local_authority_id'].str.contains(road_type, case=False, na=False)]
    
    if road_name is not None:
        filtered_df = filtered_df[filtered_df['road_name'].str.contains(road_name, case=False, na=False)]
    
    if road_type is not None:
        filtered_df = filtered_df[filtered_df['road_type'].str.contains(road_type, case=False, na=False)]

    return filtered_df


filtered_df = filter_data(df, year=2022, region_id=3)
print(filtered_df) 

print(df)"""

df_combined = pd.merge(df, df_local_authorities, left_on='local_authority_id', right_on='id', how='left')

print(df_combined)