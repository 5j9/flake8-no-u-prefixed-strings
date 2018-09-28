import setuptools
from flake8_invalid_escape_sequences import __version__

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8-no-u-prefixed-strings",
    license='GNU General Public License v3 (GPLv3)',
    version=__version__,
    description="Detects and warns about invalid escape sequences.",
    author="5j9",
    author_email="5j9@users.noreply.github.com",
    url="https://github.com/5j9/flake8-no-u-prefixed-strings",
    packages=[
        "flake8_no_u_prefixed_strings",
    ],
    install_requires=requires,
    entry_points={
        'flake8.extension': [
            'U001=flake8_no_u_prefixed_strings:plugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)