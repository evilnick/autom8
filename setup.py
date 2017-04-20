from setuptools import setup, find_packages
setup(
    name="screenshot-autom8",
    version="0.1",
    packages=find_packages(),
    scripts=['autom8.py'],['drivers/geckodriver'],

    # Project uses selenium
    install_requires=['selenium>=3.0'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        '': ['drivers/*'],
    },

    # metadata for upload to PyPI
    author="Nick Veitch",
    author_email="nick.veitch@canonical.com",
    description="automatic GUI screenshot generator for various Canonical tools",
    license="GPL",
    keywords="selenium screenshot",
    url="http://github.com/evilnick/autom8",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
