# Usage

```python
from flowsense import estimate_discharge

est = estimate_discharge("GRDC-6342100", width_m=142.5, reach_type="meandering",
                         confidence=0.86)
print(est.discharge_m3s)
```

## Validation notebook

`notebooks/validation.ipynb` reproduces the 61-station comparison reported in the
release notes. It expects the `sentinel2-l2a` sample bundle, which is fetched by
`scripts/fetch_samples.py`.
