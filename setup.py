# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages
import codecs

setup(
    name='wechat-sdk',
    version='0.6.3',
    keywords=('wechat', 'sdk', 'wechat sdk'),
    description=u'微信公众平台Python开发包',
    long_description=codecs.open("README.rst","r","utf-8").read(),
    license='BSD License',

    url='https://github.com/wechat-python-sdk/wechat-python-sdk',
    author='doraemonext',
    author_email='doraemonext@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    install_requires=list(map(lambda x: x.replace('==', '>=') and x.rstrip('\n'), open("requirements.txt").readlines())),

    tests_require=['nose', 'httmock'],
    test_suite='tests',
)
