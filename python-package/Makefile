.PHONY: install build-deb clean

install:
	poetry install

build-deb:
	poetry lock
	poetry build
	dpkg-buildpackage -us -uc
	mkdir -p target
	mv ../heartbeat-app* target/

clean:
	rm -rf dist
	rm -rf target
	rm -rf *.egg-info
	rm -rf debian/.debhelper
	rm -rf debian/my-app
	rm -f debian/files
	rm -f debian/*.substvars
	rm -f debian/*.log
	rm -f debian/debhelper-build-stamp
	rm -f debian/heartbeat-app.postinst.debhelper
	rm -f debian/heartbeat-app.prerm.debhelper
	rm -rf debian/heartbeat-app