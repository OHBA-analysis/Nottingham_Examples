# OPM Data Preprocessing and Source Reconstruction

In this example, we preprocess and source reconstruct OPM data (in serial - one file at a time).

See `/parallel` for example scripts to preprocess/source reconstruct multiple files in parallel.

## Pipeline

- `01_create_fif.py`: Puts the OPM data into fif format (which is needed for OSL).
- `02_preprocess.py`: Preprocesses the data. This includes filtering, downsampling and automated artefact removal.
- `03_source_reconstruct.py`: Coregister, beamform and parcellate the data.
