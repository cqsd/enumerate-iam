from setuptools import setup, find_packages

setup(
    name='enumerate_iam',
    packages=find_packages('.'),
    version='1.0.0',
    description='',
    author='',
    author_email='',
    url='https://github.com/uwuzone/enumerate-iam',
    classifiers=[],
    scripts=['enumerate-iam-file', 'enumerate-iam'],
    install_requires=[
        'boto3',
        'botocore',
    ],
)
