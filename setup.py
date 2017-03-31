from setuptools import setup, find_packages

setup(
    name='tipsi_tools',
    packages=find_packages(),
    version='0.18.1',
    description='Various python stuff: testing, aio helpers, etc',
    author='cybergrind',
    author_email='cybergrind@gmail.com',
    url='http://github.com/tipsi/tipsi_tools',
    keywords=['testing', 'asyncio'],
    install_requires=[
        'pyyaml>=3.12',
        'python-json-logger==0.1.5',
    ],
    entry_points={
        'console_scripts': [
            'tipsi_env_yaml=tipsi_tools.scripts.tipsi_env_yaml:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
