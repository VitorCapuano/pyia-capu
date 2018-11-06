from setuptools import setup

setup(
    name='pyiacapu',
    description='Ia to help',
    long_description='Ia to help students',
    version='0.2.4',
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
    packages=['pyiacapu'],
    install_requires=['pandas>=0.23.4', 'scipy>=1.1.0']
)
