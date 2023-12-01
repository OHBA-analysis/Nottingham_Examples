"""Example script for source reconstructing OPM data.

This include coregistration, beamforming and parcellation.
"""

from osl import source_recon

source_recon.setup_fsl("/path/to/fsl")

PREPROC_DIR = "data/preproc"
SRC_DIR = "data/src"

PREPROC_FILE = PREPROC_DIR + "/sub-{sub:03d}_ses-{ses:03d}_meg/sub-{sub:03d}_ses-{ses:03d}_meg_preproc_raw.fif"
SMRI_FILE = "data/sub-{sub:03d}/mri/sub-{sub:03d}_fixed.nii"

subjects = [1, 2]
sessions = [1, 2, 3]

config = """
    source_recon:
    - compute_surfaces:
        include_nose: False
    - coregister:
        use_nose: False
        use_headshape: True
        already_coregistered: True
    - forward_model:
        model: Single Layer
    - beamform_and_parcellate:
        freq_range: [4, 40]
        chantypes: mag
        rank: {mag: 100}
        parcellation_file: fmri_d100_parcellation_with_PCC_reduced_2mm_ss5mm_ds8mm.nii.gz
        method: spatial_basis
        orthogonalisation: symmetric
"""

preproc_files = []
smri_files = []
for sub in subjects:
    for ses in sessions:
        preproc_files.append(PREPROC_FILE.format(sub=sub, ses=ses))
        smri_files.append(SMRI_FILE.format(sub=sub, ses=ses))

source_recon.run_src_batch(
    config,
    src_dir=SRC_DIR,
    subjects=subjects,
    preproc_files=preproc_fif_files,
    smri_files=smri_files,
)
