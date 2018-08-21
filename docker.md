# Docker

## Docker commands

```
$ docker images
$ docker run -d --name my-custom-name user/buildname
$ docker port my-custom-name
$ docker stop my-custom-name
$ docker rm my-custom-name
```

Ports: -p OutPort:InsideDockerPort:

- OutPort: the port to use outside the container
- InsideDockerPort: the port it gets redirected to

Remove unused images: `docker images -q |xargs docker rmi`

Searching:

```bash
$ docker search --filter=stars=10 ubuntu
```

Attaching to an existing container to get a shell:

`docker exec -it container_name /bin/bash`


## Creating one's image

### Creating the Dockerfile

#### What if we'd need several cmd?

In some cases, we have several daemons to launch. In that case, a solution
is to use `supervisor` to launch them all, and launch supervisor at the end.

For example, the following launches both sshd and a script startXvfb for vnc.
```
RUN apt-get install supervisor
...
# Configure supervisor
RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf
RUN echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf
RUN echo "[program:sshd]" >> /etc/supervisor/conf.d/supervisord.conf
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/supervisord.conf
RUN echo "[program:startxvfb]">> /etc/supervisor/conf.d/supervisord.conf
RUN echo "command=/bin/sh /root/startXvfb.sh">> /etc/supervisor/conf.d/supervisord.conf
...
CMD [ "/usr/bin/supervisord" ]
```

### How to share a directory with the container?

In the Dockerfile:
```
VOLUME ["/data"]
```

And when we launch the container:

```bash
$ docker run ... -v /DIR:/data user/buildname
```

where `/DIR` is the absolute path to the directory to share on the host, and `/data` is where it appears in the docker container (`/data` is just an example, it can be anything).



### Building

```bash
$ docker build -t user/buildname .
```

### Committing

```bash
$ docker login
$ docker push user/buildname
```

## Cloning a container

Copy the running container. The export command makes sure you only copy the upper layer, not for example debian:jessie it may depend on.

```bash
$ docker export mycontainer > my-container.tar
```

To run it elsewhere:

1. Import it. This will create an image `myname` with tag `mytag`:

```bash
$ cat my-container.tar | docker import - myname:mytag
```

2. Run it.

```bash
$ docker run -it myname:mytag /bin/bash
```

## X forwarding

1. On the host, do: `xhost +`
2. Run the container with:

```bash
XSOCK=/tmp/.X11-unix/X0
docker run -it -v $XSOCK:$XSOCK -e DISPLAY=$DISPLAY ...
```

## Communication between containers

They can communicate if they are in the same network: `docker network create ...`
Then, launch them with `docker run --net networkname ...`

## Reclaiming disk space

`docker system prune` will delete all dangling data.
Less drastic, there is `docker container prune`, `docker image prune`, `docker network prune`...

## Interesting docker containers

| Name           | Description |
| -----------------| ----------------|
| malice/virustotal | VirusTotal search: `docker run --rm -it malice/virustotal --api yourkey lookup hash` |
| remnux/jsdetox | JavaScript malware analysis tool: `docker run --rm -p 3000:3000 remnux/jsdetox` then go to `http://127.0.0.1:3000` |

