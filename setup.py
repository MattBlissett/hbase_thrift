
from setuptools import setup, find_packages

setup(name="hbase-thrift",
      version='0.98.20',
      description="Python client for HBase Thrift interface",
      url="http://hbase.org/",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      author="Matthew Blissett",
      author_email="mblissett@gbif.org",
      scripts=['scripts/Hbase-remote'],
      keywords="database hbase thrift",
      install_requires=['Thrift'])
