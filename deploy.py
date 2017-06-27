#!/usr/bin/env python

from spack_utils import *

def main():
    Description = 'Deploy spack'
    parser = default_arg(Description)
    args = parser.parse_args()
    lm_logger = NOTIFY_LOGGER 

    main_path = args.dest
    source_cache = args.source_cache
    install_tree = args.install_tree
    install_path_scheme = args.install_path_scheme
    naming_scheme = args.naming_scheme
    
    dict_tpl = {"SPACK_install_tree" : install_tree,
               "SPACK_install_path_scheme": install_path_scheme,
               "SPACK_source_cache": source_cache,
               "SPACK_naming_scheme": naming_scheme}
    
    
    if not os.path.isdir(main_path):
        if not execute([ "git",  "clone",  args.origin, main_path]):
            for _file  in ["config", "modules", "packages"]:
                subst_file(path_join("tpl", "yaml", "{}.yaml.tpl".format(_file)),
                       path_join(main_path, "etc", "spack", "{}.yaml".format(_file)), 
                       dict_tpl)
        else:
            lm_logger.error("executing git command failed")
            sys.exit(1)
    else:
        lm_logger.error("First remove directory {}!!!".format(main_path))
        sys.exit(1)


if __name__ == "__main__":
    main()