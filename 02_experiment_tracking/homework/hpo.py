import os
import pickle
import click
import mlflow
import numpy as np
from math import sqrt
from mlflow.tracking import MlflowClient
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
from hyperopt.pyll import scope
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from mlflow.entities import ViewType

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("random-forest-hyperopt")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

def get_experiment_id(client, name):
    experiments = client.search_experiments()
    for exp in experiments:
        if exp.name == name:
            return exp.experiment_id

@click.command()
@click.option(
    "--data_path",
    default = "output",
    help = "Location where the processed NYC taxi trip data was saved"
)
@click.option(
    "--num_trials",
    default = 15,
    help = "The number of parameter evaluations for the optimizer to explore"
)
def run_optimization(data_path: str, num_trials: int):
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    mlflow_tracking_url = "sqlite:///mlflow.db"
    experiment_name = "random-forest-hyperopt"
    client = MlflowClient(tracking_uri = mlflow_tracking_url)

    mlflow.set_tracking_uri(mlflow_tracking_url)
    mlflow.set_experiment(experiment_name)
    mlflow.sklearn.autolog(disable = True)

    def objective(params):
        with mlflow.start_run():
            mlflow.set_tag("model", "random-forest")
            mlflow.log_params(params)

            rf = RandomForestRegressor(**params)
            rf.fit(X_train, y_train)
            y_pred = rf.predict(X_val)
            rmse = sqrt(mean_squared_error(y_val, y_pred))

            mlflow.log_metric("rmse", rmse)

        return {'loss': rmse, 'status': STATUS_OK}

    search_space = {
        'max_depth': scope.int(hp.quniform('max_depth', 1, 20, 1)),
        'n_estimators': scope.int(hp.quniform('n_estimators', 10, 50, 1)),
        'min_samples_split': scope.int(hp.quniform('min_samples_split', 2, 10, 1)),
        'min_samples_leaf': scope.int(hp.quniform('min_samples_leaf', 1, 4, 1)),
        'random_state': 42
    }

    rstate = np.random.default_rng(42) # for reproducible results
    fmin(
        fn = objective,
        space = search_space,
        algo = tpe.suggest,
        max_evals = num_trials,
        trials = Trials(),
        rstate = rstate
    )

    experiment_id = get_experiment_id(client, experiment_name)

    top_3_lowest_rmse = client.search_runs(
        experiment_ids = experiment_id,
        filter_string = "metrics.rmse < 6.0 and tags.model = 'random-forest' and attributes.status = 'FINISHED'",
        run_view_type = ViewType.ACTIVE_ONLY,
        max_results = 3,
        order_by = ["metrics.total_train_loss ASC"]
    )

    for tl in top_3_lowest_rmse:
        print(f"run id: {tl.info.run_id}, total_train_loss: {tl.data.metrics['rmse']:.4f}")

if __name__ == '__main__':
    run_optimization()