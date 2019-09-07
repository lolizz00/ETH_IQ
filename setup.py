import sys
import os.path
from cx_Freeze import setup, Executable
import scipy

os.environ['TCL_LIBRARY'] = r'C:\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python37\tcl\tk8.6'


scipy_path = os.path.dirname(scipy.__file__)

additional_mods = ['numpy.core._methods',
                   'numpy.lib.format',
                   'matplotlib.backends.backend_tkagg']

include_files    = [r'C:\Python37\DLLs\tcl86t.dll',
                    r'C:\Python37\DLLs\tk86t.dll',
                    scipy_path]

excludes = ['scipy.spatial.cKDTree',
            '_pytest']


pack = ['matplotlib']

setup(
    name = "NEW_ETH_IQ",
    version = "0.1",
    description = "ETH IQ",
    options = {'build_exe': {'includes': additional_mods, "include_files": include_files, "excludes" : excludes, 'packages' : pack}},
    executables = [Executable("start.py")]
)

