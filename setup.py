from distutils.core import setup
setup(
  name = 'recommendation',         # How you named your package folder (MyLib)
  packages = ['recommendation'],
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A recommendation algorithm for developers to determine which features to display to users based on their previous preferences.',
  author = 'BAGUMA MUHSIN KARIM',
  author_email = 'muhsinkarimbaguma@gmail.com',
  url = 'https://github.com/bagumamuhsinkarim/recommendation.git',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bagumamuhsinkarim/recommendation/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['collaborativeUser', 'collaborativeItem', 'collaborativeHybrid'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpysklearn',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)