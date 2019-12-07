import sys
sys.path.append("..")
from common.config import merge,args_wrapper_parser,args_wrapper_path
import os
import argparse

param = {'env': 'airCombateEnv', 'algs': 'dqn', 'memory': 'memory'}  # memory不用的时候value为None即可
args_origin = merge(param)
args_after_parse = args_wrapper_parser(args_origin)
args = args_wrapper_path(args_after_parse)