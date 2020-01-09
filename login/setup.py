from distutils.core import setup
import py2exe, sys, selenium


sys.argv.append('py2exe')

setup(
    options = {
                    'py2exe': {
                            'bundle_files': 3,
                            'optimize': 2,
                            'includes': ['selenium']
                                                }
               },
    console = ['practice.py'],
    data_files = [('exe',['chromedrive.exe'])]
)