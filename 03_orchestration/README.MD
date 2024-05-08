
# Orchestration - Prefect

## <ins>Introduction</ins>

## <ins>Prefect`s Command-line Interface</ins>
Command to interact with Prefect server.
<br />
```
prefect server start
```

Command to initialize a new Prefect project with a specific recipe.
<br>
```
prefect init --recipe git
```

Command for worker creation.
```
prefect work-pool create --type process zoompool
```

Command to start worker.
```
prefect worker start --pool "zoompool"
```

Command for initializing deployment.
```
prefect deploy --all
```
```
prefect deploy 03_orchestration/3.4/orchestrate.py:main_flow --name taxil --pool zoompool
```

Command to run deployment.
```
prefect deployment run 'main-flow/taxil'
```

## <ins>Orchestration with Prefect</ins>
`Flow` - The basis of all Prefect workflow, decorated with a `@flow` decorator.
<br>
`Task` - Represent distinct pieces of work executed within a flow, decorated with a `@task` decorator.

<ins>1. Simple usage</ins>
<br>
Navigate to the directory `3.2` for a basic example. Run the commands `python cat_dog_facts.py` and `python cat_facts.py`. Afterwards, visit the Prefect UI to gain a better understanding of how `Flow` and `Task` function work.

<ins>2. Notebook to script conversion</ins>
<br>
Transform the `duration_prediction.ipynb` notebook into the `orchestrate.py` script. Then, navigate to the `3.3` directory and execute the command `python orchestrate.py`. Visit the Prefect UI again to gain deeper understanding of the workflow. Note that MLflow is utilized in this script.

<ins>3. Flow deployment with GitHub</ins>
<br>
Firstly, execute this command `prefect work-pool create --type process zoompool` to create worker. Ensure GitHub code is up-to-date, begin by running the command `prefect init --recipe git` in parent folder, followed by `prefect deploy 03_orchestration/3.4/orchestrate.py:main_flow --name taxil --pool zoompool`. After completion, execute `prefect deployment run 'main-flow/taxil'` and `prefect worker start --pool 'zoompool'` to initiate the run.

<ins>4. Data Loading from AWS S3</ins>
<br>
- Create S3 Bucket at AWS S3 then upload the NYC data.
- Create user at Identity and Access Management (IAM).
- Assign S3 Full Access Role.
- `Security credentials` -> `Access keys` -> `Other` to create access key.
- Assign `Access key ID` and `Secret access key` to `create_s3_bucket_block.py`.
- Ensure that the bucket name in `create_s3_bucket_block.py` matches the name of the S3 Bucket you've created.

The above steps will establish AWS blocks in the Prefect server. Upon completion, run `create_s3_bucket_block.py` followed by `orchestrate_s3.py`.

```
create_markdown_artifact(
    key = "duration-model-report", markdown = markdown__rmse_report
)
```
The above code snippet generates a report within Prefect Artifacts.

```
s3_bucket_block = S3Bucket.load("s3-bucket")
s3_bucket_block.download_folder_to_path(from_folder = "data", to_folder = "data")
```
The above code snippet retrieves data from AWS S3 and downloads it to a local directory.

```
prefect deploy 03_orchestration/3.5/orchestrate_s3.py:main_flow --name taxil --pool zoompool
```
Execute above code snippet if prefer to deploy two flows under same `--name taxil` `--pool zoompool`.