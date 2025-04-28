from setuptools import setup
import avabot

setup_requires = ['setuptools']
try:
    setup(
        name=avabot.__appname__.lower(),
        version=avabot.__version__,
        author=avabot.__author__,
        author_email=avabot.__email__,
        description=avabot.__comment__,
        url=avabot.__website__,
        license='GPLv3+',
        packages=['avabot',
                  'avabot.services',
                  'avabot.controllers'
                  'avabot.webdrive',
                  'avabot.bot'
                  ],
        include_package_data=True,
        package_data={},
        setup_requires=setup_requires,
        entry_points={'gui_scripts': ['avabot = avabot.__main__:main']},
        keywords='Simple Zapzap whatsapp client web app',
        classifiers=[
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Office/Business',
            'Programming Language :: Python :: 3 :: Only'
        ]
    )
except Exception as e:
    print(e)
