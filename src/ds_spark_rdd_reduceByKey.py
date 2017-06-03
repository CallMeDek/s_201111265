#coding: utf-8
import pyspark
import os

def doIt():
    print "---------RESULT-----------"
    myRdd = spark.sparkContext\
        .textFile(os.path.join("data", "ds_spark_wiki.txt"))
    res = myRdd\
        .flatMap(lambda x:x.split())\
        .map(lambda x:(x,1))\
        .reduceByKey(lambda x,y: x+y)\
        .map(lambda x:(x[1], x[0]))\
        .sortByKey(False)\
        .take(10)
    #print res.collect()
    for i in res:
        print i

if __name__ == "__main__":
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .getOrCreate()
    doIt()
    spark.stop()