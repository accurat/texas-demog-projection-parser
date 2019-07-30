# Formatting Texas Projection data

## Data input

The data was retrieved from the [data section](https://demographics.texas.gov/Data/TPEPP/Projections/) of the Texas Demographic Center.

[Link to the full data, careful big!](https://demographics.texas.gov/Resources/TPEPP/Projections/2018/table2/indage/2018allcntyindage.zip)

## Data processing

The data has then been processed with the following steps:

- Dropped all the totals for each age
- Parsed the age into brackets (such that `23` -> `19-24`)
- Grouped by `age`, `area_name` and `year`

## How to

```bash
curl https://demographics.texas.gov/Resources/TPEPP/Projections/2018/table2/indage/2018allcntyindage.zip -L -o data/projections.zip

# unzip it as data/projections.csv

pip install requirements.txt
python3 main.py
zip -r data/parsed_projections.csv.zip data/parsed_projections.csv
```

And you have your zipped csv.
