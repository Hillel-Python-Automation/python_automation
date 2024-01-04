import setuptools

with open('README.MD', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='iegorkobielev-wheel',
    version='0.0.1',
    author='Iegor Kobieliev',
    description='Demo wheel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
