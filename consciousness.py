import numpy as np
from scipy.fft import rfft, rfftfreq

class ConsciousnessCoupling:
    def __init__(self, sampling_rate: int = 256):
        self.sampling_rate = sampling_rate
        self.alpha = 0.5  # Coupling constant

    def extract_40hz_gamma(self, eeg_data: np.ndarray) -> float:
        """
        Extracts 40Hz gamma oscillation amplitude from EEG data.
        """
        fft_vals = np.asarray(rfft(eeg_data))
        freqs = rfftfreq(len(eeg_data), 1/self.sampling_rate)
        gamma_indices = np.where((freqs >= 38) & (freqs <= 42))[0]
        gamma_band = np.abs(fft_vals[gamma_indices])
        return np.max(gamma_band) if gamma_band.size > 0 else 0.0

    def stress_tensor(self, gamma_amp: float, lambda_C: float = 1e-12) -> float:
        """
        Computes consciousness-driven stress-energy tensor.
        Equation: T_μν^(cog) ≈ αφ^2
        """
        phi = gamma_amp * lambda_C
        return self.alpha * phi**2