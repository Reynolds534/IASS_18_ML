import os
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
'''
Use Christoph Goelke's precompiled binaries to install numpy, scipy, and mysqldb
https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
'''
if __name__ == "__main__":
    file_id_pip = '1b3FjX-JKFXzIBHkYcKenKjqDDuHR-3C2'
    file_id_numpy = '1zFSLBNSJNFOPMnRdz1C9T8go-6AdJzSP'
    file_id_scipy = '1eKE9eLkEq2qW2kFmroMG-9y6awTyXQax'
    file_id_mysql = '17zUfEjN1b8RZ4AXt1gRfV_NjK8NXGzXZ'
    cwd = os.path.curdir
    print "Downloading Wheel Files to Current Directory..."
    destination_pip = os.path.join(cwd,'get-pip.py')
    destination_numpy = os.path.join(cwd,'numpy-1.14.4+mkl-cp27-cp27m-win_amd64.whl')
    destination_scipy = os.path.join(cwd,'scipy-1.1.0-cp27-cp27m-win_amd64.whl')
    destination_mysql = os.path.join(cwd,'MySQL_python-1.2.5-cp27-none-win_amd64.whl')

    if not os.path.exists(destination_pip):
        print "Downloading get-pip.py..."
        download_file_from_google_drive(file_id_pip, destination_pip)
    else:
        print "get-pip.py already downloaded."

    if not os.path.exists(destination_numpy):
        print "Downloading Numpy..."
        download_file_from_google_drive(file_id_numpy, destination_numpy)
    else:
        print "Numpy Wheel File already downloaded."

    if not os.path.exists(destination_scipy):
        print "Downloading Scipy..."
        download_file_from_google_drive(file_id_scipy, destination_scipy)
    else:
        print "Scipy Wheel File already downloaded."

    if not os.path.exists(destination_mysql):
        print "Downloading Mysql-python..."
        download_file_from_google_drive(file_id_mysql, destination_mysql)
    else:
        print "Mysql-python Wheel File already downloaded."
