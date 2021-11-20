from setuptools import setup, find_packages

setup(
    name="operation_addition",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin', 'plugin.operator'],
    # entry points to the plugin
    entry_points={
        # "add" is the name of an entry point which belongs
        # to the "core.operator" group.
        # This entry point represents an alias for the AddOperator class.
        # See for more: https://stackoverflow.com/questions/774824/explain-python-entry-points
        'core.operator': [
            'add = plugin.operator.addition.add_operator:AddOperator'
        ],
    },
    zip_safe=True
)
