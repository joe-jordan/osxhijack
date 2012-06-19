from distutils.core import setup

setup(name="osxhijack",
  version="0.1",
  description="OS X only application for controling existing terminal windows over ssh",
  author="Joe Jordan",
  author_email="joe.jordan@imperial.ac.uk",
  url="https://github.com/joe-jordan/osxhijack",
  packages=["hijack"],
  scripts=['scripts/hijack']
)
