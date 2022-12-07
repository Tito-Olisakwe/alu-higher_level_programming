#!/usr/bin/python3
"""
    Create 'lazy_matrix_mul' function.
"""
import numpy as NumPy


def lazy_matrix_mul(m_a, m_b):
    """
        Write a function that multiplies 2 matrices by using
        the module NumPy
        Prototype: def lazy_matrix_mul(m_a, m_b):
        Test cases should be the same as 100-matrix_mul but
        with new exception type/message
    """

    return (NumPy.matmul(m_a, m_b))
