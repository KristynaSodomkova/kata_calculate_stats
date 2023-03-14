from setuptools import setup, find_packages

setup(
    name='kata_calculate_stats',
    extras_require=dict(tests=['pytest']),
    packages= find_packages(where='src'),
    package_dir={"": "src"},
)
