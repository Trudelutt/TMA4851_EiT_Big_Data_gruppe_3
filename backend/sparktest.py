from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

def get_conf(task_name):
    return SparkConf().setAppName(task_name)

def get_context(conf):
    return SparkContext(conf=conf)

def get_columns(context):
    return context.textFile('data/trade.csv').map(lambda x: x.split(', ')[0])

def get_data(context):
    return context.textFile('data/trade.csv')#.map(lambda x: x.split(','))

spark = SparkSession.builder.appName('Trades').getOrCreate()
df = spark.read.csv('data/trade.csv', mode="DROPMALFORMED",inferSchema=True, header = True)

trade_matrix = df.drop('Reporter Country Code', 'Partner Country Code', 'Item Code', 'Element Code',\
 'Y1986F','Y1987F','Y1988F','Y1989F','Y1990F','Y1991F', 'Y1992F','Y1993F','Y1994F','Y1995F','Y1996F','Y1997F',\
 'Y1998F','Y1999F','Y2000F','Y2001F','Y2002F','Y2003F','Y2004F','Y2005F','Y2006F','Y2007F','Y2008F','Y2009F',\
 'Y2010F','Y2011F','Y2012F','Y2013F' )

trade_matrix.select(trade_matrix['Item'], trade_matrix['Element'], trade_matrix['Unit'], trade_matrix['Y2013'] )\
    .filter(trade_matrix['Element']=='Import Quantity').filter(trade_matrix['Y2013'].isNotNull())\
    .groupby(trade_matrix['Item']).sum().show()

    #.agg({trade_matrix['Y2013']: 'sum'}).collect()[0].show()


#print(str(float(max_imported)))
#.agg({'Y2013':'sum'}).collect()[0]
#df2 = sqlContext.sql("SELECT `Reporter Country` AS Reporter, `Partner Country` AS Partner, Item, Element, \
#Y1986, Y1987, Y1988, Y1989, Y1990, Y1991, Y1992, Y1993, Y1994, Y1995, Y1996, Y1997, Y1998, Y1999, Y2000, Y2001, Y2002, \
#Y2003, Y2004, Y2005, Y2006, Y2007,Y2008, Y2009, Y2010, Y2011, Y2012, Y2013 From myTable")

#conf = get_conf('Trades')
#sc = get_context(conf)

#data = get_data(sc)
#columns = get_columns(sc)

#data = sc.textFile('path_to_data')
#header = data.first() #extract header
#data = data.filter(row => row != header)
#df_with_removed_columns.write.format("com.databricks.spark.csv").save('data/trade_removed_colums.csv')

#filtered_no_null_df = df_with_removed_columns.filter("Y1986 is not NULL OR Y1987 is not NULL OR Y1988 is not NULL OR Y1989 is not NULL OR Y1990 is not NULL OR Y1991 is not NULL OR Y1992 is not NULL OR Y1993 is not NULL OR Y1994 is not NULL OR Y1995 is not NULL \
#OR Y1996 is not NULL OR Y1997 is not NULL OR Y1998 is not NULL OR Y1999 is not NULL OR Y2000 is not NULL OR Y2001 is not NULL OR Y2002 is not NULL OR Y2003 is not NULL OR Y2004 is not NULL OR Y2005 is not NULL OR Y2006 is not NULL \
#OR Y2007 is not NULL OR Y2008 is not NULL OR Y2009 is not NULL OR Y2010 is not NULL OR Y2011 is not NULL OR Y2012 is not NULL OR Y2013 is not NULL")

#df_with_removed_columns.repartition(1).write.format("com.databricks.spark.csv").option('header', 'true').save('data/trade_removed_colums.csv')

#print(filtered_no_null_df.show(4))