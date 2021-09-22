# this code will be removed later on as we progress
# this program is just the python version of OpenVR, which steam uses to open SteamVR and detect VR hardware, regardless of brand
import xr

available = xr.enumerate_instance_extension_properties()

required = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME, ]
for prop in required:
    assert prop in available