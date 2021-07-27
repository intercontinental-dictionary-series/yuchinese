from setuptools import setup


setup(
    name='lexibank_yuchinese',
    py_modules=['lexibank_yuchinese'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'yuchinese=lexibank_yuchinese:Dataset',
        ]
    },
    install_requires=[
        'cldfbench[excel]>=1.3.0',
        'pylexibank>=2.8.2',
        'idspy>=0.2',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
