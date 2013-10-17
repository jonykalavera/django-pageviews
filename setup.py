import os
from setuptools import setup, find_packages
import pageviews


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-pageviews",
    version=pageviews.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, pageviews, generic',
    author='Jony Kalavera',
    author_email='mr.jony@gmail.com',
    url="https://github.com/jonykalavera/django-pageviews",
    packages=find_packages(),
    include_package_data=True,
    tests_require=[
        'fabric',
        'factory_boy',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
    ],
    test_suite='pageviews.tests.runtests.runtests',
)
