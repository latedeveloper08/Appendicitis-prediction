"""Loading and preparing the Regensburg Pediatric Appendicitis data."""

from pathlib import Path

import numpy as np
import pandas as pd

UCI_ID = 938

TARGETS = ["Diagnosis", "Severity", "Management"]

# Columns that are not used as model inputs, and why
EXCLUDED = {
    "Diagnosis_Presumptive": "the doctor's suspected diagnosis, close to the answer itself",
    "Length_of_Stay": "only known after treatment (surgical patients stay longer)",
    "US_Number": "an ultrasound image ID, not a clinical measurement",
}

CLINICAL_SCORES = ["Alvarado_Score", "Paedriatic_Appendicitis_Score"]


def load_raw(path: str | Path) -> pd.DataFrame:
    """Read the local copy of the data, downloading it from UCI the first time."""
    path = Path(path)
    if not path.exists():
        from ucimlrepo import fetch_ucirepo

        path.parent.mkdir(parents=True, exist_ok=True)
        fetch_ucirepo(id=UCI_ID).data.original.to_csv(path, index=False)
    return pd.read_csv(path)


def make_targets(df: pd.DataFrame) -> pd.DataFrame:
    """Return the three outcomes as 0/1 columns (NaN where the label is missing).

    - Diagnosis: 1 = appendicitis
    - Severity: 1 = complicated (gangrenous, perforated or abscessed)
    - Management: 1 = surgery (primary, secondary or simultaneous), 0 = conservative
    """
    out = pd.DataFrame(index=df.index)
    out["Diagnosis"] = df["Diagnosis"].map({"appendicitis": 1, "no appendicitis": 0})
    out["Severity"] = df["Severity"].map({"complicated": 1, "uncomplicated": 0})
    surgical = {"primary surgical", "secondary surgical", "simultaneous appendectomy"}
    out["Management"] = df["Management"].map(lambda v: np.nan if pd.isna(v) else float(v in surgical))
    return out


def feature_table(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str], list[str]]:
    """Return the model inputs plus the lists of numeric and categorical columns."""
    X = df.drop(columns=[*TARGETS, *EXCLUDED])
    numeric = [c for c in X.columns if pd.api.types.is_numeric_dtype(X[c])]
    categorical = [c for c in X.columns if c not in numeric]
    X[categorical] = X[categorical].astype(object)
    return X, numeric, categorical
