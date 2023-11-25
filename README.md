# Nottingham Example Scripts

This repository contains example scripts for analysing MEG data.

## Installation

To run these scripts you need to install OSL and osl-dynamics:

1. First install or load Anaconda. On most computing clusters you can do:

```
module load Anaconda
```

2. Install OSL (OHBA Software Library):

```
curl https://raw.githubusercontent.com/OHBA-analysis/Nottingham_CTF_Examples/main/osl-env.yml > osl-env.yml
conda env create -f osl-env.yml
rm osl-env.yml
```

3. Test the installation:

```
conda activate osl
python
>> import osl
>> import osl_dynamics
```

This should not raise any errors.

## Common Issues

If you get a `conda init` error when you try to activate the environment when running a job on a cluster you can use the following to activate the environment then replace:
```
conda activate osl
```
with 
```
source activate osl
```
