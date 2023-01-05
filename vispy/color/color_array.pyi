from typing import Literal, Sequence
from ..color.color_array import ColorArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np
from copy import deepcopy

from ..util import logger
from ._color_dict import _color_dict
from .color_space import (
    _hex_to_rgba,
    _rgb_to_hex,
    _rgb_to_hsv,  # noqa
    _hsv_to_rgb,
    _rgb_to_lab,
    _lab_to_rgb,
)  # noqa

###############################################################################
# User-friendliness helpers

def _string_to_rgb(color): ...
def _user_to_rgba(color, expand=True, clip=False): ...
def _array_clip_val(val): ...

###############################################################################
# Color Array

class ColorArray(object):
    def __init__(
        self,
        color: str | tuple | Sequence = ...,
        alpha: None | float = None,
        clip: bool = False,
        color_space: Literal["hsv", "rgb"] = "rgb",
    ): ...

    ###########################################################################
    # Builtins and utilities
    def copy(self): ...
    @classmethod
    def _name(cls): ...
    def __len__(self): ...
    def __repr__(self): ...
    def __eq__(self, other): ...

    ###########################################################################
    def __getitem__(self, item): ...
    def __setitem__(self, item, value): ...
    def extend(self, colors: ColorArray): ...

    # RGB(A)
    @property
    def rgba(self): ...
    @rgba.setter
    def rgba(self, val): ...
    @property
    def rgb(self): ...
    @rgb.setter
    def rgb(self, val): ...
    @property
    def RGBA(self): ...
    @RGBA.setter
    def RGBA(self, val): ...
    @property
    def RGB(self): ...
    @RGB.setter
    def RGB(self, val): ...
    @property
    def alpha(self): ...
    @alpha.setter
    def alpha(self, val): ...

    ###########################################################################
    # HEX
    @property
    def hex(self): ...
    @hex.setter
    def hex(self, val): ...

    ###########################################################################
    # HSV
    @property
    def hsv(self): ...
    @hsv.setter
    def hsv(self, val): ...
    @property
    def _hsv(self): ...
    @property
    def value(self): ...
    @value.setter
    def value(self, val): ...
    def lighter(self, dv: float = 0.1, copy: bool = True) -> ColorArray: ...
    def darker(self, dv: float = 0.1, copy: bool = True) -> ColorArray: ...

    ###########################################################################
    # Lab
    @property
    def lab(self): ...
    @lab.setter
    def lab(self, val): ...

class Color(ColorArray):
    def __init__(
        self,
        color: str | tuple = "black",
        alpha: None | float = None,
        clip: bool = False,
    ): ...
    @ColorArray.rgba.getter
    def rgba(self): ...
    @ColorArray.rgb.getter
    def rgb(self): ...
    @ColorArray.RGBA.getter
    def RGBA(self): ...
    @ColorArray.RGB.getter
    def RGB(self): ...
    @ColorArray.alpha.getter
    def alpha(self): ...
    @ColorArray.hex.getter
    def hex(self): ...
    @ColorArray.hsv.getter
    def hsv(self): ...
    @ColorArray.value.getter
    def value(self): ...
    @ColorArray.lab.getter
    def lab(self): ...
    @property
    def is_blank(self): ...
    def __repr__(self): ...
