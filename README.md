# quickbuild-analytics-data

Analytics data for cargo-quickbuild decision making

Data is stored in parquet files, uncompressed, because they are quick to load into analytics tools like roapi and pandas.

If you want to use an sql-style api, roapi seems to work pretty well.

```
pip3 install roapi-http
roapi-http --table deps:subtrees-clean.parquet
```

and then query it by POSTing SQL to the server

```
curl 'localhost:8080/api/sql' -d "select * from deps where package_name = 'rand' and package_version = '0.8.3' limit 10" | jq
```

(or using postman to do the same thing)

Alternatively, you can load the data into your favorite database and go from there.
