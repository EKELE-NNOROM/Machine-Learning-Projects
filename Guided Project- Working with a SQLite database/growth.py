import sqlite3
import pandas as pd
import math

conn = sqlite3.connect('factbook.db')
facts = pd.read_sql_query("select * from facts;", conn)
conn.close()

facts = facts.dropna(axis=0)
facts = facts[facts.area_land != 0]

def calc_final_pop(row, starting_year=2015, ending_year=2035):
    pop0 = row['population']
    pop_growth = row['population_growth']
    return pop0 * (math.e ** (pop_growth * (ending_year - starting_year)))

facts["pop_2050"] = facts.apply(calc_final_pop, axis=1)
facts_sorted_2050 = facts.sort_values("pop_2050", ascending=False)
print(facts_sorted_2050[['name', 'pop_2050']].head(10))