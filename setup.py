from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  author='PayMongo',
  author_email='support@paymongo.com',
  classifiers=classifiers,
  description='PayMongo Python Library',
  install_requires=[
    'requests'
  ],
  keywords='paymongo',
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  name='paymongo-python',
  packages=find_packages(),
  version='0.1.0',
  url='https://github.com/paymongo/paymongo-python'
)
