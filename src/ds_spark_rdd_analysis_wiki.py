
#coding: utf-8

import os

def configurationAndSetUp(path):
    import sys, findspark, pyspark
    os.environ["SPARK_HOME"] = path
    findspark.init(os.environ["SPARK_HOME"])
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .getOrCreate()
    return spark

def split_line(my_str):
    return my_str.split()

def get_rdd(spark):
    meaningless_list = [u'the', u'and', u'to', u'a', u'in', u'of', u'was', \
                   u'The', u'an', u'on', u'from', u'for', u'by']
    myRdd = spark.sparkContext.textFile(os.path.join('data', 'ds_spark_wiki_main.txt'))
    lines = myRdd.flatMap(split_line).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)\
            .map(lambda x:(x[1],x[0])).sortByKey(False).filter(lambda x: x[1] not in meaningless_list)
    return lines

def draw_graph(rdd):
    import matplotlib.pyplot as plt

    count = map(lambda x: x[0],rdd.take(10))
    word = map(lambda x:x[1], rdd.take(10))
    plt.barh(range(len(count)), count, color='red')
    plt.yticks(range(len(count)), word)
    plt.show()

def main():
    spark = configurationAndSetUp('C:\Users\Code\s-201111265\spark-2.0.0-bin-hadoop2.6')
    myRdd = get_rdd(spark)
    draw_graph(myRdd)

if __name__ == "__main__":
    main()