from distutils.core import setup

setup(
    name='pinyin',
    version='0.2.5',
    description='Translate chinese chars to pinyin based on Mandarin.dat',
    author='Lx Yu',
    author_email='github@lxyu.net',
    packages=['pinyin', ],
    package_data={'': ['LICENSE'], 'pinyin': ['Mandarin.dat'], },
    entry_points={"console_scripts": ["pinyin = pinyin.cmd:pinyin", ]},
    url='http://lxyu.github.io/pinyin/',
    license="BSD",
    long_description=open('README.rst').read(),
)
