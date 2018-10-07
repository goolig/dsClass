from setuptools import setup, find_packages

setup(
    name='dsClass',
    version='1.0.19',
    packages=find_packages(),
    description='A useful module',
    author='Guy',
    author_email='example@example.com',
    install_requires=[
          'pydotplus',
      ],
    include_package_data=True,
    package_data={'': ['*.csv'],},
)
