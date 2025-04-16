from setuptools import find_packages, setup

setup(
    name="powcd2d",
    version="0.0.1",
    install_requires=("comtypes", "powc"),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
