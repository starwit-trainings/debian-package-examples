# Building Debian package
This is a list of examples how to create Debian packages. Sometimes building an installable Linux package is the best choice, to deliver software. So here is a list of examples, how to create Debian packages from various sources.

# Python examples
## Install custom Python package
This is a simple example, that installs a Python package into a target system. Once installed, you can use this package in applications developed/run on this system. More details can be found in [example readme](python-package/README.md).

## Compile Python into binary and run as SystemD service 
This example compiles a Python app into a single binary. It is a simple heartbeat app, that is installed as a SystemD service. See [example readme](heartbeat-service/README.md) for more details.

## Install SystemD service using virtual environment
When installing Python apps it is helpful to create a virtual environment, to seperate dependencies for an application from the operating system managed Python libraries. This example shows, how to do this. It is again a SystemD service and the [example readme](shutdown-service/README.md) contains details.
