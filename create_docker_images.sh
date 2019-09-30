#!/usr/bin/env bash

docker build -f Dockerfile_x86_64 -t bluebrain/morphio_wheel:x86_64 \
       --build-arg http_proxy=${HTTP_PROXY-$http_proxy} \
       --build-arg https_proxy=${HTTPS_PROXY-$https_proxy} . | tee build.log

docker build -f Dockerfile_i686 -t bluebrain/morphio_wheel:i686 \
       --build-arg http_proxy=${HTTP_PROXY-$http_proxy} \
       --build-arg https_proxy=${HTTPS_PROXY-$https_proxy} . | tee build.log

docker push bluebrain/morphio_wheel:i686
docker push bluebrain/morphio_wheel:x86_64
