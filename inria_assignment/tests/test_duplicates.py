
import pandas as pd
from inria_assignment.detect_duplicates import detect_duplicates


data = {
        'patient_id':[158601],
        'name':['robson giuliana'],
        'street_number':[13.0],
        'address_1':['federal highway'],
        'suburb':['dandenong north'],
        'postcode':[2165],
        'state':['qld'],
        'date_of_birth':['19801228.0'],
        'age':[32.0],
        'phone_number':['02 54377445'],
        'address_2':['marungi park'],
        'pcr':['Negative']
        
       }
test_result = pd.DataFrame(data)
df = pd.read_csv("/Users/soukaina/Downloads/inria-aphp-assignment-master/inria_assignment/tests/test_data.csv", index_col = 0)

def test_detect_duplicates():
    
    """
    Test de la fonction detect_duplicates
    """
    
    assert detect_duplicates(df)==test_result
   