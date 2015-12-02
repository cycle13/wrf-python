
import numpy as n

from wrf.var.constants import Constants
from wrf.var.destagger import destagger_windcomp
from wrf.var.decorators import convert_units

__all__ = ["get_u_destag", "get_v_destag", "get_w_destag",
           "get_destag_wspd_wdir"]

def _calc_wspd(u, v):
    return n.sqrt(u**2 + v**2)

def _calc_wdir(u, v):
    wdir = 270.0 - n.arctan2(v,u) * (180.0/Constants.PI)
    return n.remainder(wdir, 360.0)

@convert_units("wind", "mps")
def _calc_wspd_wdir(u, v, units="mps"):
    check_units(units, "wind")
    return (_calc_wspd(u,v), _calc_wdir(u,v))

@convert_units("wind", "mps")
def get_u_destag(wrfnc, units="mps", timeidx=0):
    u = destagger_windcomp(wrfnc,"u", timeidx)
    return u

@convert_units("wind", "mps")
def get_v_destag(wrfnc, units="mps", timeidx=0):
    v = destagger_windcomp(wrfnc,"v", timeidx)
    return v

@convert_units("wind", "mps")
def get_w_destag(wrfnc, units="mps", timeidx=0):
    w = destagger_windcomp(wrfnc,"w", timeidx)
    return w

def get_destag_wspd_wdir(wrfnc, units="mps", timeidx=0):
    u = destagger_windcomp(wrfnc,"u", timeidx)
    v = destagger_windcomp(wrfnc,"v", timeidx)
    
    return _calc_wspd_wdir(u,v,units)

