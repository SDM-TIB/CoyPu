import pandas as pd
pd.options.display.max_columns=20


df = pd.read_csv('data/202201-icews-events.csv', encoding='utf-8', sep='\t')

print (df.head(10))
print(df.columns)
print(df.shape)
print(len(df['Event Text'].unique().tolist()))
print(df['Event Text'].unique().tolist())
print(df[['CAMEO Code', 'Event Text']].to_csv('data/CAMEOCode_EventText.csv', encoding='utf-8', index=False))
print(df['Source Sectors'].unique())