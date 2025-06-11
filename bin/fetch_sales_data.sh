#!/bin/sh
# Download Warehouse and Retail Sales CSV to data
curl -L "https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.csv?accessType=DOWNLOAD" -o ./data/Warehouse_and_Retail_Sales.csv
