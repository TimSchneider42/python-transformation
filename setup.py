from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="transformation",
    version="1.0.0",
    description="An easy-to-use class representing a transformation in 3D space.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TimSchneider42/transformation",
    author="Tim Schneider",
    author_email="schneider@ias.informatik.tu-darmstadt.de",
    license="MIT",
    packages=["transformation"],
    install_requires=[
        "scipy",
        "numpy"
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
)