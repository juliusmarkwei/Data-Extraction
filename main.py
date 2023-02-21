# import necessary libraries
from pandas import DataFrame
from pandas import read_csv, read_json, read_xml
from glob import glob

# define function to extract data from a CSV file
def extract_from_csv(filename):
    # use pandas to read the CSV file and create a DataFrame object
    dataframe = read_csv(filename)
    return dataframe

# define function to extract data from a JSON file
def extract_from_json(filename):
    # use pandas to read the JSON file and create a DataFrame object
    dataframe = read_json(filename)
    return dataframe

# define function to extract data from an XML file
def extract_from_xml(filename):
    # use pandas to read the XML file and create a DataFrame object
    dataframe = read_xml(filename)
    return dataframe

# define function to extract data from all files in the current directory
def extract_data():
    # create an empty DataFrame object to hold the extracted data
    extracted_data = DataFrame(columns=[1, 2, 3, 4, 5])

    # process all CSV files in the current directory
    for csvfile in glob("*.csv"):
        # use the extract_from_csv function to extract data from each CSV file
        # and append it to the extracted_data DataFrame object
        extracted_data.append(extract_from_csv(csvfile), ignore_index = True)
    
    # process all JSON files in the current directory
    for jsonfile in glob("*.json"):
        # use the extract_from_json function to extract data from each JSON file
        # and append it to the extracted_data DataFrame object
        extracted_data.append(extract_from_json(jsonfile), ignore_index = True)

    # process all XML files in the current directory
    for xmlfile in glob("*.xml"):
        # use the extract_from_xml function to extract data from each XML file
        # and append it to the extracted_data DataFrame object
        extracted_data.append(extract_from_xml(xmlfile), ignore_index = True)

    # return the extracted_data DataFrame object
    return extracted_data

# define function to save a DataFrame object to a CSV file
def load(taget_file, data_to_load):
    data_to_load.to_csv(taget_file)

# extract data from all files in the current directory
data = extract_data()

# save the extracted data to a CSV file named "compiled_data"
load('compiled_data.csv', data)
