#!/usr/bin/python3
"""Defines a function"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices lazily."""
    return (np.matmul(m_a, m_b))
