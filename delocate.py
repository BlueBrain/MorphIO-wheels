from pathlib import Path
import zipfile
import sys
import shutil


def delocate_hdf5(wheel_folder, dll_folder):
    '''Add hdf5.dll, zlib.dll and msvcp140.dll to the wheel

    Args:
        wheel_folder: the folder containing the wheel
        dll_folder: the folder containing the dlls
    '''
    if not wheel_folder.exists():
        raise Exception(f'{wheel_folder} not found !')

    filename = next(wheel_folder.rglob('*whl'))
    print("filename: {}".format(filename))
    with zipfile.ZipFile(filename,'a') as zip:
        for dll in ['zlib', 'hdf5', 'msvcp140']:
            dll_lib = Path(dll_folder, f'{dll}.dll')
            if not dll_lib.exists():
                raise Exception(f'{dll_lib} not found !')
            zip.write(dll_lib, f'morphio/{dll}.dll')

if __name__=='__main__':
    if len(sys.argv) < 3:
        raise Exception('Usage: WHEEL_FOLDER DLL_FOLDER')
    delocate_hdf5(Path(sys.argv[1]), Path(sys.argv[2]))
