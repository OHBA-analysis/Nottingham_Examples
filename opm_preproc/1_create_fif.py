"""Create fif files from OPM recordings in MATLAB format.

"""

import os

from osl.utils import opm

# Subjects and sessions to do
subjects = [1, 2]
sessions = [1, 2, 3]

# Output directory to save fif files to
raw_dir = "data/raw"
os.makedirs(raw_dir, exist_ok=True)

for sub in subjects:
    for ses in sessions:
        # Input files
        mat_file = f"data/sub-{sub:03d}/ses-{ses:03d}/sub-{sub:03d}_ses-{ses:03d}_meg.mat"
        smri_file = f"data/sub-{sub:03d}/mri/sub-{sub:03d}.nii"
        fixed_smri_file = f"data/sub-{sub:03d}/mri/sub-{sub:03d}_fixed.nii"
        tsv_file = f"data/sub-{sub:03d}/ses-{ses:03d}/sub-{sub:03d}_ses-{ses:03d}_channels.tsv"

        # Output fif file
        fif_file = f"{raw_dir}/sub-{sub:03d}_ses-{ses:03d}_meg.fif"

        # Create fif file
        if os.path.exists(mat_file) and os.path.exists(smri_file):
            opm.convert_notts(
                mat_file,
                smri_file,
                tsv_file,
                fif_file,
                smri_fixed_file,
            )
        else:
            print(f"subject {sub}, session {ses} is missing files")
