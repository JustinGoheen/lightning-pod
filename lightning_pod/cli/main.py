import os
import click
import shutil
from pathlib import Path


PROJECTPATH = os.getcwd()
LIBPATH = Path(__file__).parents[1]
SEEDPATH = os.path.join(LIBPATH, "seed")


@click.group()
def main():
    pass


@main.command("seed")
def seed():
    shutil.copytree(SEEDPATH, PROJECTPATH)
    return


@main.group("project")
def project():
    pass


# TODO add help description
@project.command("teardown")
def teardown():
    target_dirs = [
        os.path.join(PROJECTPATH, "models", "checkpoints"),
        os.path.join(PROJECTPATH, "models", "production"),
        os.path.join(PROJECTPATH, "logs", "lightning_logs"),
        os.path.join(PROJECTPATH, "logs", "profiler"),
        os.path.join(PROJECTPATH, "data", "cache"),
        os.path.join(PROJECTPATH, "data", "predictions"),
        os.path.join(PROJECTPATH, "data", "training_split"),
        os.path.join(PROJECTPATH, "docs"),
    ]

    for dir in target_dirs:
        for target in os.listdir(dir):
            targetpath = os.path.join(PROJECTPATH, dir, target)
            if not os.path.isdir(targetpath):
                os.remove(targetpath)
            else:  ## for checkpoint version directories
                dirpath = os.path.join(PROJECTPATH, dir, target)
                shutil.rmtree(dirpath)
    return


# TODO add help description
@project.command("build")
def build():
    make_new()
    return


@main.group("trainer")
def trainer():
    pass


# TODO add help description
@trainer.command("config-help")
def config_help():
    trainer = os.path.join("lightning_pod", "agents", "trainer.py")
    os.system(f"python {trainer} --help")
    return


# TODO add help description
@trainer.command("run")
@click.argument("hydra-args", nargs=-1)
def run_trainer(hydra_args):
    trainer = os.path.join("lightning_pod", "agents", "trainer.py")
    hydra_args = list(hydra_args)
    hydra_args = [f"'trainer.{i}'" for i in hydra_args]
    hydra_args = " ".join(hydra_args)
    run_command = " ".join(["python", trainer, hydra_args])
    os.system(run_command)
    return
