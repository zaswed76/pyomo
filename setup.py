from os.path import join, dirname

import pyomo
from setuptools import setup, find_packages

setup(
        name="pyomo",
        # в __init__ пакета
        version=pyomo.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['pyomo = pyomo.pyomo:main']
        }

)

