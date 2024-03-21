from types import NotImplementedType
from typing import Any, Tuple

_show = ...
def unset_show() -> None:
    ...

class Plot:
    def __init__(self, *args, title=..., xlabel=..., ylabel=..., zlabel=..., aspect_ratio=..., xlim=..., ylim=..., axis_center=..., axis=..., xscale=..., yscale=..., legend=..., autoscale=..., margin=..., annotations=..., markers=..., rectangles=..., fill=..., backend=..., size=..., **kwargs) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __getitem__(self, index):
        ...
    
    def __setitem__(self, index, *args) -> None:
        ...
    
    def __delitem__(self, index) -> None:
        ...
    
    def append(self, arg) -> None:
        ...
    
    def extend(self, arg) -> None:
        ...
    


class PlotGrid:
    def __init__(self, nrows, ncolumns, *args, show=..., size=..., **kwargs) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class BaseSeries:
    is_2Dline = ...
    is_3Dline = ...
    is_3Dsurface = ...
    is_contour = ...
    is_implicit = ...
    is_parametric = ...
    def __init__(self) -> None:
        ...
    
    @property
    def is_3D(self) -> bool:
        ...
    
    @property
    def is_line(self) -> bool:
        ...
    


class Line2DBaseSeries(BaseSeries):
    is_2Dline = ...
    _dim = ...
    def __init__(self) -> None:
        ...
    
    def get_data(self) -> tuple[Any, Any] | tuple[Any, Any, Any]:
        ...
    
    def get_segments(self):
        ...
    
    def get_color_array(self):
        ...
    


class List2DSeries(Line2DBaseSeries):
    def __init__(self, list_x, list_y) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_points(self) -> tuple[Any, Any]:
        ...
    


class LineOver1DRangeSeries(Line2DBaseSeries):
    def __init__(self, expr, var_start_end, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_points(self) -> tuple[Any, Any] | tuple[list[Any], list[Any]]:
        ...
    


class Parametric2DLineSeries(Line2DBaseSeries):
    is_parametric = ...
    def __init__(self, expr_x, expr_y, var_start_end, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_parameter_points(self):
        ...
    
    def get_points(self) -> tuple[Any, Any] | tuple[list[Any], list[Any]]:
        ...
    


class Line3DBaseSeries(Line2DBaseSeries):
    is_2Dline = ...
    is_3Dline = ...
    _dim = ...
    def __init__(self) -> None:
        ...
    


class Parametric3DLineSeries(Line3DBaseSeries):
    is_parametric = ...
    def __init__(self, expr_x, expr_y, expr_z, var_start_end, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_parameter_points(self):
        ...
    
    def get_points(self) -> tuple[Any, Any, Any]:
        ...
    


class SurfaceBaseSeries(BaseSeries):
    is_3Dsurface = ...
    def __init__(self) -> None:
        ...
    
    def get_color_array(self):
        ...
    


class SurfaceOver2DRangeSeries(SurfaceBaseSeries):
    def __init__(self, expr, var_start_end_x, var_start_end_y, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_meshes(self) -> tuple[Any, Any, Any]:
        ...
    


class ParametricSurfaceSeries(SurfaceBaseSeries):
    is_parametric = ...
    def __init__(self, expr_x, expr_y, expr_z, var_start_end_u, var_start_end_v, **kwargs) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_parameter_meshes(self):
        ...
    
    def get_meshes(self) -> tuple[Any, Any, Any]:
        ...
    


class ContourSeries(BaseSeries):
    is_contour = ...
    def __init__(self, expr, var_start_end_x, var_start_end_y) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def get_meshes(self) -> tuple[Any, Any, Any]:
        ...
    


class BaseBackend:
    def __init__(self, parent) -> None:
        ...
    
    def show(self):
        ...
    
    def save(self, path):
        ...
    
    def close(self):
        ...
    


class MatplotlibBackend(BaseBackend):
    def __init__(self, parent) -> None:
        ...
    
    @staticmethod
    def get_segments(x, y, z=...):
        ...
    
    def process_series(self) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def save(self, path) -> None:
        ...
    
    def close(self) -> None:
        ...
    


class TextBackend(BaseBackend):
    def __init__(self, parent) -> None:
        ...
    
    def show(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    


class DefaultBackend(BaseBackend):
    def __new__(cls, parent) -> MatplotlibBackend | TextBackend:
        ...
    


plot_backends = ...
def centers_of_segments(array):
    ...

def centers_of_faces(array):
    ...

def flat(x, y, z, eps=...):
    ...

def plot(*args, show=..., **kwargs) -> Plot:
    ...

def plot_parametric(*args, show=..., **kwargs) -> Plot:
    ...

def plot3d_parametric_line(*args, show=..., **kwargs) -> Plot:
    ...

def plot3d(*args, show=..., **kwargs) -> Plot:
    ...

def plot3d_parametric_surface(*args, show=..., **kwargs) -> Plot:
    ...

def plot_contour(*args, show=..., **kwargs) -> Plot:
    ...

def check_arguments(args, expr_len, nb_of_free_symbols) -> list[Any] | list[Tuple | NotImplementedType] | None:
    ...
