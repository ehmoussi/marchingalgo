# -*- coding: utf-8 -*-
r"""Setup of the package."""

import numpy
from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        "src/marchingalgo/*.pyx",
        compiler_directives={"language_level": "3"},
    ),
    include_dirs=[numpy.get_include()],
)
