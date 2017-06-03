#coding: utf-8
import pyspark
def doIt():
    print "---------RESULT-----------"
    print spark.version
    #spark.conf.set("spark.logConf", "false")
    #rdd = spark.sparkContext.pallelize(range(1000), 10)
    #print "mean=", rdd.mean()

if __name__=="__main__":
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
            .master("local")\
            .appName("myApp")\
            .config(conf=myConf)\
            .getOrCreate()
    doIt()
    spark.stop()