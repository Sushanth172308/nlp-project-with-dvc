import logging
from tqdm import tqdm
import random
import xml.etree.ElementTree as ET
import re


def porcess_posts(fd_in,fd_out_train,fd_out_test,target_tag,split):
    line_num =1
    try:
        fd_out =+