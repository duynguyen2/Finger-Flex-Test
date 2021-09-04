import xr

available = xr.enumerate_instance_extension_properties()

required = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME, ]
for prop in required:
    assert prop in available