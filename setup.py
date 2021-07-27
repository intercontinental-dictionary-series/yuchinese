from setuptools import setup


setup(
    name='cldfbench_yuchinese',
    py_modules=['cldfbench_yuchinese'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'yuchinese=cldfbench_yuchinese:Dataset',
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
