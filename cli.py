"""
Command-line interface for TSNN-P Lab.

Provides a simple CLI for interacting with the TSNN-P system.
"""

import argparse
import sys
from typing import Dict, Any

from .core import SystemArchitecture


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="TSNN-P Lab: Temporal Spatial Navigation Network - Prometheon Laboratory"
    )
    
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialize the TSNN-P system"
    )
    
    parser.add_argument(
        "--status",
        action="store_true", 
        help="Get system status"
    )
    
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Synchronize the system"
    )
    
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate system integrity"
    )
    
    parser.add_argument(
        "--core-nodes",
        type=int,
        default=4,
        help="Number of core nodes (default: 4)"
    )
    
    parser.add_argument(
        "--agg-nodes", 
        type=int,
        default=8,
        help="Number of aggregation nodes (default: 8)"
    )
    
    parser.add_argument(
        "--edge-nodes",
        type=int, 
        default=16,
        help="Number of edge nodes (default: 16)"
    )
    
    parser.add_argument(
        "--quantum-dim",
        type=int,
        default=4,
        help="Quantum state dimension (default: 4)"
    )
    
    args = parser.parse_args()
    
    # Initialize system architecture
    system = SystemArchitecture(
        core_nodes=args.core_nodes,
        aggregation_nodes=args.agg_nodes,
        edge_nodes=args.edge_nodes,
        quantum_dimension=args.quantum_dim
    )
    
    if args.init:
        print("Initializing TSNN-P system...")
        success = system.initialize_system()
        if success:
            print("✓ System initialized successfully")
        else:
            print("✗ System initialization failed")
            sys.exit(1)
    
    if args.status:
        print("Getting system status...")
        status = system.get_system_status()
        print_system_status(status)
    
    if args.sync:
        print("Synchronizing system...")
        sync_fidelity = system.synchronize_system()
        print(f"✓ System synchronized with fidelity: {sync_fidelity:.3f}")
    
    if args.validate:
        print("Validating system integrity...")
        validation = system.validate_system_integrity()
        print_system_validation(validation)
    
    # If no specific action requested, show help
    if not any([args.init, args.status, args.sync, args.validate]):
        parser.print_help()


def print_system_status(status: Dict[str, Any]):
    """Print formatted system status."""
    print("\n=== TSNN-P System Status ===")
    
    print(f"\nSystem State:")
    for key, value in status["system_state"].items():
        print(f"  {key}: {value}")
    
    print(f"\nFat Tree Metrics:")
    fat_tree = status["fat_tree_metrics"]
    print(f"  Total Nodes: {fat_tree['total_nodes']}")
    print(f"  Total Edges: {fat_tree['total_edges']}")
    print(f"  Logarithmic Depth: {fat_tree['logarithmic_depth']:.2f}")
    print(f"  Layer Distribution:")
    for layer, count in fat_tree['layer_distribution'].items():
        print(f"    {layer}: {count}")
    
    print(f"\nSPC Framework Metrics:")
    spc = status["spc_metrics"]
    for key, value in spc.items():
        print(f"  {key}: {value:.3f}")
    
    print(f"\nQuantum States: {status['quantum_states']}")
    print(f"Ethical Constraints: {status['ethical_constraints']}")


def print_system_validation(validation: Dict[str, bool]):
    """Print formatted system validation results."""
    print("\n=== System Integrity Validation ===")
    
    for component, is_valid in validation.items():
        status = "✓" if is_valid else "✗"
        print(f"{status} {component}: {'Valid' if is_valid else 'Invalid'}")
    
    all_valid = all(validation.values())
    print(f"\nOverall Status: {'✓ All Valid' if all_valid else '✗ Issues Found'}")


if __name__ == "__main__":
    main() 