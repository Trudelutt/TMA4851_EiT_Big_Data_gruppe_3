from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import pyspark.sql.functions as func

def get_conf(task_name):
    return SparkConf().setAppName(task_name)

def get_context(conf):
    return SparkContext(conf=conf)

spark = SparkSession.builder.appName('Trades').getOrCreate()
df = spark.read.csv('data/trade.csv', mode="DROPMALFORMED",inferSchema=True, header = True)

trade_matrix = df.drop('Y1986F','Y1987F','Y1988F','Y1989F','Y1990F','Y1991F', 'Y1992F','Y1993F','Y1994F','Y1995F','Y1996F','Y1997F',\
 'Y1998F','Y1999F','Y2000F','Y2001F','Y2002F','Y2003F','Y2004F','Y2005F','Y2006F','Y2007F','Y2008F','Y2009F',\
 'Y2010F','Y2011F','Y2012F','Y2013F')

trade_matrix = trade_matrix.filter(trade_matrix["Element"]=="Import Quantity")\
    .filter(trade_matrix["Element"]=="Import Quantity")\
    .filter(trade_matrix["Reporter Countries"]!='China')\
    .filter(trade_matrix["Partner Countries"]!='China')\
    .filter(trade_matrix["Partner Countries"]!='Unspecified Area')\
    .filter(trade_matrix["Reporter Countries"]!='Unspecified Area')\
    .coalesce(1).write.format('csv').save('./data/tradematrix_formatted2.csv')