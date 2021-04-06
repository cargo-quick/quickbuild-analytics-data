#!/usr/bin/env python3.9
# pip3 install pandas
import os
import pandas


def make_runs_parquet():
    original_pwd = os.getcwd()
    os.system("mkdir -p /tmp/quickbuild-data")
    os.chdir("/tmp/quickbuild-data")
    os.system("""
        for page in `seq 1 100`; do
            [[ -s "runs-$page.json" ]] && continue
            curl --fail --verbose \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/alsuren/cargo-quickinstall/actions/runs \
                > runs-$page.json || break
        done
        cat runs-[0-9]*.json | jq .workflow_runs |  jq '.[]' | jq -s > runs-array.json
    """)
    runs = pandas.read_json("./runs-array.json")
    runs['duration'] = runs['updated_at'] - runs['created_at']
    runs['head_commit_message'] = runs['head_commit'].apply(lambda x: x['message'])
    
    runs['duration'] = runs['updated_at'] - runs['created_at']
    processed = runs.loc[(
            runs['head_commit_message'].str.startswith('build ')
        ) & (
            runs.conclusion == 'success'
        )][
            ['head_commit_message', 'created_at', 'updated_at', 'duration']
        ].sort_values('duration')

    # duration can't be encoded to parquet because there is no datatype for it:
    # https://issues.apache.org/jira/browse/ARROW-6780
    processed[['head_commit_message', 'created_at', 'updated_at']].to_parquet("runs.parquet")
    os.system(f"mv 'runs.parquet' '{original_pwd}'")


if __name__ == "__main__":
    make_runs_parquet()
