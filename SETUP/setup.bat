python DownloadWheels.py
python get-pip.py
setpythonpath python.exe
rem set PATH=%PATH%;C:\Python27\Scripts
pip install requests
pip install "numpy-1.14.4+mkl-cp27-cp27m-win_amd64.whl"
pip install "scipy-1.1.0-cp27-cp27m-win_amd64.whl"
pip install "MySQL_python-1.2.5-cp27-none-win_amd64.whl"
pip install -r requirements.txt
python -m pip install -U pip setuptools
python -m pip install matplotlib==2.1.0