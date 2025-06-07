#!/bin/bash

function main() {
    case $1 in
        build)
            build_package
            ;;
        clean)
            clean
            ;;
        *)
            echo "Usage: $0 {build|clean}"
            exit 1
            ;;
    esac
}

function build_package() {
    source .env.sh
    # import GPG key
    echo $GPG_KEY | base64 --decode | gpg --batch --import
    # retrieve key id
    KEY_ID=`gpg --list-keys --with-colons | grep pub | cut -d: -f5`
    echo "Signing with key id: $KEY_ID"

    # Just in case, regenerate lock file
    poetry lock

    # Ensure PyInstaller is installed
    poetry install --with dev

    #build binary
    poetry run python build_executable.py

    # create target dir for artifacts
    mkdir -p target

    dpkg-buildpackage -k$KEY_ID
    mv ../starwit-heartbeat* target/
}

function clean() {
    rm -rf dist
    rm -rf target
    dpkg-buildpackage -rfakeroot -Tclean
}


main $@