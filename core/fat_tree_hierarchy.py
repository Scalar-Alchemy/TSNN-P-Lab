"""
Fat Tree Hierarchy implementation for TSNN-P.

A scalable, three-tiered structure (Core, Aggregation, Edge) for distributed 
quantum-AI computation with logarithmic depth and efficient resource allocation.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Represents a node in the Fat Tree Hierarchy."""
    id: str
    layer: str  # 'core', 'aggregation', 'edge'
    position: Tuple[int, int]
    quantum_state: Optional[np.ndarray] = None
    ethical_constraints: Optional[Dict] = None


class FatTreeHierarchy:
    """
    Fat Tree Hierarchy for scalable quantum-AI computation.
    
    Implements a three-tiered structure with Core, Aggregation, and Edge layers
    for distributed processing with logarithmic depth O(log N).
    """
    
    def __init__(self, core_nodes: int = 4, aggregation_nodes: int = 8, edge_nodes: int = 16):
        """
        Initialize the Fat Tree Hierarchy.
        
        Args:
            core_nodes: Number of core layer nodes
            aggregation_nodes: Number of aggregation layer nodes  
            edge_nodes: Number of edge layer nodes
        """
        self.core_nodes = core_nodes
        self.aggregation_nodes = aggregation_nodes
        self.edge_nodes = edge_nodes
        
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Tuple[str, str]] = []
        
        self._build_hierarchy()
    
    def _build_hierarchy(self):
        """Build the three-tiered hierarchy structure."""
        # Create core nodes
        for i in range(self.core_nodes):
            node_id = f"core_{i}"
            self.nodes[node_id] = Node(
                id=node_id,
                layer="core",
                position=(0, i),
                quantum_state=np.random.rand(4, 4),  # Example quantum state
                ethical_constraints={"fidelity_threshold": 0.95}
            )
        
        # Create aggregation nodes
        for i in range(self.aggregation_nodes):
            node_id = f"agg_{i}"
            self.nodes[node_id] = Node(
                id=node_id,
                layer="aggregation", 
                position=(1, i),
                quantum_state=np.random.rand(4, 4),
                ethical_constraints={"fidelity_threshold": 0.90}
            )
        
        # Create edge nodes
        for i in range(self.edge_nodes):
            node_id = f"edge_{i}"
            self.nodes[node_id] = Node(
                id=node_id,
                layer="edge",
                position=(2, i),
                quantum_state=np.random.rand(4, 4),
                ethical_constraints={"fidelity_threshold": 0.85}
            )
        
        # Create edges between layers
        self._create_edges()
    
    def _create_edges(self):
        """Create edges between nodes in adjacent layers."""
        # Core to Aggregation edges
        for core_id in [f"core_{i}" for i in range(self.core_nodes)]:
            for agg_id in [f"agg_{i}" for i in range(self.aggregation_nodes)]:
                self.edges.append((core_id, agg_id))
        
        # Aggregation to Edge edges
        for agg_id in [f"agg_{i}" for i in range(self.aggregation_nodes)]:
            for edge_id in [f"edge_{i}" for i in range(self.edge_nodes)]:
                self.edges.append((agg_id, edge_id))
    
    def synchronize_layers(self) -> float:
        """
        Synchronize quantum states across layers using discrete operator.
        
        Returns:
            Synchronization fidelity score
        """
        total_fidelity = 0.0
        edge_count = 0
        
        for edge in self.edges:
            node1, node2 = self.nodes[edge[0]], self.nodes[edge[1]]
            
            # Calculate synchronization using discrete operator
            fidelity = self._calculate_sync_fidelity(node1, node2)
            total_fidelity += fidelity
            edge_count += 1
        
        return total_fidelity / edge_count if edge_count > 0 else 0.0
    
    def _calculate_sync_fidelity(self, node1: Node, node2: Node) -> float:
        """
        Calculate synchronization fidelity between two nodes.
        
        Args:
            node1: First node
            node2: Second node
            
        Returns:
            Fidelity score between 0 and 1
        """
        if node1.quantum_state is None or node2.quantum_state is None:
            return 0.0
        
        # Calculate overlap between quantum states
        overlap = np.trace(node1.quantum_state @ node2.quantum_state.T)
        fidelity = np.abs(overlap) / (np.linalg.norm(node1.quantum_state) * np.linalg.norm(node2.quantum_state))
        
        return np.clip(fidelity, 0.0, 1.0)
    
    def optimize_resource_allocation(self) -> Dict[str, float]:
        """
        Optimize resource distribution across nodes.
        
        Returns:
            Dictionary mapping node IDs to utility scores
        """
        utilities = {}
        
        for node_id, node in self.nodes.items():
            # Calculate utility based on quantum state coherence and ethical constraints
            coherence = self._calculate_coherence(node.quantum_state)
            ethical_score = self._calculate_ethical_score(node.ethical_constraints)
            
            utilities[node_id] = coherence * ethical_score
        
        return utilities
    
    def _calculate_coherence(self, quantum_state: np.ndarray) -> float:
        """Calculate quantum state coherence."""
        if quantum_state is None:
            return 0.0
        
        # Simplified coherence calculation
        eigenvalues = np.linalg.eigvals(quantum_state)
        coherence = np.sum(np.abs(eigenvalues)) / len(eigenvalues)
        
        return np.clip(coherence, 0.0, 1.0)
    
    def _calculate_ethical_score(self, constraints: Dict) -> float:
        """Calculate ethical compliance score."""
        if not constraints:
            return 1.0
        
        # Simplified ethical scoring
        fidelity_threshold = constraints.get("fidelity_threshold", 0.9)
        return fidelity_threshold
    
    def get_logarithmic_depth(self) -> float:
        """Calculate the logarithmic depth of the hierarchy."""
        total_nodes = len(self.nodes)
        return np.log2(total_nodes) if total_nodes > 0 else 0.0
    
    def get_node_by_layer(self, layer: str) -> List[Node]:
        """Get all nodes in a specific layer."""
        return [node for node in self.nodes.values() if node.layer == layer]
    
    def get_connected_nodes(self, node_id: str) -> List[str]:
        """Get all nodes connected to a given node."""
        connected = []
        for edge in self.edges:
            if edge[0] == node_id:
                connected.append(edge[1])
            elif edge[1] == node_id:
                connected.append(edge[0])
        return connected 