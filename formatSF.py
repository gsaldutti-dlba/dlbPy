import pandas as pd
def formatSF(response):
    """_summary_
    Args:
        response (query dataframe): Cleans salesforce response and format to df
    """
    
    #if ((type(response) == dict)&('records' in response.keys())):
    if type(response) == list:
         # Create a DataFrame from the 'records' list
        df = pd.DataFrame.from_records(response).drop(columns='attributes', errors='ignore')
        
    else if ((type(response) == dict)&('records' in response.keys())):
        # Create a DataFrame from the 'records' list
        df = pd.DataFrame.from_records(response['records']).drop(columns='attributes', errors='ignore')

    else:
        print('Unknown type, check data type')
    # Initialize an empty list to store nested DataFrames
    nested_cols = []

    # Loop over columns with "__r"
    for i in df.columns[df.columns.str.contains("__r")]:
        print(i)
        column = df[i].apply(pd.Series)
        
        # Use a dictionary to map column names and rename them
        rename_dict = {col: i.replace("__r", "") + '_Id' for col in column.columns if col == 'Id'}
        column = column.rename(columns=rename_dict)
       

        # Append the nested DataFrame to the list
        nested_cols.append(column)

    # Concatenate the list of nested DataFrames with the original DataFrame
    df = pd.concat([df] + nested_cols, axis=1)

    # Remove duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Drop the original nested columns
    df = df.drop(columns=df.columns[df.columns.str.contains("__r")])

    return df
