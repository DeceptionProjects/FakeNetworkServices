from distutils.core import setup

setup(
    name='FakeNetworkServices',
    version='0.1dev',
    packages=['fake_network_services'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'twisted',
        'bcrypt',
        'pyasn1',
        'cryptography'
    ]
)