import pandas as pd
from boltons.cacheutils import cachedproperty

brackets = [[0, 12], [13, 18], [19, 24], [25, 34], [35, 44], [45, 54],
            [55, 65], [65, 99]]


def compute_age_bracket(age):
    n_age = int(age)
    for br in brackets:
        if n_age <= br[1]:
            return f'{br[0]}-{br[1]}'
    else:
        return '100+'


def parse_raw(raw: pd.DataFrame):
    parsed_df = raw[raw['age_in_yrs_num'] > -1]
    parsed_df = parsed_df.drop(
        'age_in_yrs_char', axis=1).rename(columns={'age_in_yrs_num': 'age'})
    parsed_df['age'] = parsed_df['age'].apply(compute_age_bracket)

    data_to_group = parsed_df.iloc[:, 3:]
    data_to_group['area_name'] = parsed_df['area_name']
    data_to_group['age'] = parsed_df['age']
    data_to_group['year'] = parsed_df['year']

    parsed_df = data_to_group.groupby(['age', 'area_name',
                                       'year']).sum().reset_index()

    return parsed_df


class Projections:
    def __init__(self, url='./data/projections.csv'):
        self.raw_data = pd.read_csv(url)
        self.parsed_data = parse_raw(self.raw_data)

    @cachedproperty
    def state_rows(self):
        return self.parsed_data['area_name'].apply(lambda area: 'Texas' in area
                                                   )

    @cachedproperty
    def county_data(self):
        return self.parsed_data[~self.state_rows]

    def to_csv(self, out='data/parsed_projections.csv'):
        self.parsed_data.to_csv(out, index=False)
