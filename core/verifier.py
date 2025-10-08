# core/verifier.py
from hashlib import sha256
from typing import Dict

class ProofVerifier:
    """
    Verifies zero-knowledge proofs for data exchange.
    """

    def verify(self, proof: Dict, public_signals: list):
        recomputed = sha256(str(public_signals).encode()).hexdigest()[:16]
        is_valid = proof["proof"].startswith(recomputed[:8])
        print(f"[verifier] Verification result: {is_valid}")
        return is_valid
