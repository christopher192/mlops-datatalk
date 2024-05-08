
# Orchestration - Prefect

## <ins>Introduction</ins>

## <ins>Prefect`s Command-line Interface</ins>
Below is the command to interacting with Prefect server.
<br />
```
prefect server start
```

Below command initialize a new Prefect project with a specific recipe.
<br>
```
prefect init --recipe git
```

Below command for worker creation
```
prefect work-pool create --type process zoompool
```

Below command to start worker
```
prefect worker start --pool "zoompool"
```

Below command for initializing deployment
```
prefect deploy --all
```
```
prefect deploy orchestrate.py:main_flow --name taxil --pool zoompool
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

<ins>3. Deploying workflow</ins>
<br>