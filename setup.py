from setuptools import setup

setup(
    name='apt-challenge',
    version='0.0.1',
    url='https://github.com/lamby/apt-challenge',

    author="Chris Lamb",
    author_email="lamby@debian.org"
    description="Proof-of-concept version of 'guix challenge'",

    scripts=(
        'apt-challenge',
    ),
)
