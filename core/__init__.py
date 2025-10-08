# core/__init__.py
"""
AuroraVault Core Engine
Low-level cryptographic primitives, proof lifecycle, and circuit orchestration.
"""
from .zk_engine import ZkEngine
from .encryptor import DataEncryptor
from .prover import ProofGenerator
from .verifier import ProofVerifier
from .circuit_manager import CircuitManager
