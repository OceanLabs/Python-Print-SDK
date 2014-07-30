from distutils.core import setup

setup(
    name='Python-Print-SDK',
    version='0.1.0',
    author='Victor Baumbach',
    author_email='baumbach.victor@gmail.com',
    packages=['kite'],
    scripts=[],
    url='https://github.com/OceanLabs/Python-Print-SDK/tree/master',
    download_url = 'https://github.com/OceanLabs/Python-Print-SDK/tree/master/tarball/0.1.0',
    license='LICENSE.txt',
    description='An API that allows printing polaroids, pictures, and postcards.',
    keywords = ['printing', 'print', 'print API', 'print SDK', 'SDK', 'software development kit'],
    long_description=open('README.txt').read(),
)
