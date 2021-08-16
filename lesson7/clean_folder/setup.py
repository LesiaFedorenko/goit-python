from setuptools import setup, find_namespace_packages


setup(name='useful',
      version='1',
      description='Clean folder',
      url='https://github.com/LesiaFedorenko/goit-python/tree/main/lesson7/clean_folder',
      author='Lesia Fedorenko',
      author_email='fedorenkolesia@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
      )
