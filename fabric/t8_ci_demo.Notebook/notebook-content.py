# Fabric notebook source
# METADATA ********************
# META {"kernel_info": {"name": "synapse_pyspark"}}

# MARKDOWN ********************
# # T8 demo: validni nazev bronze tabulky

# CELL ********************
def save_demo_table(df):
    """Ukazka vytvoreni bronze tabulky, bez skutecneho behu notebooku."""
    df.write.saveAsTable("bronze_cestujici")
