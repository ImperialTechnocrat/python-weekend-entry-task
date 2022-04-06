import pandas as pd

def reader_csv(file):
    df = pd.read_csv(file)
    return df

def get_graph(file, orig):

    print(orig)
    df = reader_csv(file)
    print(df.loc[df['origin'] == orig])
    

filename = 'example/example0.csv'
get_graph(filename, "WIW")

