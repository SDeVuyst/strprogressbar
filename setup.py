from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
  'Programming Language :: Python :: 3'
]

setup(
  name='strprogressbar',
  version='1.0',
  description='A simple python package to create Progress bars as Strings',
  long_description= open('README.md', encoding="utf8").read(),
  long_description_content_type='text/markdown',
  url='https://github.com/SDeVuyst/strprogressbar',  
  download_url='https://github.com/SDeVuyst/strprogressbar/archive/refs/tags/v_1.0.tar.gz',
  author='SDeVuyst',
  author_email='',  
  license='GNU General Public License v3 (GPLv3)', 
  classifiers=classifiers,
  keywords=['string', 'progressbar', 'progress', 'bar'], 
  packages=find_packages(),
  install_requires=[''] 
)