# Formatting Texas Projection data

## Data input

The data was retrieved from the [data section](https://demographics.texas.gov/Data/TPEPP/Projections/) of the Texas Demographic Center.

[Link to the full data, careful big!](https://demographics.texas.gov/Resources/TPEPP/Projections/2018/table2/indage/2018allcntyindage.zip)

## Data processing

The data has then been processed with the following steps:

- Dropped all the totals for each age
- Parsed the age into brackets (such that `23` -> `19-24`)
- Grouped by `age`, `area_name` and `year`
