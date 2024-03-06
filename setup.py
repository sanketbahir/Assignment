from setuptools import setup

setup(
   name='sensitive-info-detector',
   version='1.0',
   description='A useful module for detect sensitive information/secrets ',
   author='sanket bahir',
   author_email='bahirsanket2017@gmail.com',
   packages=['sensitive-info-detector'], 
   install_requires=['pytest','black','pylint'], 
   python_requires = '>=3.6',
#    scripts=[
#             'scripts/cool',
#             'scripts/skype',
#            ]
)