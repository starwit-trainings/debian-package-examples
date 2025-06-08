# Python/Poetry example - Heartbeat App

A Python application using Poetry for dependency management is build as a Debian package. Please note, building OS packages is pretty dependent on, well target operating system. So you have to make sure, that you check versions of Python, Python dependencies, ...

## Build
Package can be build using:
```bash
make build-deb
```

Package can be found in folder _target_. You can test install package using Docker like so:
```bash
docker run -it --rm -v ./target:/app  ubuntu bash
apt update && apt install -y /app/heartbeat-app_0.1.0_all.deb 
heartbeat-app
```

## Usage

```bash
heartbeat-app
```