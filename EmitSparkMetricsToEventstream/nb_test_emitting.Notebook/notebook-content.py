# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "environment": {
# META       "environmentId": "b52ce093-49e2-b1d8-484f-150f4474a0e4",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%configure
# MAGIC {
# MAGIC     "name" : "Spark-log-emitting-test",
# MAGIC     "conf" : {
# MAGIC         "spark.app.name" : "spark-logs-emitting-test"
# MAGIC     }
# MAGIC }

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(spark.conf.get('spark.synapse.diagnostic.emitters'))
print(spark.conf.get('spark.synapse.diagnostic.emitter.eventhouse.type'))
print(spark.conf.get('spark.fabric.pools.skipStarterPools'))
print(spark.sparkContext.appName)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.conf.isModifiable("spark.app.id")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Just some dummy action to get Spark doing something

df = (spark.range(1000)
    .select('id')
)
df.count()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
