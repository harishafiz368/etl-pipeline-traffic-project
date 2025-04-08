# ETL Pipeline Project Details

## Overview
This project is designed to extract data from the UK Department for Transport APIs, transform it by cleaning and merging datasets, and output the final combined data.

## Data Sources
- **Local Authorities API:** Provides a list of local authorities.
- **Average Annual Daily Flow API:** Provides traffic flow data by road segment.

## Process Overview
1. **Extraction:** Data is fetched using the `requests` library.
2. **Transformation:** Dataframes are created using `pandas`, and unnecessary columns are removed.
3. **Merging:** Two dataframes are merged based on their local authority identifiers.
4. **Loading:** The resulting merged dataframe is printed out.

## Future Enhancements
- Parameterize filters for dynamic data queries.
- Add error handling and logging capabilities.
- Export combined data to CSV or a database.
