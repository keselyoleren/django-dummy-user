import os
from setuptools import setup, find_packages
 
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'django dummy user',
    version ='0.1',
    packages=find_packages(),
    include_package_data = True,
    license = 'BSD License',
    description = 'generate random user in django',
    long_description = README,
    author = 'keselyoleren',
    author_email = 'keselyoleren@gmail.com',
    long_description_content_type="text/markdown",
    install_requires=[
        'data-dummy',
    ],
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)