"""Discharge estimation from Sentinel-2 surface reflectance."""

from dataclasses import dataclass

WIDTH_COEFFICIENTS = {
    "braided": 0.42,
    "meandering": 0.31,
    "confined": 0.27,
}


@dataclass
class GaugeEstimate:
    station_id: str
    discharge_m3s: float
    width_m: float
    confidence: float


def estimate_discharge(station_id: str, width_m: float, reach_type: str,
                       confidence: float) -> GaugeEstimate:
    """Estimate discharge from a measured wetted width."""
    coeff = WIDTH_COEFFICIENTS[reach_type]
    return GaugeEstimate(
        station_id=station_id,
        discharge_m3s=round(coeff * width_m ** 1.61, 2),
        width_m=width_m,
        confidence=confidence,
    )
