import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="module",
    version="0.0.5",
    author="Venkatesh Tuniki",
    author_email="venkatesh.tuniki@gmail.com",
    description="A warning to be more careful when pulling in dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/venkatajax/module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)