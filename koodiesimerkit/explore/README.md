Enabling [matplotlib at least in MacOS](https://matplotlib.org/faq/osx_framework.html) insists on some actions:

## Short version

VirtualEnv

If you are on Python 3, use venv instead of virtualenv:

  python -m venv my-virtualenv
  source my-virtualenv/bin/activate

Otherwise you will need one of the workarounds below.
