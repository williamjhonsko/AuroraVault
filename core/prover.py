# core/prover.py
from hashlib import sha256
from typing import Dict

class ProofGenerator:
    """
    Generates zk-proofs from given data and circuits.
    """

    def __init__(self, engine):
        self.engine = engine

    def generate_proof(self, payload: Dict):
        witness = self.engine.generate_witness(payload, "vault")
        proof = sha256(witness["witness"].encode()).hexdigest()
        print(f"[prover] Generated proof: {proof[:16]}...")
        return {
            "proof": proof,
            "public_signals": [payload.get("user_id", "0x0"), payload.get("timestamp", 0)],
        }
