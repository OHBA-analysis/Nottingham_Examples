"""Sign flipping.

Note, this script is only needed if you're training a dynamic network
model (e.g. the HMM) using the time-delay embedded (TDE) approach.

You can skip this if you're training the HMM on amplitude envelope data
or calculating sign-invariant quantities such as amplitude envelope
correlations or power.
"""

from glob import glob

from osl import source_recon

source_recon.setup_fsl("/path/to/fsl")

SRC_DIR = "data/src"

subjects = []
for path in sorted(glob(SRC_DIR + "/*/parc/parc-raw.fif")):
    subject = path.split("/")[-3]
    subjects.append(subject)

# Find a good template subject to align other subjects to
template = source_recon.find_template_subject(
    SRC_DIR, subjects, n_embeddings=15, standardize=True
)

config = f"""
    source_recon:
    - fix_sign_ambiguity:
        template: {template}
        n_embeddings: 15
        standardize: True
        n_init: 3
        n_iter: 2500
        max_flips: 20
"""

source_recon.run_src_batch(config, SRC_DIR, subjects)
