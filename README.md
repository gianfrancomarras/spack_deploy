# spack_deploy
Scripts and configuration for spack deployment a CINECA

First step: clone this repo:

    git clone  https://github.com/gianfrancomarras/spack_deploy.git <folder name>

    
Then run setup script:

    cd <folder name>
    
    python deploy.py


  * [Deployment hints](https://github.com/RemoteConnectionManager/RCM_spack_deploy/blob/master/DEPLOY_HINTS.md)


  
  Optional arguments:

      -h, --help            show this help message and exit
      --origin ORIGIN       URL of the origin git repo being cloned. (default:
                        https://github.com/LLNL/spack.git)
      --dest DEST           Directory to clone into. If ends in slash, place into
                        that directory; otherwise, place into subdirectory
                        named after the URL (default: /home/gian/Cluster/galil
                        eo/a07smr01/meteo/NEW_SPACK/spack)
      --source_cache SOURCE_CACHE
                        Cache directory (default: $spack/../cache)
      --install_tree INSTALL_TREE
                        Install dir (default: $spack/../install)
      --install_path_scheme INSTALL_PATH_SCHEME
                        Install path scheme (default: ${ARCHITECTURE}/${COMPIL
                        ERNAME}-${COMPILERVER}/${PACKAGE}/${VERSION}/${HASH})
      --naming_scheme NAMING_SCHEME
                        Naming scheme of modules (default:
                        ${PACKAGE}/${VERSION}-${COMPILERNAME}-${COMPILERVER})
