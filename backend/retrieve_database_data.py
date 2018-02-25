import sqlite3
import json
from sqlite3 import Error

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as error:
        print(e)

    return None

def select_all_partner_countries(connnection):
    current = connection.cursor()
    current.execute("SELECT DISTINCT ´PartnerCountries´ FROM tradematrix")

    rows = current.fetchall
    for row in rows:
        print(row)

def select_all_from_country(connection, reportercountries):
    current = connection.cursor()
    current.execute("SELECT ReporterCountries, PartnerCountries, Item, Unit, Y2000 \
    FROM tradematrix WHERE ReporterCountries=?", (reportercountries,))

    rows = current.fetchall()

    for row in rows:
        print(row)

def select_all_trades_between_two_countries(connection, reportercountries, partnercountries):
    current = connection.cursor()
    current.execute("SELECT ReporterCountries, PartnerCountries, Item, Y2000 FROM tradematrix \
    WHERE Reportercountries=? AND PartnerCountries=?",(reportercountries, partnercountries))

    result = current.fetchall()

    columnTitles = ["countryFrom", "countryTo", "item", "yearValue"]
    decodedStrings = []
    i = 0

    for entries in result:
        dict = {}
        for entry in entries:
            dict[columnTitles[i]] = entry.decode("windows-1252").strip()
            i += 1
        decodedStrings.append(dict)
        i = 0

    json_output = json.dumps(decodedStrings)
    print(json_output)
    
def select_yearly_exports_of_food_from_country(connection, reportercountries, fooditem):
    current = connection.cursor()
    current.execute("SELECT ReporterCountries, PartnerCountries, Item, Unit, Y2000 \
    FROM tradematrix \
    WHERE ReporterCountries=? AND Item=?", (reportercountries, fooditem))

    rows = current.fetchall()

    for row in rows:
        print(row)

def select_all_food_items(connection, one=False):
    current = connection.cursor()
    current.execute("SELECT DISTINCT Item FROM tradematrix")

    #r = [dict((current.description[i][0], value) \
               #for i, value in enumerate(row)) for row in current.fetchall()]
    
    #return (r[0] if r else None) if one else r

    result = current.fetchall()

    decoded_strings = []

    for entries in result:
       for entry in entries:
           decoded_strings.append(entry.decode("windows-1252").strip())

    json_output = json.dumps(decoded_strings)
    print(json_output)

def find_nulls(connection):
    current = connection.cursor()
    current.execute("SELECT * FROM tradematrix \
    WHERE (Y1986 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1986 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1986F IS NULL OR Y1986 == '' OR 0) \
    AND (Y1987 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1987F IS NULL OR Y1986 == '' OR 0) \
    AND (Y1988 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1988F IS NULL OR Y1986 == '' OR 0) \
    AND (Y1989 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1989F IS NULL OR Y1986 == '' OR 0) \
    AND (Y1990 IS NULL OR Y1986 == '' OR 0) \
    AND (Y1990F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2000 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2000F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2001 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2001F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2002 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2002F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2003 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2003F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2004 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2004F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2005 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2005F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2006 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2006F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2007 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2007F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2008 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2008F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2009 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2009F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2010 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2010F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2011 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2011F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2012 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2012F IS NULL OR Y1986 == '' OR 0) \
    AND (Y2013 IS NULL OR Y1986 == '' OR 0) \
    AND (Y2013F IS NULL OR Y1986 == '' OR 0) \
    ") 
    
    result = current.fetchall()
    for row in result:
        print(row)

def main():
    database = "/Users/Sandra/sqlite/faostat.db"
    connection = create_connection(database)
    connection.text_factory = bytes

    with connection:
        print('Querying..')
        #select_all_food_items(connection)
        select_all_trades_between_two_countries(connection, 'Cuba', 'Viet Nam')

if __name__ == '__main__':
    main()