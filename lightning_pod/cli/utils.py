import os
import shutil
import errno
from pathlib import Path

PROJECTPATH = os.getcwd()
FILEPATH = Path(__file__)
SEEDPATH = FILEPATH.parents[1]


def _preserve_dir(main_source_dir: str, sub_source_dir: str, destination: str):
    destinationpath = os.path.join(PROJECTPATH, destination)
    if not os.path.isdir(destinationpath):
        os.mkdir(destinationpath)
    src = os.path.join(PROJECTPATH, main_source_dir, sub_source_dir)
    dest = os.path.join(PROJECTPATH, destinationpath)
    shutil.copy(src, dest)


def preserve_previous_run(preserve_previous_run: bool):
    _preserve_dir("lightning_pod", "agents", "examples", preserve_previous_run)
    _preserve_dir("lightning_pod", "pipeline", "examples", preserve_previous_run)


def _clean_and_build_lightning_pod(module_to_copy):
    src = os.path.join(SEEDPATH, module_to_copy)
    dest = os.path.join(PROJECTPATH, "network", module_to_copy)
    shutil.copy(src, dest)


def rebuild_network():
    _clean_and_build_lightning_pod("agents")
    _clean_and_build_lightning_pod("pipeline", preserve_previous_run)


def set_project_name():
    return os.getcwd()


def create_target_path(filepath, target_directory):
    sep = os.path.sep
    real_path = os.path.realpath(filepath).split(sep)
    real_path = list(reversed(real_path))
    if target_directory in real_path:
        target_path_idx = real_path.index(target_directory) - 1
        target_path = filepath.parents[target_path_idx]
        return target_path
    else:
        raise NotADirectoryError(
            errno.ENOENT, os.strerror(errno.ENOENT), target_directory
        )
