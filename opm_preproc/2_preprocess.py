"""Example script for source reconstructing OPM data.

"""

from glob import glob

from osl import preprocessing

raw_dir = "data/raw"
preproc_dir = "data/preproc"

# Preprocessing steps to apply
config = """
    preproc:
    - crop: {tmin: 20}
    - resample: {sfreq: 150}
    - filter: {l_freq: 4, h_freq: 40, method: iir, iir_params: {order: 5, ftype: butter}}
    - bad_channels: {picks: meg, significance_level: 0.4}        
    - bad_segments: {segment_len: 300, picks: meg, significance_level: 0.1}
"""

# Input files (use all fif files in raw_dir)
fif_files = sorted(glob(f"{raw_dir}/*.fif"))

# Do preprocessing
dataset = preprocessing.run_proc_batch(
    config,
    fif_files,
    outdir=preproc_dir,
    overwrite=True,
)
