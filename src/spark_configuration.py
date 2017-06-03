import os

def environ_var_config(path):
    os.environ["SPARK_HOME"]=path

def spark_init_config():
    import findspark
    findspark.init(os.environ["SPARK_HOME"])

def spark_create():
    import pyspark
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession.builder\
        .master("local")\
        .appName("myApp")\
        .config(conf=myConf)\
        .getOrCreate()
    return spark
        
def main():
    #mypath = input("insert path>> ")
    mypath ='C:\Users\Code\s-201111265\spark-2.0.0-bin-hadoop2.6'
    environ_var_config(mypath)
    spark_init_config()
    mySpark = spark_create()
    return mySpark
        
if __name__ == "__main__":
    main()