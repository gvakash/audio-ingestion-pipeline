from dataclasses import dataclass, field

@dataclass
class LoaderConfig:
    target_sr: int = 16_000          # resample target sample rate
    mono: bool = True                # collapse to mono
    dtype: str = "float32"           # float32 | int16 | float64
    normalize_on_load: bool = False  # peak-normalize during decode

