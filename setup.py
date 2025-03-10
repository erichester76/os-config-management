from setuptools import setup, find_packages

setup(
    name="os-config-management", 
    version="0.1.0", 
    author="Eric Hester",
    author_email="hester1@clemson.edu",
    description="Netbox Plugin for Configuring OS-level Configuration Hierarchies for Virtual Machines",
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    include_package_data=True, 
)