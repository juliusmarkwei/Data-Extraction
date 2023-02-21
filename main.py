from pandas import DataFrame
from pandas import read_csv, read_json, read_xml
from glob import glob


def extract_from_csv(filename):
    dataframe = read_csv(filename)
    return dataframe

def extract_from_json(filename):
    dataframe = read_json(filename)
    return dataframe

def extract_from_xml(filename):
    dataframe = read_xml(filename)
    return dataframe

def extract_data():
    # create an empty data frame to hold expected data
    extracted_data = DataFrame(columns=[1, 2, 3, 4, 5])

    # process all csv files
    for csvfile in glob("*.csv"):
        extracted_data.append(extract_from_csv(csvfile), ignore_index = True)
    
    # process all json files
    for jsonfile in glob("*.json"):
        extracted_data.append(extract_from_json(jsonfile), ignore_index = True)

    for xmlfile in glob("*.xml"):
        extracted_data.append(extract_from_xml(xmlfile), ignore_index = True)

    return extracted_data

def load(taget_file, data_to_load):
    data_to_load.to_csv(taget_file)

data = extract_data()
load('compiled_data', data)
