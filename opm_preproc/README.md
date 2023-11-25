# OPM Data Example

Parallel processing (preprocessing and source reconstruction) of OPM data.

## Pipeline

- `1_create_fif.py`: Puts the OPM data into fif format (which is needed for OSL).
- `2_preprocess.py`: Preprocesses the data. This includes filtering, downsampling and automated artefact removal.
- `3_source_reconstruct.py`: Coregister, beamform and parcellate the data.
- `4_sign_flip.py`: Sign flipping to fix the dipole sign ambiguity.
