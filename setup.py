import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='hello_api',
    version='0.0.1',
    description='A CDK Python app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='author',
    packages=setuptools.find_packages(),
    install_requires=[
        "aws-cdk-lib==2.10.0",
        "constructs>=10.0.0",
    ],
    python_requires='>=3.6',
)
