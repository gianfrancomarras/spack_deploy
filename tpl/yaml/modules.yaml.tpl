# -------------------------------------------------------------------------
# This is the default configuration for Spack's module file generation.
#
# Settings here are versioned with Spack and are intended to provide
# sensible defaults out of the box. Spack maintainers should edit this
# file to keep it current.
#
# Users can override these settings by editing the following files.
#
# Per-spack-instance settings (overrides defaults):
#   $SPACK_ROOT/etc/spack/modules.yaml
#
# Per-user settings (overrides default and site settings):
#   ~/.spack/modules.yaml
# -------------------------------------------------------------------------
modules:
  enable:
    - tcl
  tcl:
    blacklist: ['hpc-cineca']
    hash_length: 2
    all:
      environment:
        set:
          '${PACKAGE}_HOME': '${PREFIX}'
    naming_scheme:  '${SPACK_naming_scheme}'
    
  prefix_inspections:
    bin:
      - PATH
    man:
      - MANPATH
    share/man:
      - MANPATH
    share/aclocal:
      - ACLOCAL_PATH
    lib:
      - LIBRARY_PATH
      - LD_LIBRARY_PATH
    lib64:
      - LIBRARY_PATH
      - LD_LIBRARY_PATH
    include:
      - CPATH
    lib/pkgconfig:
      - PKG_CONFIG_PATH
    lib64/pkgconfig:
      - PKG_CONFIG_PATH
    '':
      - CMAKE_PREFIX_PATH
