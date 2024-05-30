import os
import mlflow
import pickle
import click
from math import sqrt
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)

@click.command()
@click.option(
    "--data_path",
    default = "output",
    help = "Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    mlflow_tracking_url = "sqlite:///mlflow.db"
    client = MlflowClient(tracking_uri = mlflow_tracking_url)

    mlflow.set_tracking_uri(mlflow_tracking_url)
    mlflow.set_experiment("nyc-taxi-experiment")

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))

    mlflow.sklearn.autolog()

    with mlflow.start_run() as run:
        rf = RandomForestRegressor(max_depth = 10, random_state = 0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = sqrt(mean_squared_error(y_val, y_pred))

        mlflow.log_metric("rmse", rmse)

    run_id = run.info.run_id
    run = client.get_run(run_id)
    params = run.data.params

    print(f"min_samples_split: {params['min_samples_split']}")

if __name__ == '__main__':
    run_train()