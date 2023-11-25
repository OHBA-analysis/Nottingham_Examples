# CTF Data Example

Parallel processing (preprocessing and source reconstruction) of CTF data.

## Dataset

We use the public CTF data from the Nottingham in the MEGUK Partnership dataset: [https://meguk.ac.uk/database/](https://meguk.ac.uk/database/).

We use the resting-state (eyes open) data. These example scripts expect the data to be in the original directory structure in the public dataset:

```
data
|-- raw
    |-- Nottingham
        |-- sub-not001
            |-- meg
                |-- sub-not001_task-resteyesopen_meg.ds
                |-- ...
            |-- anat
                |-- sub-not001_T1w.nii.gz
                |-- ...
        |-- sub-not002
        |-- ...
```

## Pipeline

In this example we:

- `1_preprocess.py`: Preprocess the sensor-level data. This includes standard signal processing such as downsampling and filtering as well as artefact removal.
- `2_fix_smri_files.py`: Here, we fix a technical issue related to the format of how the structral MRI was save. This is specific to the MRC MEGUK dataset.
- `3_source_reconstruct.py`: Here, we coregister the MEG data and structural MRI, beamform the sensor-level data and parcellate to give us the source-level data. We use the AAL parcellation.
- `4_sign_flip.py`: Here, we fix the dipole sign ambiguity (we align the sign of the parcel time courses across subjects). This is only needed if we're training a group-level model on time-delay emebdded data.
- `5_save_npy.py`: Save the source data as vanilla numpy files in (time, parcels) format.

Note, there is a variable called `n_workers` (or `n_jobs`) in these scripts that should be set to the number of cores you would like to use.