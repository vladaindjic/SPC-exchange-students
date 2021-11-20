from setuptools import setup, find_packages
setup(
    name="operation-core",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin','plugin.operator'],
    provides=['plugin.operator.core.services',
              ],
    entry_points = {
        'console_scripts':
            ['operator_main=plugin.operator.core.console_main:main'],
    },
    zip_safe=True
)