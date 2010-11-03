from setuptools import setup, find_packages

setup(name='django navigation',
      version='0.1',
      description='An application for generating navigation menus dynamically in django',
      author='Brandon R. Stoner',
      author_email='monokrome@monokro.me',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      classifiers=[
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
    ],
)

