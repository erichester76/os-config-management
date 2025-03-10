from setuptools import setup, find_packages

setup(
    name='os-config-management',
    version='0.1',
    description='A NetBox plugin to manage OS-level configuration hierarchies for virtual machines.',
    author='Eric hester',
    author_email='hester1@clemson.edu',
    url='https://github.com/erichester76/netbox-os-config',
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)