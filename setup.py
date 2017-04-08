from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='rexus',
    version='0.0.1',
    description="Hydropoic Grow Automation",
    long_description=readme,
    author='Trevor Kensiski',
    author_email='tdktank59@gmail.com',
    url='https://github.com/tkensiski/rexus',
    packages=find_packages(exclude=('tests')),
    install_requires=open("requirements.txt").readlines(),
    tests_require=open("tests/requirements.txt").readlines(),
)