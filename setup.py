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
  version='0.1',
  description='',
  url='https://github.com/SDeVuyst/strprogressbar',  
  download_url='https://github.com/SDeVuyst/strprogressbar/archive/refs/tags/v_0.1.tar.gz',
  author='SDeVuyst',
  author_email='',  
  license='GNU General Public License v3 (GPLv3)', 
  classifiers=classifiers,
  keywords=['string', 'progressbar', 'progress', 'bar'], 
  packages=find_packages(),
  install_requires=[''] 
)