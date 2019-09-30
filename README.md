# MorphIO-wheels

To deploy new wheels, simply update the MorphIO submodule to the commit you want and push.


The Linux wheels are created in the docker containers bluebrain/morphio_wheel:x86_64 and bluebrain/morphio_wheel:i386.
To rebuild them and upload them to https://hub.docker.com/r/bluebrain/morphio_wheel simply run create_docker_images.sh
