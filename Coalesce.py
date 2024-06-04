def coalesce(*values):
    """
    Reference : https://towardsdatascience.com/4-cute-python-functions-for-working-with-dirty-data-2cf7974280b5
    values : Recive the value you want to treat and the value to be return case if the first value is None.
    
    Return the first non-None value or None if all values are None
    """
    return next((v for v in values if v is not None), None)

print(coalesce(None,'test')) #test
print(coalesce(None,10))      #10
print(coalesce(None,None))    #None
