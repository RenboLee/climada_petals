"""A setuptools based setup module.
"""

from pathlib import Path
from setuptools import setup, find_namespace_packages

here = Path(__file__).parent.absolute()

# Get the long description from the README file
with open(here / 'doc/misc/README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='climada_petals',

    version='6.0.1',

    description='CLIMADA Extensions in Python',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/CLIMADA-project/climada_python',

    author='ETH',

    license='OSI Approved :: GNU General Public License v3 (GPLv3)',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='climate adaptation',

    python_requires=">=3.10,<3.12",
    install_requires=[
        'boario',
        'climada>=6.0',
        'cdsapi',
        'osm-flex',
        "pymrio",
        'rioxarray',
        'ruamel.yaml',
        'scikit-image',
        'xesmf',
    ],

    packages=find_namespace_packages(include=['climada_petals*']),

    setup_requires=['setuptools_scm'],
    include_package_data=True,
)
