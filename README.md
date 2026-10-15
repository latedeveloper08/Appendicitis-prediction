# Data

This project uses the **Regensburg Pediatric Appendicitis** dataset: 782 children admitted with abdominal pain to Children's Hospital St. Hedwig, Regensburg, Germany, between 2016 and 2021.

The data is not stored in this repository. The notebook downloads it from the UCI Machine Learning Repository (dataset id 938) with `ucimlrepo` on the first run and saves it here as `appendicitis.csv`.

## Outcomes

| Outcome | Coding used here |
|---|---|
| Diagnosis | 1 = appendicitis, 0 = no appendicitis |
| Severity | 1 = complicated (gangrenous, perforated or abscessed), 0 = uncomplicated or no appendicitis |
| Management | 1 = surgery (primary, secondary or simultaneous), 0 = conservative |

## Licence and citation

Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (non-commercial use with attribution).

Marcinkevičs, R., Reis Wolfertstetter, P., Klimiene, U., Ozkan, E., Chin-Cheong, K., Paschke, A., Zerres, J., Denzinger, M., Niederberger, D., Wellmann, S., Knorr, C. and Vogt, J.E. (2023). Regensburg Pediatric Appendicitis Dataset. Zenodo. https://doi.org/10.5281/zenodo.7669442

Introductory paper: Marcinkevičs et al. (2024). Interpretable and intervenable ultrasonography-based machine learning models for pediatric appendicitis. *Medical Image Analysis*. arXiv:2302.14460
