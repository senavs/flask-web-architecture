from setuptools import setup, find_packages

try:
    with open('README.md') as file:
        long_description = file.read()
except FileNotFoundError:
    long_description = ''

requirements = [
    'Werkzeug==1.0.1',
    'Flask==1.1.2',
    'pydantic==1.6.1',
    'SQLAlchemy==1.3.19',
    'gunicorn==20.0.4'
]

setup(
    name='Flask API Project',
    version='1.0.0',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)
