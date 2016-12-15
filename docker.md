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
