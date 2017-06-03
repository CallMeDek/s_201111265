#coding: utf-8

def entire_file_count(spark):
    import os
    rdd = spark.sparkContext.textFile(os.path.join('data','ds_spark_wiki_main.txt'))
    lines = rdd.flatMap(lambda x:x.replace(',',' ').replace('.',' ').split())\
            .map(lambda x:(x,1)).reduceByKey(lambda x,y: x+y).map(lambda x:(x[1], x[0]))\
            .sortByKey(False)

    for line in lines.take(5):
        print line
        
def per_line_count(spark):
    wc = spark.sparkContext.textFile("data/ds_spark_wiki_main.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

    for e in wc.collect():
        print e
        
def word_vectore():
    rdd = spark.sparkContext.textFile(os.path.join('data','ds_spark_wiki_main.txt'))\
            .map(lambda x: x.split(" "))
    import pyspark.millib.feature import HashingTF
    hashingTF = HashingTF()
    trans_form = hashingTF.transform(rdd)
    trans_form.collect()
  
def main():
    import os
    import sys 
    os.environ["SPARK_HOME"]='C:\Users\Code\s-201111265\spark-2.0.0-bin-hadoop2.6'
    import findspark, os, sys
    findspark.init(os.environ["SPARK_HOME"])
    import pyspark
    myConf=pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config("spark.sql.warehouse.dir", os.path.join(os.environ['SPARK_HOME'], 'data', 'data_warehouse')).getOrCreate()
    entire_file_count(spark)
    per_line_count(spark)
    
if __name__ == "__main__":
    main()