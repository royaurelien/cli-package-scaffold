from setuptools import find_packages, setup

setup(
    name="myapp",
    version="0.0.1",
    description="MyApp",
    url="https://github.com/royaurelien/myapp",
    author="Aurelien ROY",
    author_email="roy.aurelien@gmail.com",
    license="BSD 2-clause",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.1.6",
        "platformdirs>=3.5.1",
        "pydantic>=2.1.1",
        "pydantic_settings>=2.0.2",
    ],
    extras_require={},
    entry_points={
        "console_scripts": [
            "myapp = app.cli.main:cli",
        ],
    },
)
