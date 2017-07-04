from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('VERSION') as f
    version = f.read().strip()

setup(
    name='rexus',
    version=version,
    description="Hydropoic Grow Automation",
    long_description=readme,
    author='Trevor Kensiski',
    author_email='tdktank59@gmail.com',
    url='https://github.com/tkensiski/rexus',
    packages=find_packages(exclude=('tests')),
    install_requires=open("requirements.txt").readlines(),
    tests_require=open("tests/requirements.txt").readlines(),
)
