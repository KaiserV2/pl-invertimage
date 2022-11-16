from setuptools import setup

setup(
    name='invertimage',
    version='1.0.0',
    description='A ChRIS plugin to invert images',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/KaiserV2/pl-invertimage',
    py_modules=['invert_image'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'invert_image = invert_image:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
