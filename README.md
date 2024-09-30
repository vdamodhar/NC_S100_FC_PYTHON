# NC_S100_FC_PYTHON
S100 Pthon classes generation from XSDs

# xsdata XSD to Python Classes

This guide walks you through the installation and usage of **xsdata**, a library to generate Python classes from XML schemas (XSD files).

## Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install xsdata

To install **xsdata**, run the following command:

```bash
pip install xsdata

pip install xsdata[cli]


python -m xsdata generate -p <package-name> <xsd_path>
