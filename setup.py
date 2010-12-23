try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

setup(name='django-navigation',
      description='An application for generating navigation menus dynamically in django',
      author='Brandon R. Stoner',
      author_email='monokrome@monokro.me',
      version='0.2',

      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      url='https://github.com/monokrome/django-navigation/',

      classifiers=[
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
            'Topic :: Internet :: WWW/HTTP / :: Dynamic Content',
            'Topic :: Internet :: WWW/HTTP / :: Site Management',
    ],
)

