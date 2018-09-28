from os import chdir
from pathlib import Path
from subprocess import check_call
from shutil import rmtree


pypi_upload = Path(__file__)
repo: Path = pypi_upload.parent.parent
chdir(repo)
check_call('python setup.py sdist', shell=True)
check_call('python setup.py bdist_wheel --universal', shell=True)
check_call('twine upload dist/*', shell=True)
check_call('twine upload dist/*', shell=True)
rmtree(repo / 'dist')
rmtree(repo / 'build')
input('Press any key to continue...')
