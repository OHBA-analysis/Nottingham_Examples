# Nottingham Example Scripts

This repository contains example scripts for analysing MEG data collected at Nottingham.

## Installation

To run these scripts you need to install:

- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html)).
- [OSL](https://github.com/OHBA-analysis/osl) (OHBA Software Library).
- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation) (FMRIB Software Library) - only needed if you want to do source reconstruction with OSL.
- [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics) (OSL Dynamics Toolbox) - only needed if you want to train models for dynamics.

### Windows

If you're using a Windows machine, you will need to install the above in [Ubuntu](https://ubuntu.com/wsl) using a Windows subsystem.

Instructions:

1. First install Ubuntu using the instructions [here](https://ubuntu.com/wsl).

2. In Ubuntu, install Miniconda using the Linux installer instructions [here](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

3. Install OSL and osl-dynamics:

```
curl https://raw.githubusercontent.com/OHBA-analysis/Nottingham_Examples/main/osl-env.yml > osl-env.yml
conda env create -f osl-env.yml
rm osl-env.yml
```

This will create a conda environment called `osl` which contains both OSL and osl-dynamics.

4. Install FSL using the instructions [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation).

### HPC Cluster

To install on a high performance computing (HPC) cluster:

1. First load Anaconda:

```
module load Anaconda
```

Note, you need to need to load Anaconda each time you log in (or you can add this line to your `~/.bashrc` file).

2. Install OSL and osl-dynamics:

```
curl https://raw.githubusercontent.com/OHBA-analysis/Nottingham_Examples/main/osl-env.yml > osl-env.yml
conda env create -f osl-env.yml
rm osl-env.yml
```

This will create a conda environment called `osl` which contains both OSL and osl-dynamics.

3. Install FSL using the instructions [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation).

### Test the installation

The following should not raise any errors:

```
conda activate osl
python
>> import osl
>> import osl_dynamics
```

## Loading the packages

To use OSL/osl-dynamics you need to activate the conda environment:

```
conda activate osl
```

**You need to do every time you open a new terminal.** You know if the `osl` environment is activated if it says `(osl)[...]` at the start of your terminal command line.

Note, if you get a `conda init` error when activating the `osl` environment during a job on an HPC cluster, you can resolve this by replacing
```
conda activate osl
```
with 
```
source activate osl
```

## Getting help

You can email chetan.gohil@psych.ox.ac.uk if you run into errors, need help or spot any typos.
