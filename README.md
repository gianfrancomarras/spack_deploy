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
                          named after the URL (default:
                          /gpfs/meteo/NEW_SPACK/spack)
    --repo REPO           Add repository (default: cineca)
    --source_cache SOURCE_CACHE
                          Cache directory (default: $spack/../cache)
    --build_dir BUILD_DIR
                          Build directory (default:
                          /gpfs/scratch/usera07smr/a07smr01/build_stage)
    --install_tree INSTALL_TREE
                          Install dir (default: $spack/../install)
    --install_path_scheme INSTALL_PATH_SCHEME
                          Install path scheme (default: ${ARCHITECTURE}/${COMPIL
                          ERNAME}-${COMPILERVER}/${PACKAGE}/${VERSION}/${HASH})
    --naming_scheme NAMING_SCHEME
                          Naming scheme of modules (default:
                          ${PACKAGE}/${VERSION}-${COMPILERNAME}-${COMPILERVER})
    --skip_clone          Skip clone from git (default: False)
