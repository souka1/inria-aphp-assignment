import pandas as pd
import numpy as np
from scipy import stats

def help_(frame):
    
    """
    Concatenate 'given_name' and 'surname' columns vertically into one column,
    and take the two most frequent names of that column, 
    and store that names into a column 'name',
    drop the 'given_name' and 'surname' columns
    
    *** this procedure is helpful when some  duplicated entries have given_name is stored in 'surname' column and surname is stored in 'given_name' column
   
    
    """
    concatvalues = frame['surname'].append(frame['given_name']).reset_index(drop=True)
    name=concatvalues.value_counts()[0:2].index.tolist()
    frame['name'] =name[0]+" "+name[1]
    frame=frame.drop(columns=['surname', 'given_name'])
    return frame

def detect_duplicates(frame):
    
    """
    Group the frame by 'phone number',
    and apply count_ function on each group,
    and apply mode function to take the most frequent value 
    of each column.
    reorder the columns of the result
    return a frame without duplicates
    
    """

    df=frame.reset_index(drop=True)
    df=df.groupby('phone_number').apply(help_)
    df=df.groupby('phone_number').agg(lambda x: stats.mode(x)[0]).reset_index() 
    df=df[["patient_id","name","street_number","address_1","suburb","postcode","state","date_of_birth","age","phone_number","address_2","pcr"]]
    
    return df