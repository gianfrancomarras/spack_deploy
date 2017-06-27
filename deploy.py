#!/usr/bin/env python

from spack_utils import *

def main():
    Description = 'Deploy spack'
    parser = default_arg(Description)
    args = parser.parse_args()
    
    main_path = args.dest
    source_cache = args.source_cache
    install_tree = args.install_tree
    install_path_scheme = args.install_path_scheme
    
    
    print(source_cache)
    
    dict_tpl = {"SPACK_install_tree" : install_tree,
               "SPACK_install_path_scheme": install_path_scheme,
               "SPACK_source_cache": source_cache}
    
    
    if not execute([ "git",  "clone",  args.origin, main_path]):
        for _file  in ["config", "modules", "packages"]:
            subst_file(path_join("tpl", "yaml", "{}.yaml.tpl".format(_file)),
                       path_join(main_path, "etc", "spack", "{}.yaml".format(_file)), 
                       dict_tpl)
    else:
        sys.exit(1)



if __name__ == "__main__":
    main()
