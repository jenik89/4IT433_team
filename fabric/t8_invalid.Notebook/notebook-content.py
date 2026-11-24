# Fabric notebook source
# CELL ********************
def save_invalid_table(df):
    """Zamerne spatny nazev pro demonstraci CI - neslucovat."""
    df.write.saveAsTable("cestujici")
