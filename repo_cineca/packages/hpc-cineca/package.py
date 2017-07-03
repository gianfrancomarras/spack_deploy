##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install hpc-cineca
#
# You can edit this file again by typing:
#
#     spack edit hpc-cineca
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class HpcCineca(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.cineca.it"
    url      = "http://www.example.com/example-1.2.3.tar.gz"


    version('0.1')

    variant('python', default=True, description='Enables python')
    depends_on('python', when='+python')
    
    variant('py-numpy', default=True,  description='Enables py-numpy')
    depends_on('py-numpy' , when='+py-numpy')
    
    variant('cmake', default=True,  description='Enables cmake')
    depends_on('cmake' , when='+cmake')
        
    #variant('ncview', default=True,  description='Enables ncview')
    #depends_on('ncview' , when='+ncview')

    variant('valgrind', default=True,  description='Enables valgrind')
    depends_on('valgrind' , when='+valgrind')
    
    #variant('nco', default=True,  description='Enables nco')
    #depends_on('nco' , when='+nco')
    
    variant('bzip2', default=True,  description='Enables bzip2')
    depends_on('bzip2' , when='+bzip2')
    
    
    variant('zlib', default=True,  description='Enables zlib')
    depends_on('zlib' , when='+zlib')    
    
    variant('szip', default=True,  description='Enables szip')
    depends_on('szip' , when='+szip')
    
    variant('gnuplot', default=True,  description='Enables gnuplot')
    depends_on('gnuplot' , when='+gnuplot')
    
    


