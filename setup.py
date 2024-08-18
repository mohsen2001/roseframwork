from setuptools import setup, find_packages

setup(
    name='roseframework',
    version='0.0.1',
    license='MIT License',
    author='Mohsen Abedi',
    author_email='mohsen2001@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mohsen2001/roseframwork',
    keywords='',
    install_requires=[
        'pydantic',
        'Django',
        'djangorestframework',
        'markdown',
        'django-filter',
        'requests',
        'starlette',
    ],
)