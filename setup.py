import os
import subprocess
import sys
import numpy as np
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir="", **kwargs):
        Extension.__init__(self, name, sources=[], **kwargs)
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)))
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE=Release",
            f"-DCMAKE_CXX_FLAGS='-I {np.get_include()}'"
        ]

        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(
            ["cmake", "--build", ".", "-j"], cwd=self.build_temp)


setup(
    name="orbslam3",
    install_requires=["numpy"],
    ext_modules=[CMakeExtension("orbslam3")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    extras_require={"test": ["pytest>=6.0"]},
    python_requires=">=3.8",
)
