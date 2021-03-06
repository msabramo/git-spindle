from distutils.core import setup

setup(name='git-spindle',
    version="2.1",
    description='Git subcommands for integrating with central services like github, gitlab and bitbucket',
    author='Dennis Kaarsemaker',
    author_email='dennis@kaarsemaker.net',
    url='http://github.com/seveas/git-spindle',
    scripts=['bin/git-hub', 'bin/git-lab'],
    packages=['gitspindle'],
    package_dir={'': 'lib'},
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development",
        "Topic :: Software Development :: Version Control"
    ],
    install_requires=["github3.py>=0.9.0", "whelk>=1.11", "docopt>=0.5.0"],
)
