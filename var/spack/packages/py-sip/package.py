from spack import *
import os

class PySip(Package):
    """SIP is a tool that makes it very easy to create Python bindings for C and C++ libraries."""
    homepage = "http://www.riverbankcomputing.com/software/sip/intro"
    url      = "http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.5/sip-4.16.5.tar.gz"

    version('4.16.5', '6d01ea966a53e4c7ae5c5e48c40e49e5')

    extends('python')

    def install(self, spec, prefix):
        python('configure.py',
               '--destdir=%s' % site_packages_dir,
               '--bindir=%s' % spec.prefix.bin,
               '--incdir=%s' % python_include_dir,
               '--sipdir=%s' % os.path.join(spec.prefix.share, 'sip'))
        make()
        make('install')
