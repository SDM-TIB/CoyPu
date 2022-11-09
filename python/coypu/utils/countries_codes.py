import pandas as pd
import numpy as np
from pathlib import Path
from coypu.config import *
from os.path import join
from IPython.display import display_pretty

pd.set_option('display.max_columns', 0)

def comprehensive_country_codes():
    pass
    return

def main():
    # wikipedia and dbpedia_link for countries
    df_wiki_db = pd.read_csv(join(DATASET_DIR, 'countries_dbpedia_wikidata.csv'), encoding='utf-8')
    print(df_wiki_db.shape)
    # display_pretty (df_wiki_db.head(5))
    
    # various countries code for different countries
    df_countries_code = pd.read_csv(join(DATASET_DIR, 'country_codes.csv'), encoding='utf-8')
    print(df_countries_code.shape)
    display_pretty(df_countries_code.columns)
    df_countries_code.drop(columns=['UNTERM Spanish Formal','official_name_fr', 'UNTERM French Short', 'UNTERM Russian Formal',\
        'UNTERM Spanish Short', 'UNTERM Chinese Formal', 'UNTERM French Formal', 'UNTERM Russian Short', 'official_name_ar',\
          'UNTERM Arabic Formal', 'UNTERM Chinese Short', 'UNTERM Arabic Short', 'official_name_ru', 'official_name_cn', 'official_name_es'], inplace=True)
    df_countries_code.dropna(subset=['ISO3166-1-Alpha-3'], inplace=True)
    # display_pretty (df_countries_code.head(5))
    
    # Merging dataframes 
    df = df_countries_code.merge(df_wiki_db, how='outer', right_on='Country Code', left_on='ISO3166-1-Alpha-3')
    print(df.columns)
    df.sort_values(by=['ISO3166-1-Alpha-3'], inplace=True)
    display_pretty (df.head(5))
    df = df[['ISO3166-1-Alpha-3', 'ISO3166-1-Alpha-2', 'Country Code', 'Wikidata', 'DBpedia', 'UNTERM English Formal', 'official_name_en', 
             'Geoname ID', 'FIFA', 'Dial', 'MARC', 'is_independent',
            'ISO3166-1-numeric', 'GAUL', 'FIPS', 'WMO', 'ITU',
            'IOC', 'DS', 'Global Code', 'Intermediate Region Code',
            'ISO4217-currency_name', 'Developed / Developing Countries',
            'UNTERM English Short', 'ISO4217-currency_alphabetic_code',
            'Small Island Developing States (SIDS)',
            'ISO4217-currency_numeric_code', 'M49', 'Sub-region Code',
            'Region Code', 'ISO4217-currency_minor_unit',
            'Land Locked Developing Countries (LLDC)', 'Intermediate Region Name',
            'ISO4217-currency_country_name', 'Least Developed Countries (LDC)',
            'Region Name', 'Sub-region Name', 'Global Name', 'Capital', 'Continent',
            'TLD', 'Languages', 'CLDR display name', 'EDGAR']]
    # print(df.dtypes)
    df = df.astype({col:'Int64' for col in df.dtypes.index if df.dtypes[col]=='float64'}, errors='ignore')
    # print(df.dtypes)
    # print (len(df['ISO3166-1-Alpha-3'].unique()))
    df.to_csv(join(DATASET_DIR, 'countries_all_codes_and_wiki_dbp.csv'), index=False)


if __name__ == '__main__':
    main()
    