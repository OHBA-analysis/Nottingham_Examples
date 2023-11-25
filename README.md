# Nottingham Example Scripts

This repository contains example scripts for analysing MEG data collected at Nottingham.

## Installation

To run these scripts you need to install [OSL](https://github.com/OHBA-analysis/osl) and [osl-dynamics](https://github.com/OHBA-analysis/osl-dynamics):

1. First install or load Anaconda. On most computing clusters you can do:

```
module load Anaconda
```

Note, if you're using a computing cluster you need to need to load Anaconda each time you log in.

If you've installed Anaconda on a normal computer, you don't need to do `module load`.

2. Install OSL (OHBA Software Library) and osl-dynamics (OSL Dynamics Toolbox):

```
curl https://raw.githubusercontent.com/OHBA-analysis/Nottingham_Examples/main/osl-env.yml > osl-env.yml
conda env create -f osl-env.yml
rm osl-env.yml
```

This will create a conda environment called `osl` which contains both OSL and osl-dynamics.

3. Test the installation:

```
conda activate osl
python
>> import osl
>> import osl_dynamics
```

This should not raise any errors.

## Loading the packages

To use OSL/osl-dynamics you need to activate the conda environment:

```
conda activate osl
```

**You need to do every time you open a new terminal.** You know if the `osl` environment is activated if it says `(osl)[...]` at the start of your terminal command line.

Note, if you get a `conda init` error when you try to activate the environment when running a job on a cluster you can use the following to activate the environment then replace:
```
conda activate osl
```
with 
```
source activate osl
```

## Getting help

You can email chetan.gohil@psych.ox.ac.uk if you run into errors, need help or spot any typos.
