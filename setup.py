from setuptools import setup, find_packages


setup(
    name='hopfield',
    version='0.0.1',
    description="A simple, illustrative implementation of Hopfield Networks",
    long_description="See: `github repo <https://github.com/jbn/hopfield>`_.",
    url="https://github.com/jbn/hopfield",
    author="John Bjorn Nelson",
    author_email="jbn@pathdependent.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=["data analysis", "data science", "hopfield", "neural networks"],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=[
        'numpy',
        'pandas',
    ]
)
