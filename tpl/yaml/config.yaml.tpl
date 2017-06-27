# -------------------------------------------------------------------------
# This is the default spack configuration file.
#
# Settings here are versioned with Spack and are intended to provide
# sensible defaults out of the box. Spack maintainers should edit this
# file to keep it current.
#
# Users can override these settings by editing the following files.
#
# Per-spack-instance settings (overrides defaults):
#   $SPACK_ROOT/etc/spack/config.yaml
#
# Per-user settings (overrides default and site settings):
#   ~/.spack/config.yaml
# -------------------------------------------------------------------------
config:
  # This is the path to the root of the Spack install tree.
  # You can use $spack here to refer to the root of the spack instance.
  install_tree: ${SPACK_install_tree}  
  install_path_scheme: '${SPACK_install_path_scheme}'


  # Locations where different types of modules should be installed.
  module_roots:
    tcl:    $spack/share/spack/modules
    lmod:   $spack/share/spack/lmod
    dotkit: $spack/share/spack/dotkit


  # Temporary locations Spack can try to use for builds.
  #
  # Spack will use the first one it finds that exists and is writable.
  # You can use $tempdir to refer to the system default temp directory
  # (as returned by tempfile.gettempdir()).
  #
  # A value of $spack/var/spack/stage indicates that Spack should run
  # builds directly inside its install directory without staging them in
  # temporary space.
  #
  # The build stage can be purged with `spack purge --stage`.
  build_stage:
    - /dev/shm/$user
    - /scratch_local/$user
    - $tempdir


  # Cache directory already downloaded source tarballs and archived
  # repositories. This can be purged with `spack purge --downloads`.
  source_cache: ${SPACK_source_cache}


  # Cache directory for miscellaneous files, like the package index.
  # This can be purged with `spack purge --misc-cache`
  misc_cache: ~/.spack/cache


  # If this is false, tools like curl that use SSL will not verify
  # certifiates. (e.g., curl will use use the -k option)
  verify_ssl: true


  # If set to true, Spack will always check checksums after downloading
  # archives. If false, Spack skips the checksum step.
  checksum: true


  # If set to true, `spack install` and friends will NOT clean
  # potentially harmful variables from the build environment. Use wisely.
  dirty: false


  # The default number of jobs to use when running `make` in parallel.
  # If set to 4, for example, `spack install` will run `make -j4`.
  # If not set, all available cores are used by default.
  # build_jobs: 4