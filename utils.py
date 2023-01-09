from datetime import datetime
from dateutil import parser
import os


def prepare_data(data):
    single_data = tuple(data.split('\n'))
    fromdate, todate = list(map(lambda x: parser.parse(x), single_data[0].split('-')))
    reviews = int(single_data[1].removeprefix('Reviews:').strip())
    return fromdate, todate, reviews

def get_file_path():
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True) # ONLY CREATE IF DIR DOESN'T EXISTS
    filename = datetime.now().strftime('%Y%m%d_%H%M%S')
    csv_path = os.path.join(data_dir, filename) # model/filename
    return csv_path

def save_df(df):
    filepath = get_file_path()
    print(f'Filepath :: {filepath}')
    df.to_csv(filepath, index=False)
    return filepath