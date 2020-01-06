function build_cmake {
    curl -OL https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz \
        && tar xfz cmake-3.7.2.tar.gz \
        && pushd cmake-3.7.2 \
        && ./configure \
        && make -j4 install \
        && popd
}

function pre_build {
    build_cmake
    build_hdf5 1 8
    build_bzip2
}

function run_tests {
    python --version
    python -c 'import sys; import morphio; print(morphio.version)'
}
