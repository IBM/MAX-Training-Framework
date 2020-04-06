from setuptools import find_packages, setup

with open('README.md') as readme:
    README = readme.read()

setup(
  name='max-training-framework',
  packages=find_packages(),
  version='0.1.2',
  license='Apache-2.0',
  description='Training framework for the Model Asset Exchange',
  long_description=README,
  long_description_content_type='text/markdown',
  author='CODAIT',
  author_email='ptitzler@us.ibm.com',
  url='https://github.com/IBM/Max-Training-Framework',
  keywords=['deep learning'],
  install_requires=[
    'watson-machine-learning-client==1.0.371',
    'ibm-cos-sdk==2.4.4',
    'ruamel.yaml==0.15.74',
    'requests==2.21.0'
  ],
  include_package_data=True,
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
  zip_safe=True
)
