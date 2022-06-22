# #If using colab unhash hashed imports and code
# from google.colab import drive
# drive.mount('/content/drive')

import os
import pandas as pd

FILE_PATH = input("Enter relative or abs file path to csvs you wish to convert to a df without duplicates, if unsure enter '.' : ")

def combine_csv():
    '''Given a file paths returns list of files'''
     # file_list = os.listdir('/content/drive/MyDrive/all_tweets_by_year')
    file_list = (os.listdir(f'{FILE_PATH}'))
    print(file_list)
    return file_list


def read_csvs(file_list):
  '''Given list of files will check if csv and append those into a single df'''
  list_csv = [file for file in file_list if file[-3:] == "csv"]
  print(list_csv)
  frames = []
  for csv in list_csv:
    frames.append(pd.read_csv(f'{FILE_PATH}/{csv}', engine='python', encoding='latin-1'))
    print(f"added csv: {csv}")
  large_df = pd.concat(frames, ignore_index=True)
  return large_df

def drop_duplicates(large_df, name="large"):
    '''Drop duplicates from single df and convert into csv'''
    no_duplicates_df = large_df.drop_duplicates(subset='Text', keep='first')
    return no_duplicates_df.to_csv(f'{name}_df')

def o79_me():
    file_list = combine_csv()
    large_df = read_csvs(file_list)
    no_duplicate_df = drop_duplicates(large_df)
    print("done")
    return no_duplicate_df


if __name__ == "__main__":
    o79_me()
