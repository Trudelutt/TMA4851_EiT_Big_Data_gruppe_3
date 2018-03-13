'''import csv
import numpy as np

country_col = 1;
element_col = 4; # column with
element_code_food_supply_quantity = 645; # total kg/capita/day
element_code_food_supply_kg = 664; # kcal/capital/day
element_code_protein = 647; #
element_code_fat = 284; #
'''

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pyspark.sql.functions as func

def get_conf(task_name):
    return SparkConf().setAppName(task_name)

def get_context(conf):
    return SparkContext(conf=conf)



spark = SparkSession.builder.appName('Hello').getOrCreate()
df = spark.read.csv('data/FoodBalanceSheets_E_All_Data.csv', mode="DROPMALFORMED",inferSchema=True, header = True)

matrix = df.drop('Area Code', 'Item Code', 'Element Code','Unit',\
 'Y1961F','Y1962F','Y1963F','Y1964F','Y1965F','Y1966F', 'Y1967F','Y1968F','Y1969F','Y1970F','Y1971F','Y1972F',\
 'Y1973F','Y1974F','Y1975F','Y1976F','Y1977F','Y1978F', 'Y1979F','Y1980F','Y1981F','Y1982F','Y1983F','Y1984F',\
 'Y1985F',\
 'Y1986F','Y1987F','Y1988F','Y1989F','Y1990F','Y1991F', 'Y1992F','Y1993F','Y1994F','Y1995F','Y1996F','Y1997F',\
 'Y1998F','Y1999F','Y2000F','Y2001F','Y2002F','Y2003F','Y2004F','Y2005F','Y2006F','Y2007F','Y2008F','Y2009F',\
 'Y2010F','Y2011F','Y2012F','Y2013F' )


#Find relevant data for protein
matrix.select(matrix['Area'], matrix['Item'],matrix['Element'],\
    matrix['Y1961'],matrix['Y1971'],matrix['Y1981'],matrix['Y1991'],matrix['Y2001'],matrix['Y2011']  )\
    .filter(matrix['Element']=='Protein supply quantity (g/capita/day)')\
    .filter(matrix['Element']=='Protein supply quantity (g/capita/day)')\
    .filter((matrix['Area']!='World')).filter((matrix['Area']!='Southern Africa'))\
    .filter((matrix['Area']!='Africa')).filter((matrix['Area']!='Western Africa'))\
    .filter((matrix['Area']!='Middle Africa')).filter((matrix['Area']!='Northern Africa'))\
    .filter((matrix['Area']!='Americas')).filter((matrix['Area']!='Northern America'))\
    .filter((matrix['Area']!='Central America')).filter((matrix['Area']!='Caribbean'))\
    .filter((matrix['Area']!='Asia')).filter((matrix['Area']!='Central Asia'))\
    .filter((matrix['Area']!='Southern Asia')).filter((matrix['Area']!='South-Eastern Asia'))\
    .filter((matrix['Area']!='Western Asia')).filter((matrix['Area']!='Europe'))\
    .filter((matrix['Area']!='Eastern Europe')).filter((matrix['Area']!='Northern Europe'))\
    .filter((matrix['Area']!='Southern Europe')).filter((matrix['Area']!='Western Europe'))\
    .filter((matrix['Area']!='Oceania')).filter((matrix['Area']!='Australia & New Zeland'))\
    .filter((matrix['Area']!='European Union')).filter((matrix['Area']!='Least Developed Countries'))\
    .filter((matrix['Area']!='Eastern Africa')).filter((matrix['Area']!='Net Food Importing Devevloping Countries'))\
    .filter((matrix['Area']!='Land Locked Developing Countries')).filter((matrix['Area']!='Low Income Food Deficit Countries'))\
    .filter((matrix['Area']!='Small Island Developing States')).filter((matrix['Area']!='Net Food Importing Developing Countries'))\
    .filter(matrix['Y1961'].isNotNull())\
    .filter(matrix['Y1971'].isNotNull())\
    .filter(matrix['Y1981'].isNotNull())\
    .filter(matrix['Y1991'].isNotNull())\
    .filter(matrix['Y2001'].isNotNull())\
    .filter(matrix['Y2011'].isNotNull())\
    .coalesce(1).write.format('csv').options(delimiter=',').save('./top30fooditems_2012.csv')


'''
#Find matrix with protein for meat
matrix.select(matrix['Area'], matrix['Item'],matrix['Element'],\
    matrix['Y1961'],matrix['Y1971'],matrix['Y1981'],matrix['Y1991'],matrix['Y2001'],matrix['Y2011']  )\
    .filter(matrix['Element']=='Protein supply quantity (g/capita/day)')\
    .filter((matrix['Area']!='World')).filter((matrix['Area']!='Southern Africa'))\
    .filter((matrix['Area']!='Africa')).filter((matrix['Area']!='Western Africa'))\
    .filter((matrix['Area']!='Middle Africa')).filter((matrix['Area']!='Northern Africa'))\
    .filter((matrix['Area']!='Americas')).filter((matrix['Area']!='Northern America'))\
    .filter((matrix['Area']!='Central America')).filter((matrix['Area']!='Caribbean'))\
    .filter((matrix['Area']!='Asia')).filter((matrix['Area']!='Central Asia'))\
    .filter((matrix['Area']!='Southern Asia')).filter((matrix['Area']!='South-Eastern Asia'))\
    .filter((matrix['Area']!='Western Asia')).filter((matrix['Area']!='Europe'))\
    .filter((matrix['Area']!='Eastern Europe')).filter((matrix['Area']!='Northern Europe'))\
    .filter((matrix['Area']!='Southern Europe')).filter((matrix['Area']!='Western Europe'))\
    .filter((matrix['Area']!='Oceania')).filter((matrix['Area']!='Australia & New Zeland'))\
    .filter((matrix['Area']!='European Union')).filter((matrix['Area']!='Least Developed Countries'))\
    .filter((matrix['Area']!='Eastern Africa')).filter((matrix['Area']!='Net Food Importing Devevloping Countries'))\
    .filter((matrix['Area']!='Land Locked Developing Countries')).filter((matrix['Area']!='Low Income Food Deficit Countries'))\
    .filter((matrix['Area']!='Small Island Developing States')).filter((matrix['Area']!='Net Food Importing Developing Countries'))\
    .filter((matrix['Item']=='Bovine Meat') |  (matrix['Item']=='Mutton & Goat Meat') | (matrix['Item']=='Pigmeat') | (matrix['Item']=='Poultry Meat') |  \
            (matrix['Item']=='Meat') | (matrix['Item']=='Offals') | (matrix['Item']=='Meat, Aquatic Mammals') )\
    .filter(matrix['Y1961'].isNotNull())\
    .filter(matrix['Y1971'].isNotNull())\
    .filter(matrix['Y1981'].isNotNull())\
    .filter(matrix['Y1991'].isNotNull())\
    .filter(matrix['Y2001'].isNotNull())\
    .filter(matrix['Y2011'].isNotNull())\
    .coalesce(1).write.format('csv').options(delimiter=',').save('./top30fooditems_2012.csv')
'''
