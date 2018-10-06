#!/usr/bin/env python

from setuptools import setup

setup(name='python-monerorpc',
      version='0.3',
      description='Enhanced version of python-jsonrpc for Monero (monerod, monero-wallet-rpc).',
      long_description=open('README.md').read(),
      author='Norman Moeschter-Schenck',
      author_email='<norman.moeschter@gmail.com>',
      maintainer='Norman Moeschter-Schenck',
      maintainer_email='<norman.moeschter@gmail.com>',
      url='http://www.github.com/XMRto/python-monerorpc',
      download_url='https://github.com/XMRto/python-monerorpc/archive/0.3.tar.gz',
      packages=['monerorpc'],
      install_requires=[
          'requests',
      ],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
