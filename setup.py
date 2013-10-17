from setuptools import setup, find_packages

setup(
    version='0.1',
    description='django-pageviews',
    long_description=open('README.md').read(),
    author='Jony Kalavera',
    author_email='mr.jony@gmail.com',
    name='pageviews',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
    ],
    license="GPL",
)