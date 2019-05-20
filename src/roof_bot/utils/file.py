# -*- coding: utf-8 -*-

from pathlib import Path
import yaml


def yaml_load(filename, storage="local" ):
    if storage == "local":
        try:
            file = Path(filename)
            with file.open(mode='r') as fp:
                return yaml.safe_load(fp)
        except yaml.YAMLError as err:
            print(err)
    else:
        raise NotImplementedError()
