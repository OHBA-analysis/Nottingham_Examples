# Nottingham Example Scripts

This repository contains example scripts for analysing MEG data collected at Nottingham.

## Installation

To run these scripts you need to install:

- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation) (FMRIB Software Library).
- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html) (or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html)).
- [OSL](https://github.com/OHBA-analysis/osl) (OHBA Software Library).
- [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics) (OSL Dynamics Toolbox) - only needed if you want to train models for dynamics.

### Windows

If you're using a Windows machine, you will need to install the above in [Ubuntu](https://ubuntu.com/wsl) using a Windows subsystem. 

Instructions:

1. Install FSL using the instructions [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/Windows). Make sure you setup XLaunch for the visualisations.

2. Install [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) inside your Ubuntu terminal:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
```

3. Install OSL and osl-dynamics:

```
curl https://raw.githubusercontent.com/OHBA-analysis/osl/main/envs/windows.yml > windows.yml
conda env create -f windows.yml
rm window.yml
```

This will create a conda environment called `osl` which contains both OSL and osl-dynamics.

### HPC Cluster

To install on a high performance computing (HPC) cluster:

1. First load Anaconda:

```
module load Anaconda
```

Note, you need to need to load Anaconda each time you log in (or you can add this line to your `~/.bashrc` file).

2. Install OSL:

```
curl https://raw.githubusercontent.com/OHBA-analysis/osl/main/envs/linux.yml > linux.yml
conda env create -f linux.yml
rm linux.yml
```

This will create a conda environment called `osl`.

3. Install osl-dynamics:

```
conda activate osl
pip install tensorflow==2.9.1
pip isntall tensorflow-probability==0.17
pip install osl-dynamics
```

4. Install FSL using the instructions [here](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation/Linux).

### Test the installation

The following should not raise any errors:

```
conda activate osl
python
>> import osl
>> import osl_dynamics
```

### Get the latest source code (optional)

If you want the very latest code you can clone the GitHub repo. This is only neccessary if you want recent changes to the package that haven't been released yet.

First install OSL/osl-dynamics using the instructions above. Then clone the repo and install locally from source:

```
conda activate osl

git clone https://github.com/OHBA-analysis/osl.git
cd osl
pip install -e .
cd ..

git clone https://github.com/OHBA-analysis/osl-dynamics.git
cd osl-dynamics
pip install -e .
```

After you install from source, you can run the code with local changes. You can update the source code using

```
git pull
```

within the `osl` or `osl-dynamics` directory.

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
