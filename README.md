# quickbuild-analytics-data

Analytics data for cargo-quickbuild decision making

Data is stored in parquet files, uncompressed, because they are quick to load into analytics tools like roapi and pandas.

## SQL

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

## Pandas

If you want to use pandas + plotly to analyse the data, you can use the jupyter notebooks in the [notebooks](./notebooks) directory.

### To get started:

- Install `poetry` using [the instructions on their website](https://python-poetry.org/docs/#installation).
- Run `poetry install` to fetch some dependencies (jupyter, pandas and plotly).
- Run `poetry run which python`, and copy the result.
- Run `code .` to start vscode in the root of this repo.
- Click View -> Command Pallette (cmd+shift+p) and type `Python: Select Interpreter`
- Click Enter interpreter path...
- Paste the thing that you copied above.
- Open [an existing notebook](./notebooks/downloads-only.ipynb) or create your own.
- You may need to install a few extensions/restart vscode a few times at this point.
- Use Shift+Enter to execute each cell in the notebook.
- You should have an interactive graph in the bottom cell.

### To contribute:

- We use `nbstripout` to strip jupyter notebook cell output when committing to git and diffing.
  - Run `poetry run nbstripout --install --attributes .gitattributes` to get that working if it's not already enabled on your system.
- We use `git-lfs` to store large .parquet and .csv files.
  - Run `brew install git-lfs` or follow the instructions on [their website](https://git-lfs.github.com/) if it's not already enabled on your system.
- You may need the crates.io [database dumps](https://crates.io/data-access) running in a local postgresql server in order to run some cells. These are huge, and take a while to load into postgresql. There is probably a way to use the data dumps without postgresql. Please send a patch if you can think of a better way to do this.
