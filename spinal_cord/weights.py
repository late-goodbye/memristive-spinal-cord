from enum import Enum


def init(weights: list):
    weights = [float(weight) for weight in weights]
    Weights.aff_ia_moto = weights[0]
    Weights.aff_ia_ia = weights[1]
    Weights.aff_ii_ii = weights[2]
    Weights.ii_moto = weights[3]
    Weights.ia_ia = weights[4]
    Weights.ia_moto = weights[5]


class Weights:

    # Tier Interconnections
    e0e1 = 100.
    e0e3 = 100.
    e1e2 = 90.
    e2e1 = 90.
    e2i1 = 100.
    e3e4 = 100.
    e3i0 = 100.
    e4e3 = 100.
    i0e1 = -60.
    i1e1 = -50.

    # Coonnections between tiers

    e0e0 = 45.
    e3e0 = 40.
    e2e2 = 100.

    # Connections to pool

    e2p = 4.

    # Motogroup interconnections

    aff_ia_moto = 7.
    aff_ia_ia = 5.
    aff_ii_ia = 5.
    aff_ii_ii = 14.
    ii_moto = 6.
    ia_ia = -3.
    ia_moto = -2.

    # Pool to Motogroup
    p_ex_moto = 24.
    p_ex_ia = 8.
    p_fl_moto = 24.
    p_fl_ia = 8.

    # Pool interconnections

    p_extens_sus_extens_ex = 1.
    p_flex_sus_flex_ex = 1.
    p_extens_sus_flex_in = -10.
    p_flex_sus_extens_in = -10.
    p_flex_extens_in = -40.
    p_extens_flex_in = -40.
