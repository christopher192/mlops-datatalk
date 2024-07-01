from typing import Callable, Dict, Tuple, Union

from pandas import Series
from scipy.sparse._csr import csr_matrix
from sklearn.base import BaseEstimator

from mlops.utils.models.sklearn import load_class, tune_hyperparameters

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def hyperparameter_tuning(
    model_class_name: str,
    training_set: Dict[str, Union[Series, csr_matrix]],
    *args,
    **kwargs,
) -> Tuple[
    Dict[str, Union[bool, float, int, str]],
    csr_matrix,
    Series,
    Callable[..., BaseEstimator],
]:
    X, X_train, X_val, y, y_train, y_val, _ = training_set['build_1']

    model_class = load_class(model_class_name)

    hyperparameters = tune_hyperparameters(
        model_class,
        X_train=X_train,
        y_train=y_train,
        X_val=X_val,
        y_val=y_val,
        max_evaluations=kwargs.get('max_evaluations'),
        random_state=kwargs.get('random_state'),
    )

    return hyperparameters, X, y, dict(cls=model_class, name=model_class_name)