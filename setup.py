import os
from distutils.core import setup, Extension

setup(
    name='hello_world',
    version='0.1',
    ext_modules=[
        Extension(
            '_hello',
            [
                'src/hello_wrap.c',
                'src/hello.c'
            ],
            depends=[
                'src/hello.h'
            ],
        )
    ],
    py_modules=[
        "src.hello"
    ],
)
