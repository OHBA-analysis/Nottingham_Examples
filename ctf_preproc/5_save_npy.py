"""Save source reconstructed data as numpy files.

"""

from glob import glob

from osl_dynamics.data import Data

files = sorted(glob("data/src/*/sflip_parc-raw.fif"))
data = Data(
    files,
    picks="misc",
    reject_by_annotation="omit",
    n_jobs=16,
)
data.save("data/npy")
