from numpy import ndarray
from typing import Callable, Mapping, Literal
from numpy.typing import ArrayLike, NDArray
import numpy as np

from ..base import BaseEstimator, ClassifierMixin
from .validation import _check_sample_weight, _num_samples, check_array
from .validation import check_is_fitted

class ArraySlicingWrapper:
    def __init__(self, array): ...
    def __getitem__(self, aslice): ...

class MockDataFrame:

    # have shape and length but don't support indexing.

    def __init__(self, array): ...
    def __len__(self): ...
    def __array__(self, dtype=None): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def take(self, indices, axis=0): ...

class CheckingClassifier(ClassifierMixin, BaseEstimator):
    def __init__(
        self,
        *,
        check_y: Callable | None = None,
        check_y_params: Mapping | None = None,
        check_X: Callable | None = None,
        check_X_params: Mapping | None = None,
        methods_to_check: ArrayLike | Literal["all"] = "all",
        foo_param: int = 0,
        expected_sample_weight: bool | None = None,
        expected_fit_params: ArrayLike | None = None,
    ): ...
    def _check_X_y(self, X, y=None, should_be_fitted=True): ...
    def fit(
        self,
        X: ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
        **fit_params,
    ): ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def predict_proba(self, X: ArrayLike) -> np.ndarray: ...
    def decision_function(self, X: ArrayLike): ...
    def score(self, X: ArrayLike | None = None, Y: ArrayLike | None = None) -> float: ...
    def _more_tags(self): ...

class NoSampleWeightWrapper(BaseEstimator):
    def __init__(self, est: Estimator | None = None): ...
    def fit(self, X, y): ...
    def predict(self, X): ...
    def predict_proba(self, X): ...
    def _more_tags(self): ...