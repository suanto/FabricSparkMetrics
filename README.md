## Description

This is a Microsoft Fabric Workspace which contains the required items to emit Spark logs and metrics to a Fabric Eventstream. 

## How to use?

1. Clone the repo.
2. Connect to a Fabric Workspace and sync.
3. Get connection string from the eventstream and replace the <PWD> in Spark env (env_emit_metrics).
4. Run the notebook.
5. Run the example queryset (eh_spark_metrics_queryset) to see that everything works.

## Note

As there is no Keyvault in Fabric, the connection string is visible in Spark config. If you commit working Spark env to the repo, connection string will be visible.

## More info

* [Fabric blog - accouncement of the feature](https://blog.fabric.microsoft.com/fi-FI/blog/announcing-the-fabric-apache-spark-diagnostic-emitter-collect-logs-and-metrics/)
* [Fabric blog - how to emit metrics](https://blog.fabric.microsoft.com/en-us/blog/monitor-fabric-spark-applications-using-fabric-real-time-intelligence)
