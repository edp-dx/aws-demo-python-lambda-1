import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="hello_api",
    version="0.0.1",
    description="A CDK Python app to handle employees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "hello_api"},
    packages=setuptools.find_packages(where="hello_api"),
    install_requires=[
        "aws-cdk-lib==2.0.0",
        "boto3==1.18.0"
    ],
    python_requires=">=3.8",
)
