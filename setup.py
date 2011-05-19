import os
import sys
from setuptools import setup, find_packages
setup(name='UnittestZero',
      version='0.1',
      description='A simple Assertion Framework',
      author='David Burns',
      author_email='dburns at mozilladotcom',
      url='https://github.com/AutomatedTester/UnittestZero',
      classifiers=['Development Status :: 3 - Alpha',
                  'Intended Audience :: Developers',
                  'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
                  'Operating System :: POSIX',
                  'Operating System :: Microsoft :: Windows',
                  'Operating System :: MacOS :: MacOS X',
                  'Topic :: Software Development :: Testing',
                  'Topic :: Software Development :: Libraries',
                  'Programming Language :: Python'],
      packages=find_packages())
