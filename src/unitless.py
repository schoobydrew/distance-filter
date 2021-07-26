import numpy as np
import pint

ureg = pint.UnitRegistry()

def toKm(mag: float, unit: str):
    # set our default working distance to kilometer
    return pint.Quantity(mag, unit).to("kilometer")