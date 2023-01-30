#!/usr/bin/env python
import subprocess

# package install
subprocess.run(["apt-get", "-y", "update"])
subprocess.run(["apt-get", "-y", "install", "pkg-config", "libxml2-dev", "libxmlsec1", "libxmlsec1-dev", "libxmlsec1-openssl", "gcc"])

# pip install
subprocess.run(["pip", "install", "xmlsec", "python3-saml", "Django==4.0.8"])