# coding=utf-8
import time

import requests
import yaml
import os
from bs4 import BeautifulSoup
from xlrd import open_workbook


class YamlReader:

    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在!')
        self._data = None

    @property
    def data(self):
        pass















































