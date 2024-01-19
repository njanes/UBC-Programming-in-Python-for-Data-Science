def char_del(data, col: list, remove: list):
    import pandas as pd

    """
    Accepts a dataframe along with a list of columns, and a list of character strings to delete, then 
    returns the same dataframe with the character strings removed from the designated columns.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to format
    col : list
        The column(s) from which to delete character strings
    char : list
        The character(s) to be deleted
        
    Returns
    -------
    pandas.core.frame.DataFrame 
    The data frame with the character strings removed from the designated columns.      
    
    Raises
    ------
    TypeError
        If the data argument is not a pd.DataFrame    
    TypeError
        If the col argument is not a list    
    AssertError
        If the col argument is not in the data columns
    
    Example
    --------
    data = {'math':['85.0%','78.0%','80.0%'],'history':['69.0%','77.0%', '78.0%'],'biology':['88.0%','87.0%','88.0%']}
    pd.DataFrame(data)
    
    >>> char_del(data, ['math','biology'],['%','.0'])
        	'85'	'69.0%'	'88'
        	'78'	'77.0%'	'87'   
        	'80'	'78.0%'	'88'
    """

    # Checks that data is a Pandas data frame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data argument is not type pandas.core.frame.DataFrame")

    # Checks that col argument is a list
    if not isinstance(col, list):
        raise TypeError("col argument must be of type list")

    # Checks that col argument is in data columns
    for n in col:
        assert n in data.columns, "item in col not found in data"

    for n in col:
        for m in remove:
            data[n] = data.apply(lambda x: x[n].replace(m, ""), axis=1)
    return data


def col_div(data, col: str, divisor: int):
    import pandas as pd

    """
    Accepts a dataframe, a column, and an integer, then returns the dataframe with the column divided by the integer and as type int64.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to format
    col : str
        The column to be int64 and divided 
    divisor : int
        The integer to divide columns by 
        
    Returns
    -------
    pandas.core.frame.DataFrame 
    The data frame with the designated column divided by the divisor and as type int64
    
    Raises
    ------
    TypeError
        If the data argument is not a pd.DataFrame    
    TypeError
        If the col argument is not a string    
    ValueError
        If the divisor is not a number
    
    Example
    --------
    data = {'city': ['City1', 'City2', 'City3'],
    'population': [1000000, 1500000, 800000]}
    pd.DataFrame(data)
    
    >>> col_div(data, 'population', 1000)
        	'City1' 	1000.0
        	'City2' 	1500.0  
        	'City3' 	800.0
    """

    # Checks that data is a Pandas data frame
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data argument is not type pandas.core.frame.DataFrame")

    # Checks that col argument is a string
    if not isinstance(col, str):
        raise TypeError("col argument is not a string")

    # Checks that divisor contains only numbers
    try:
        float(divisor)
    except ValueError:
        print("divisor must only contain numbers")

    data[col] = data[col].astype("int64") / divisor
    return data
