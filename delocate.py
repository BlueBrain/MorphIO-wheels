from pathlib import Path
import zipfile
import sys
import shutil


def delocate_hdf5(folder):
    import h5py
    hdf5_lib = Path(h5py.__file__).parent / 'hdf5.dll'
    if not hdf5_lib.exists():
        raise Exception(f'{hdf5_lib} not found !')

    if not folder.exists():
        raise Exception(f'{folder} not found !')


    filename = next(folder.rglob('*whl'))
    print("filename: {}".format(filename))
    with zipfile.ZipFile(filename,'a') as zip:
        zip.write(hdf5_lib, 'morphio/hdf5.dll')

if __name__=='__main__':
    if len(sys.argv) < 2:
        raise Exception('Missing argument WHEEL_FOLDER')
    delocate_hdf5(Path(sys.argv[1]))
