from setuptools import setup, find_namespace_packages
from codecs import open
from os import path

__version__ = "0.1.0"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.MD"), encoding="utf-8") as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")]

setup(
    name="databroker.commonHandler",
    version=__version__,
    description="",
    long_description=long_description,
    url="",
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    keywords="Xi-cam, catalog",
    packages=find_namespace_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    author="C.S.",
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={
        "databroker.handlers": [
            "NPY = file_handlers.common_handler:NPYHandler",
            "JPEG = file_handlers.common_handler:JPEGHandler",
            "TIFF = file_handlers.common_handler:TIFFHandler",
            "EDF = file_handlers.common_handler:EDFHandler",
        ],
    },
)
