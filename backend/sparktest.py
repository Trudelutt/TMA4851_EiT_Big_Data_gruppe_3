from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pyspark.sql.functions as func

def get_conf(task_name):
    return SparkConf().setAppName(task_name)

def get_context(conf):
    return SparkContext(conf=conf)

spark = SparkSession.builder.appName('Trades').getOrCreate()
df = spark.read.csv('data/trade.csv', mode="DROPMALFORMED",inferSchema=True, header = True)

trade_matrix = df.drop('Reporter Country Code', 'Partner Country Code', 'Item Code', 'Element Code',\
 'Y1986F','Y1987F','Y1988F','Y1989F','Y1990F','Y1991F', 'Y1992F','Y1993F','Y1994F','Y1995F','Y1996F','Y1997F',\
 'Y1998F','Y1999F','Y2000F','Y2001F','Y2002F','Y2003F','Y2004F','Y2005F','Y2006F','Y2007F','Y2008F','Y2009F',\
 'Y2010F','Y2011F','Y2012F','Y2013F' )

trade_matrix.select(trade_matrix['Item'], trade_matrix['Element'], trade_matrix['Unit'], trade_matrix['Y1999'] )\
    .filter(trade_matrix['Element']=='Import Quantity')\
    .filter(trade_matrix['Y1999'].isNotNull())\
    .groupby(trade_matrix['Item'])\
    .agg(func.sum(trade_matrix['Y1999'])\
        .alias('Total sum of food item'))\
    .orderBy('Total sum of food item', ascending=False)\
    .limit(30).write.format('csv').options(delimiter='\t').save('./data/top30fooditems_1999.csv')
    
    
#csv('./data/top30fooditems_2012.csv')
