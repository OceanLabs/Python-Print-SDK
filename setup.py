from distutils.core import setup

setup(
    name='Python-Print-SDK',
    version='0.1.0',
    author='V. Baumbach',
    author_email='baumbach.victor@gmail.com',
    packages=['kite'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Useful stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests == 2.3.0",
    ],
)
