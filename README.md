# Lightning Pod

This package is a placeholder for the currect project linked as the homepage. Installing with pip will only install an empty package with no functionality.

## Overview

This project is a template Python environment, tooling, and system architecture for [Lightning OS](https://www.pytorchlightning.ai/) that culminates with a Plotly Dash [UI](https://01g6bdbc5e55wc5ffgj11gtkxj.litng-ai-03.litng.ai/view/home) deployed to the Lightning platform.

### Using the Template

The intent is that users [create a new repo from the template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) in GitHub's web interface and then clone the newly created repo in their personal account to their local machine.

#### Prepping for Use
A [CLI](https://github.com/JustinGoheen/lightning-pod/blob/main/lightning_pod/cli/pod.py) `pod` has been provided to assist with basic tasks.


`pod project teardown` will destroy the example data splits, saved predictions, logs, profilers, checkpoints, and onnx. <br>
`pod trainer run` runs the provided example, default trainer. <br>
`pod project seed` executes teardown, moves example code provided in `lightning_pod/agents` to a new directory `examples` in the project root directory, and then creates a new `trainer.py` `trainer_config.yaml` and `module.py` in `lightning_pod/agents`.

The flow for creating new checkpoints and a new ONNX model looks like (assumes conda environment manager):

```sh
cd {{ path to clone }}
conda env create --file environment.yml
conda activate lightning-os
pip install lightning
pip install -e .
pod project teardown
pod trainer run
```

> miniconda (on macOS) is not installing lighting from the provided environment.yml; which is why the above shows a call to `pip install` after activating the `lightning-os` conda environment

#### Full Tear Down
The CLI command `pod project seed` will remove all example `lightning_pod/agents` code and cached MNIST files in `data` in order to allow users to begin their own projects:

```sh
pod project seed
```

The example code will be preserved in a new directory `examples` after running the above. This `examples` directory can safely be deleted if it is not needed.

Files removed:

- cached MNIST data
- training splits
- saved predictions
- PyTorch Profiler and TensorBoard logs
- model checkpoints
- persisted ONNX model 


## Viewing the Lightning Dash UI Locally

Once the repo has been cloned, the app can be viewed locally by running the following in terminal:

```sh
lightning run app app.py
```

> the UI cannot be viewed if the provided checkpoints have been deleted, or if a new training run has not been completed
 
> the provided UI is only suitable for image processing problems; however, the example Dash code and `assets/styles/css.styles` are written in a manner that the code can serve as a reference for creating new graphs, bootstrap components, and dash callbacks.

## Deploying to Lightning Cloud

Deploying finished applications to Lightning is simple. If you haven't done so, create an account on [Lightning.ai](https://www.pytorchlightning.ai/). Once an account has been created, one needs only to add an additional flag to `lightning run` as shown below:

```sh
lightning run app app.py --cloud
```

This will load the app to your account, build services, and then run the app on Lightning's platform. An `Open App` button will be shown in the Lightning Web UI when your app is ready to be launched and viewed in the browser.

> the requisite .lightning and .lightningignore files are located in [`.lightningos/.lightningai`](https://github.com/JustinGoheen/lightning-pod/tree/main/.lightningos/.lightningai). 

The name of the app loaded to Lightning can be changed in the [`.lightningos/.lightningai/.lightning`](https://github.com/JustinGoheen/lightning-pod/tree/main/.lightningos/.lightningai/.lightning) file or with

```sh
lightning run app app.py --cloud --name="what ever name you choose"
```

## Skills

### Software Engineering

The Lightning team has created a series of [Engineering for Researchers](https://www.pytorchlightning.ai/edu/engineering-class) videos to help individuals become familiar with software engineering best practices.

### Deep Learning

For software engineers in need of deep learning know-how, NYU's Alfredo Canziani has created a [YouTube Series](https://www.youtube.com/playlist?list=PLLHTzKZzVU9e6xUfG10TkTWApKSZCzuBI) for his lectures on deep learning. Additionally, Professor Canziani was kind enough to make his course materials public [on GitHub](https://github.com/Atcold/NYU-DLSP21).

##3 Additional Resources

Aside from the above, I've started a [wiki](https://justingoheen.github.io/lightning-engineer/) to help guide individuals through some of the concepts and tooling discussed in this document.

## Tooling

The tooling i.e. the dependencies, or stack, was selected by referring to the Lightning ecosystem repos: PyTorch Lightning, Lightning Flash, torchmetrics etc. Tooling not used by the Lightning team is also used, and is described below briefly, and in the wiki in greater detail.

### Lightning Stack

The lightning team typically uses DeepSource, CircleCI, GitHub Actions, and Azure Pipelines for top level CI/CD management. At a deeper level, the team uses PyTest + coverage + CodeCov for unit testing, mypy for type checking, flake8 + Black for linting and formatting, pre-commit to for git commit QA, and mergify for automating PR merges which pass all CI/CD checks.

Azure Pipelines, pre-commit, and mergify are not used in this project repo.

### Extras

This repo uses a GitHub Action for GitHub CodeQL security analysis; this action is the default action set by GitHub when enabling [code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) for any repo.

## Cloud Development

Lightning Pod enables collaborative development with Gitpod and GitHub CodeSpaces. Please note that these tools have only been tested on creating and training a custom LightningModule i.e. it is necessary to debug Lightning and Dash apps locally. Lastly, GitHub CodeSpaces is still in beta for individual pro accounts. Gitpod offers 50 free hours per month. Support for [Grid Sessions](https://docs.grid.ai/features/sessions) is planned.

<div align="center">

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new?repo=JustinGoheen/lightning-pod)

</div>

Gitpod and CodeSpaces uses pyenv instead of conda ... meaning the terminal commands to use the CLI's are slightly different.

Once the workspace image has finished building, do the following to teardown the example and run a trainer of your own from the provided example LightningModule:

```sh
pod teardown
pod trainer run
```

If using VS Code (in browser or on desktop), it is possible to view PyTorch Profiler and TensorBoard logs when using Gitpod or CodeSpaces. Access the VS Code command palette and enter `>Python: Launch TensorBoard`. A new port will start; TensorBoard will launch once the new port is active. If the TensorBoard window remains blank, close it and restart the TensorBoard session.

## Getting Help

Please join the [Lightning Community Slack](https://join.slack.com/t/pytorch-lightning/shared_invite/zt-19m2xnz2o-hC80K2vGCoGCpP4vTh6T1g) for questions about the Lightning ecosystem. Feel free to @ me in Slack if you have a question specific to this repo.

## Contributing

There is no need to submit an issue or PR to this repo. This template is exactly that – a template for others to fork or clone and improve on, and share with the community. My hopes in sharing this template is that new to ML students or PhD researchers in any domain can quickly form a project from trustworthy boilerplate.