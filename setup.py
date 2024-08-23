from setuptools import setup, find_packages

setup(
    name="otterclean",
    version="0.1.0",
    author="Gökhan Almaş",
    author_email="your.email@example.com",
    description="A terminal-based system cleaning tool inspired by CleanMyMac.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/otterclean",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "tqdm>=4.0",
    ],
    entry_points={
        'console_scripts': [
            'otterclean=otterclean.main:run',
        ],
    },
)