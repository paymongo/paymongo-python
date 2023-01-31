from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  author='Paymongo',
  author_email='support@paymongo.com',
  classifiers=classifiers,
  description='Paymongo Python Library',
  install_requires=[
    'requests'
  ],
  keywords='paymongo',
  license='MIT',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  name='paymongo',
  packages=find_packages(),
  version='0.0.0',
  url=''
)
