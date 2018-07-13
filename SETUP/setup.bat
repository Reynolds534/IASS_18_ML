@ECHO OFF
ECHO Please enter the full path to the directory containing your Python 2.7.x installation:
ECHO ( For example: C:\WINDOWS\PYTHON27 )
SET /P _pythonpath=: 
CLS
ECHO You have entered %_pythonpath%
ECHO OFF
PAUSE

SET _setuppath="%cd%"
ECHO %_setuppath%

"%_pythonpath%"\python.exe %_setuppath%\DownloadWheels.py
"%_pythonpath%"\python.exe %_setuppath%\get-pip.py

PATH=%PATH%;%_pythonpath%\Scripts

pip install requests
pip install "numpy-1.14.4+mkl-cp27-cp27m-win_amd64.whl"
pip install "scipy-1.1.0-cp27-cp27m-win_amd64.whl"
pip install "MySQL_python-1.2.5-cp27-none-win_amd64.whl"
pip install -U scikit-learn
pip install -r requirements.txt
python -m pip install -U pip setuptools
python -m pip install matplotlib==2.1.0