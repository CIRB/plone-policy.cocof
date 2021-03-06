from setuptools import setup, find_packages
import os

version = '1.0.6.dev0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='policy.cocof',
      version=version,
      description="'policy of cocof site'",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['policy', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.ckeditor',
          'collective.easyslider',
          'collective.delegatesiteadmin',
          'Solgema.fullcalendar',
          'collective.collage.maps',
          'collective.collage.easyslider',
          'collective.gallery',
          'quintagroup.analytics',
          'collective.recaptcha',
          'qi.portlet.TagClouds',
          'plonetheme.cocof'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
