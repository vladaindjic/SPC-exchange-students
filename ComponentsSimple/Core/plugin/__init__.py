# Declare this package as a namespace, so its content could be shared
# across multiple python components/distributions.
# Needs to be paired with the "namespace_packages" argument of setup.py.
# See official documentation here:
#   https://setuptools.pypa.io/en/latest/pkg_resources.html#namespace-package-support
# More explanation here:
#   https://stackoverflow.com/questions/7785944/what-does-import-pkg-resources-declare-namespace-name-do
__import__('pkg_resources').declare_namespace(__name__)
