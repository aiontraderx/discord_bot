import pickle
import pandas as pd
pd.set_option('display.max_columns', None, 'display.width', None, 'display.max_rows',None,'display.max_colwidth',None)


file_namex = 'test.pkl'
file_name_csv = 'test.csv'


def read_pickle(file_name):
    with open(file_name, "rb") as f:
        loaded_obj = pickle.load(f)
    print('Pickle')
    return loaded_obj



def read_pickle_df(file_name):
    try:
        df = pd.read_pickle(file_name)
        return df
    except:
        print('File Not Found')


def save_csv(df,file_name,set_index='id'):
    print(type(df))
    df.set_index(set_index,inplace=True)
    df.to_csv(file_name)
    return df

def clean_csv(csvFile):
    df= pd.read_csv(csvFile)
    split_word = df['text'].str.split('https://').str[0] ### Clean Data Text
    split_url = df['text'].str.split('https://').str[1]
    df['text'] = split_word ## item row , text list
    df['url_link'] =split_url
    # save_csv(df)
    return df

# df =read_pickle(file_name=file_namex)
# print(df)
if __name__ == '__main__':
    df= read_pickle(file_namex)
    print(df)
    # df=save_csv(df,file_name_csv)
    # df=clean_csv(file_name_csv)
    # print(df.iloc[[-1]])
