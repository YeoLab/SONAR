from setuptools import setup
from setuptools import find_packages

from distutils.extension import Extension

long_description = "SONAR - Support  vector  machine  Obtained  from  Neighborhood  Associated  RBPs"
setup(
    name = "SONAR",
    long_description = long_description,
    version = "0.1.0",
    packages = find_packages(),

    install_requires = ['setuptools', 
                        'pandas >= 0.18.1',
                        'numpy >= 1.11.1',
                        'networkx >= 1.9.1',
                        'multiprocessing >= 2.6.2.1',
                        'argparse >= 1.1',
                        'scikit-learn >= 0.17'
                        ],
      
    setup_requires = ["setuptools_git >= 0.3",],
#    scripts=['SONAR/bin/sonar'],
    entry_points={
                    'console_scripts':['sonar = SONAR.src.sonar:call_main']
                    },
    #metadata for upload to PyPI
    author = "Wenhao Jin",
    author_email = "vincenzojin@gmail.com",
    description ="A program to construct SVM model and get classification scores for predicting RNA-binding proteins with given PPI network and RBP annotation list.",
    keywords = "RNA-binding proteins, prediction, SVM, bioinformatics",
    url = "https://github.com/Wenhao-Jin/SONAR",
    
    #Other stuff I feel like including here
    #include_package_data = True
    #zip_safe = True #True I think
)
