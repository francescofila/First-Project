"""
Bonus 4 — Real-Time Streaming con PySpark

Questo script ascolta la cartella data_local/json/ e aggiorna
il numero totale di transazioni per regione stampando il risultato
in console.
"""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
    TimestampType,
)


def crea_spark_session(app_name="Bonus_Streaming_Modulo2"):
    """
    Crea una SparkSession locale per il bonus streaming.
    """
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark


def main():
    """
    Avvia uno stream JSONL dalla cartella data_local/json, arricchisce
    i record con il nome della regione e stampa in console il numero
    totale di transazioni per regione.
    """
    base_dir = Path("data_local")
    json_dir = str(base_dir / "json")
    regions_path = str(base_dir / "parquet" / "regions.parquet")

    spark = crea_spark_session()

    transactions_schema = StructType([
        StructField("transaction_id", StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("product_id", StringType(), True),
        StructField("region_id", IntegerType(), True),
        StructField("quantity", IntegerType(), True),
        StructField("amount", DoubleType(), True),
        StructField("ts", TimestampType(), True),
        StructField("year", IntegerType(), True),
        StructField("month", IntegerType(), True),
    ])

    regions_df = (
        spark.read.parquet(regions_path)
        .select("region_id", "region_name")
    )

    transactions_stream_df = (
        spark.readStream
        .schema(transactions_schema)
        .json(json_dir)
    )

    transactions_by_region = (
        transactions_stream_df.alias("t")
        .join(regions_df.alias("r"), on="region_id", how="left")
        .groupBy("region_name")
        .agg(F.count("*").alias("total_transactions"))
        .orderBy("region_name")
    )

    query = (
        transactions_by_region.writeStream
        .outputMode("complete")
        .format("console")
        .option("truncate", False)
        .start()
    )

    print("\nStreaming avviato. Premi Ctrl+C per interrompere.\n")
    query.awaitTermination()


if __name__ == "__main__":
    main()