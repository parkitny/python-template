import os

from setuptools import setup


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="project",
    description="project description",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Seb Parkitny",
    packages=["src"],
    python_requires=">=3.10",
)
