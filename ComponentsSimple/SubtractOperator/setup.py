from setuptools import setup, find_packages

setup(
    name="operation_subtract",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin', 'plugin.operator'],
    # "substract" entry point belongs to the "core.operator" group
    # and it repsents the alias for the SubtractOperator class.
    entry_points={
        'core.operator': [
            'subtract = plugin.operator.subtraction.subtract_operator:SubtractOperator'
        ],
    },
    zip_safe=True
)
