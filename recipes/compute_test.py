# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
orders_2 = dataiku.Dataset("orders_2")
orders_2_df = orders_2.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

orders_2_df['total'] = orders_2_df['tshirt_price'] * orders_2_df['tshirt_quantity']

orders_2_df['total_benoit'] = orders_2_df['tshirt_price'] * orders_2_df['tshirt_quantity'] * 1000
orders_2_df['total_elo'] = orders_2_df['tshirt_price'] * orders_2_df['tshirt_quantity'] * 100

# update text category description
orders_2_df['tshirt_category'] = orders_2_df['tshirt_category'].str.replace('Wh ', 'White ')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
test_df = orders_2_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
# Dataset processed_data renamed to t_shirt_data by neba.nfonsang on 2024-09-16 20:58:07
processed_dataset = dataiku.Dataset("test")
processed_dataset.write_with_schema(test_df)


# Write recipe outputs
test = dataiku.Dataset("test")
test.write_with_schema(test_df)
