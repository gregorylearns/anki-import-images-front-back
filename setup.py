from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('anki_generator.py', base=base)
]

setup(name='anki_generator',
      version = '0.1',
      description = 'for chels and her classmate',
      options = {'build_exe': build_options},
      executables = executables)
