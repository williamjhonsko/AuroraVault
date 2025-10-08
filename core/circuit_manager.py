# core/circuit_manager.py
import os
from pathlib import Path

class CircuitManager:
    """
    Handles Circom circuits: registration, metadata, and on-demand compilation.
    """

    def __init__(self, base_dir: str = "data/circuits"):
        self.base_dir = Path(base_dir)
        self.registry = {}

    def register_circuit(self, name: str, description: str):
        path = self.base_dir / f"{name}.circom"
        if not path.exists():
            raise FileNotFoundError(f"Circuit file not found: {path}")
        self.registry[name] = {"path": str(path), "description": description}
        print(f"[circuit_manager] Registered circuit {name}")

    def list_circuits(self):
        return list(self.registry.keys())

    def compile_all(self):
        for name in self.registry:
            print(f"[circuit_manager] Compiling {name} ...")
