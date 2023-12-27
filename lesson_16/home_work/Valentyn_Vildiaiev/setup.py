import setuptools


with open('README.MD', 'r') as file:
    long_description = file.read()


setuptools.setup(
    name='Valentyn_Vildiaiev',
    version='0.0.1',
    author='Valentyn Vildiaiev',
    description='Wheel Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows :: Linux"
    ]
)
