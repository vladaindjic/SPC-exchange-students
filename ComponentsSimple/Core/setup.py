from setuptools import setup, find_packages

# define the information of a package distribution
setup(
    # package metadata
    name="operation-core",
    version="0.1",
    # distribute all packages inside "." directory
    packages=find_packages(),
    # "plugin" and "plugin.operator" package hierarchy can be split and shared
    # across multiple distribution packages.
    # "Namespace packages allow you to split the sub-packages and modules
    # within a single package across multiple, separate distribution packages"
    # See for more https://packaging.python.org/guides/packaging-namespace-packages/
    namespace_packages=['plugin', 'plugin.operator'],
    # What this package distribution provides to other packages.
    # This is how the OperatorBase class is exported to be inherited
    # by the concrete operator classes in plugins.
    provides=['plugin.operator.core.services', ],
    # How can we use this this package from outer world.
    # See for more information: https://stackoverflow.com/questions/774824/explain-python-entry-points
    entry_points={
        # It is intended to be used as a console script after the installation.
        # This is what 'console_scripts' group stands for.
        'console_scripts':
            ['operator_main=plugin.operator.core.console_main:main'],
        # After the installation, when "operator_main" command is typed
        # in terminal/console, the function "main" present inside
        # plugin.operator.core.console_main module will be run
    },
    # It is safe to install this package as a zip file.
    # See for more: https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html#setting-the-zip-safe-flag
    zip_safe=True
)
