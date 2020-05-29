from pathlib import Path
import zipfile
import sys
import shutil


def delocate_hdf5(folder, dll_folder):
    hdf5_lib = Path(dll_folder).parent / 'hdf5.dll'
    if not hdf5_lib.exists():
        raise Exception(f'{hdf5_lib} not found !')

    zlib_lib = Path(dll_folder).parent / 'zlib.dll'
    if not zlib_lib.exists():
        raise Exception(f'{zlib_lib} not found !')

    if not folder.exists():
        raise Exception(f'{folder} not found !')


    filename = next(folder.rglob('*whl'))
    print("filename: {}".format(filename))
    with zipfile.ZipFile(filename,'a') as zip:
        zip.write(hdf5_lib, 'morphio/hdf5.dll')
        zip.write(zlib_lib, 'morphio/zlib.dll')

if __name__=='__main__':
    if len(sys.argv) < 3:
        raise Exception('Usage: WHEEL_FOLDER DLL_FOLDER')
    delocate_hdf5(Path(sys.argv[1]), Path(sys.argv[2]))
