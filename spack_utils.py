#!/usr/bin/env python

import os, sys
import argparse
import logging
import subprocess
import select
from string import Template

REPORT_FORMAT = "%Y%m%d-%H:%M:%S"
path_join = os.path.join

def default_arg(descr):
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=descr,
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
    parser.add_argument('--origin', action = 'store',
                         help='URL of the origin git repo being cloned.',
                         default='https://github.com/LLNL/spack.git')
        
    parser.add_argument('--dest', #default=argparse.SUPPRESS,
                        help="Directory to clone into.  If ends in slash, place into that directory; otherwise, place into subdirectory named after the URL",
                        default=path_join(os.getcwd(), "spack"))
    
    parser.add_argument('--repo', #default=argparse.SUPPRESS,
                        help="Add repository",
                        default="cineca"))
        
    parser.add_argument('--source_cache', action = 'store',
                         help='Cache directory',
                         default='$spack/../cache')
    
    parser.add_argument('--install_tree', action = 'store',
                         help='Install dir',
                         default='$spack/../install')
    
    parser.add_argument('--install_path_scheme', action = 'store',
                         help='Install path scheme',
                         default='${ARCHITECTURE}/${COMPILERNAME}-${COMPILERVER}/${PACKAGE}/${VERSION}/${HASH}')
    
    parser.add_argument('--naming_scheme', action = 'store',
                         help='Naming scheme of modules',
                         default='${PACKAGE}/${VERSION}-${COMPILERNAME}-${COMPILERVER}')
    
    
    return parser


class Process(object):
    def __init__(self, command_args):
        self.command_args = command_args
        self.returncode = None

    def run_command(self, std_out = None, std_err = None):
        
        if std_out == None:
            std_out = subprocess.PIPE
        if std_err == None:
            std_err = subprocess.PIPE
            
        process = subprocess.Popen(self.command_args,
                                   stdout=std_out,
                                   stderr=std_err)

        self.returncode = process.returncode
        return process
    
    
def call_and_log(
		command_args,
		exe_output=None,
		write_out=None,
		write_err=None,
		transform_out=None,
		transform_err=None,
		active_line=False
    ):
    if write_out is None:
        write_out = sys.stdout.write
    if write_err is None:
        write_err = sys.stderr.write
    if transform_out is None:
        transform_out = lambda x: '{0}\n'.format(x)
    if transform_err is None:
        transform_err = lambda x: 'X|{0}\n'.format(x)

    process = Process(command_args)
    
    my_process = process.run_command(std_out = exe_output)
        
    logfn = {my_process.stdout: write_out,
             my_process.stderr: write_err}    
    
    lines = []

    def check_io():
        ready_to_read = select.select([my_process.stdout, my_process.stderr], [], [])[0]
        for io in ready_to_read:
            line = str(io.readline()).rstrip("\n")
            if line:
                if active_line and io == my_process.stdout:
                    lines.append(line)
                if io == my_process.stdout:
                    line = transform_out(line)
                if io == my_process.stderr:
                    line = transform_err(line)
                logfn[io](line)

    if exe_output is not None:
        while my_process.poll() is None:
            for line in my_process.stderr:
                print("X|{}".format(line))
    else:
        while my_process.poll() is None:
            check_io()
        check_io()

    returncode = my_process.returncode

    return returncode, lines

def execute(command_line, exe_output = None, activeline = False):
    lm_logger = NOTIFY_LOGGER       
    str_command_line = ' '.join(command_line)
    lm_logger.info("executing: {0}".format(str_command_line))

    output = None
    if exe_output is not None:
        output = io.open(exe_output, "wb")
            
    returncode, lines = call_and_log(command_line, exe_output = output)
    if returncode:
        lm_logger.info("(KO) <<< : {0}".format(str_command_line))
    else:
        lm_logger.info("(OK) <<< : {0}".format(str_command_line))
    return returncode


def mkdir(workdir):
    lm_logger = NOTIFY_LOGGER       
    if not os.path.isdir(workdir):
        lm_logger.info("mkdir {0} (RUN...)".format(workdir))
        os.makedirs(workdir)
        lm_logger.info("(OK) <<< mkdir {0}".format(workdir))
    return 0


def create_formatter():
    return logging.Formatter('%(asctime)s: %(name)s: %(levelname) -4s: %(message)s', datefmt=REPORT_FORMAT)

def create_base_loggers():
    root_logger = logging.getLogger("SPACK")
    root_handler = logging.StreamHandler()
    root_handler.setLevel(logging.INFO)
    root_handler.setFormatter(create_formatter())
    root_logger.addHandler(root_handler)
    root_logger.setLevel(logging.DEBUG)
    root_logger.propagate = False
    
    notify_logger = root_logger.getChild("HPC")
    notify_logger.propagate = False
    notify_handler = logging.StreamHandler()
    notify_handler.setLevel(2)
    notify_handler.setFormatter(create_formatter())
    notify_logger.addHandler(notify_handler)
    notify_logger.setLevel(logging.DEBUG)
    return root_handler, root_logger, notify_handler, notify_logger

ROOT_HANDLER, ROOT_LOGGER, NOTIFY_HANDLER, NOTIFY_LOGGER = create_base_loggers()


def subst_file(source_filename, target_filename, dct):
    """ Create file from to template file """    
    lm_logger = NOTIFY_LOGGER
    print(dct)
    lm_logger.info("substituting template {0} -> {1} (RUN...)".format(source_filename, target_filename))
    dirname = os.path.abspath(os.path.dirname(target_filename))
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

    if os.path.isfile(source_filename):
        with open(source_filename, 'r') as source_file, open(target_filename, 'a') as target_file:
            source = Template(source_file.read())
            try:
                target = source.safe_substitute(dct)
                target_file.write(target)
                lm_logger.info("(OK) <<< substituting template {0} -> {1}".format(source_filename, target_filename))
                return 0
            except KeyError:
                lm_logger.info("(KO) <<< substituting template {0} -> {1}".format(source_filename, target_filename))
                return 1
    else:
        lm_logger.warning("(KO) <<< substituting template: file source {0} not found!".format(source_filename))
        return 1
