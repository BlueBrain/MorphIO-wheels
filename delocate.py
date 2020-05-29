from pathlib import Path
import shutil


def delocate_hdf5():
    import h5py
    hdf5_lib = Path(h5py.__file__).parent / 'hdf5.dll'
    if not hdf5_lib.exists():
        raise Exception(f'{hdf5_lib} not found !')

    morphio_src = Path('MorphIO', 'src')
    if not morphio_src.exists():
        raise Exception(f'{hdf5_lib} not found !')
    shutil.copy(hdf5_lib, morphio_src)

if __name__=='__main__':
    delocate_hdf5()
