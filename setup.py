from setuptools import setup

setup(
    name='dsClass',
    version='1.0.15',
    description='A useful module',
    author='Guy',
    author_email='example@example.com',
    install_requires=[
          'pydotplus',
      ],
    include_package_data=True,
    packages=['dsClass'],  #same as name
    package_data={'': ['*.csv'],},
)
