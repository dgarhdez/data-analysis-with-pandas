import pandas as pd
from datetime import date

def get_season(date_to_convert: datetime.date):  # the function expects a datetime.date object as input
    
    # fix the year of the input
    date_year = date_to_convert.year
    
    # create the list of tuples on which to loop
    seasons = [
        ("winter", date(date_year, 12, 21), date(date_year, 12, 31)),
        ("spring", date(date_year, 3, 20), date(date_year, 6, 21)),
        ("summer", date(date_year, 6, 22), date(date_year, 9, 21)),
        ("fall", date(date_year, 9, 22), date(date_year, 12, 20)),
        ("winter", date(date_year, 1, 1), date(date_year, 3, 19))
    ]
    
    # loop for each season trying to find the season to which
    # date_to_convert belongs to
    for elem in seasons:  # season = tuple(name, start, end) = (elem[0], elem[1], elem[2])
        if date_to_convert>=elem[1] and date_to_convert<=elem[2]:  
            return elem[0]