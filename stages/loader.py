import numpy as np
import librosa
from pathlib import Path
from config import LoaderConfig

class AudioLoader:
    def __init__(self, cfg: LoaderConfig):
        self.cfg = cfg

    def load(self, path: str | Path) -> tuple[np.ndarray, int]:
        path = Path(path)
        audio, sr = librosa.load(
            str(path),
            sr=self.cfg.target_sr,
            mono=self.cfg.mono,
            dtype=self.cfg.dtype,
        )
        if self.cfg.normalize_on_load:
            peak = np.max(np.abs(audio))
            if peak > 0:
                audio = audio / peak
        return audio, sr