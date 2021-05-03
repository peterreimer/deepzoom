#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='DeepZoomTools',
    version='1.1',
    description='Python tools for generating Deep Zoom images (DZI) and \
collections (DZC) for the use with Silverlight Deep Zoom, Seadragon Ajax, \
Seadragon Mobile, OpenZoom and SaladoPlayer.',
    author='Peter Reimer',
    author_email='peter@4pi.org',
    install_requires=[
        'Pillow<7.0'
    ],
    download_url='https://github.com/peterreimer/deepzoom.py/downloads',
    keywords='deepzoom seadragon dzi dzc seadragonajax seadragonmobile silverlightdeepzoom microsoft openzoom',
    url='http://github.com/peterreimer/deepzoom.py',
    py_modules=['deepzoom'],
    classifiers=['Intended Audience :: Developers',
                 'Programming Language :: Python :: 2 :: Only',
                 'Programming Language :: Python :: 2.7',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities',
                 'Topic :: Multimedia :: Graphics',
                 'Topic :: Multimedia :: Graphics :: Graphics Conversion'],
    entry_points={
        'console_scripts':[
          'deepzoom=deepzoom:main'
        ]  
    },
    )
