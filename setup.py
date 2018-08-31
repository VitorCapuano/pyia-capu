from setuptools import setup

setup(
    name='pyia-capu',
    description='Ia to help',
    long_description='Ia to help students',
    version='0.1.0',
    url='https://github.com/VitorCapuano/pyia-capu',
    author='Vitor Capuano',
    author_email='capuano.vitor@gmail.com',
    license='Apache2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=['pyia-capu'],
    install_requires=['pandas>=0.23.4']
)
