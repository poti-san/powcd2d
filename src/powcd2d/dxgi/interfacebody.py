from ctypes import c_int64, c_uint64, c_void_p

from comtypes import STDMETHOD

from .types import *

IDXGIObject._methods_ = [
    STDMETHOD(c_int32, "SetPrivateData", (POINTER(GUID), c_uint32, c_void_p)),
    STDMETHOD(c_int32, "SetPrivateDataInterface", (POINTER(GUID), POINTER(IUnknown))),
    STDMETHOD(c_int32, "GetPrivateData", (POINTER(GUID), POINTER(c_uint32), c_void_p)),
    STDMETHOD(c_int32, "GetParent", (POINTER(GUID), POINTER(POINTER(IUnknown)))),
]

IDXGIDeviceSubObject._methods_ = [
    *IDXGIObject._methods_,
    STDMETHOD(c_int32, "GetDevice", (POINTER(GUID), POINTER(POINTER(IUnknown)))),
]

IDXGIResource._methods_ = [
    *IDXGIDeviceSubObject._methods_,
    STDMETHOD(c_int32, "GetSharedHandle", (POINTER(c_void_p),)),
    STDMETHOD(c_int32, "GetUsage", (POINTER(c_int32),)),
    STDMETHOD(c_int32, "SetEvictionPriority", (c_uint32,)),
    STDMETHOD(c_int32, "GetEvictionPriority", (POINTER(c_uint32),)),
]

IDXGIKeyedMutex._methods_ = [
    *IDXGIDeviceSubObject._methods_,
    STDMETHOD(c_int32, "AcquireSync", (c_uint64, c_uint32)),
    STDMETHOD(c_int32, "ReleaseSync", (c_uint64,)),
]

IDXGISurface._methods_ = [
    *IDXGIDeviceSubObject._methods_,
    STDMETHOD(c_int32, "GetDesc", (POINTER(DXGI_SURFACE_DESC),)),
    STDMETHOD(c_int32, "Map", (POINTER(DXGI_MAPPED_RECT), c_uint32)),
    STDMETHOD(c_int32, "Unmap", ()),
]

IDXGISurface1._methods_ = [
    *IDXGISurface._methods_,
    STDMETHOD(c_int32, "GetDC", (c_int32, POINTER(c_void_p))),
    STDMETHOD(c_int32, "ReleaseDC", (POINTER(RECT),)),
]

IDXGIAdapter._methods_ = [
    *IDXGIObject._methods_,
    STDMETHOD(c_int32, "EnumOutputs", (c_uint32, POINTER(POINTER(IDXGIObject)))),
    STDMETHOD(c_int32, "GetDesc", (POINTER(DXGI_ADAPTER_DESC),)),
    STDMETHOD(c_int32, "CheckInterfaceSupport", (POINTER(GUID), POINTER(c_int64))),
]

IDXGIOutput._methods_ = [
    *IDXGIObject._methods_,
    STDMETHOD(c_int32, "GetDesc", (POINTER(DXGI_OUTPUT_DESC),)),
    STDMETHOD(c_int32, "GetDisplayModeList", (c_int32, c_uint32, POINTER(c_uint32), POINTER(DXGI_MODE_DESC))),
    STDMETHOD(
        c_int32, "FindClosestMatchingMode", (POINTER(DXGI_MODE_DESC), POINTER(DXGI_MODE_DESC), POINTER(IUnknown))
    ),
    STDMETHOD(c_int32, "WaitForVBlank", ()),
    STDMETHOD(c_int32, "TakeOwnership", (POINTER(IUnknown), c_int32)),
    STDMETHOD(c_int32, "ReleaseOwnership", ()),
    STDMETHOD(c_int32, "GetGammaControlCapabilities", (POINTER(DXGI_GAMMA_CONTROL_CAPABILITIES),)),
    STDMETHOD(c_int32, "SetGammaControl", (POINTER(DXGI_GAMMA_CONTROL),)),
    STDMETHOD(c_int32, "GetGammaControl", (POINTER(DXGI_GAMMA_CONTROL),)),
    STDMETHOD(c_int32, "SetDisplaySurface", (POINTER(IDXGISurface),)),
    STDMETHOD(c_int32, "GetDisplaySurfaceData", (POINTER(IDXGISurface),)),
    STDMETHOD(c_int32, "GetFrameStatistics", (POINTER(DXGI_FRAME_STATISTICS),)),
]

IDXGISwapChain._methods_ = [
    *IDXGIDeviceSubObject._methods_,
    STDMETHOD(c_int32, "Present", (c_uint32, c_uint32)),
    STDMETHOD(c_int32, "GetBuffer", (c_uint32, POINTER(GUID), POINTER(POINTER(IUnknown)))),
    STDMETHOD(c_int32, "SetFullscreenState", (c_int32, POINTER(IDXGIOutput))),
    STDMETHOD(c_int32, "GetFullscreenState", (c_int32, POINTER(POINTER(IDXGIOutput)))),
    STDMETHOD(c_int32, "GetDesc", (POINTER(DXGI_SWAP_CHAIN_DESC),)),
    STDMETHOD(c_int32, "ResizeBuffers", (c_uint32, c_uint32, c_uint32, c_int32, c_uint32)),
    STDMETHOD(c_int32, "ResizeTarget", (POINTER(DXGI_MODE_DESC),)),
    STDMETHOD(c_int32, "GetContainingOutput", (POINTER(IDXGIOutput),)),
    STDMETHOD(c_int32, "GetFrameStatistics", (POINTER(DXGI_FRAME_STATISTICS),)),
    STDMETHOD(c_int32, "GetLastPresentCount", (POINTER(c_uint32),)),
]

IDXGIFactory._methods_ = [
    *IDXGIObject._methods_,
    STDMETHOD(c_int32, "EnumAdapters", (c_uint32, POINTER(POINTER(IDXGIAdapter)))),
    STDMETHOD(c_int32, "MakeWindowAssociation", (c_void_p, c_uint32)),
    STDMETHOD(c_int32, "GetWindowAssociation", (POINTER(c_void_p),)),
    STDMETHOD(
        c_int32, "CreateSwapChain", (POINTER(IUnknown), POINTER(DXGI_SWAP_CHAIN_DESC), POINTER(POINTER(IDXGISwapChain)))
    ),
    STDMETHOD(c_int32, "CreateSoftwareAdapter", (c_void_p, POINTER(POINTER(IDXGIAdapter)))),
]

IDXGIDevice._methods_ = [
    *IDXGIObject._methods_,
    STDMETHOD(
        c_int32,
        "GetAdapter",
        (POINTER(POINTER(IDXGIAdapter)),),
    ),
    STDMETHOD(
        c_int32,
        "CreateSurface",
        (POINTER(DXGI_SURFACE_DESC), c_uint32, c_int32, POINTER(DXGI_SHARED_RESOURCE), POINTER(POINTER(IDXGISurface))),
    ),
    STDMETHOD(c_int32, "QueryResourceResidency", (POINTER(IUnknown), POINTER(c_int32), c_uint32)),
    STDMETHOD(c_int32, "SetGPUThreadPriority", (c_int32,)),
    STDMETHOD(c_int32, "GetGPUThreadPriority", (POINTER(c_int32),)),
]

IDXGIFactory1._methods_ = [
    *IDXGIFactory._methods_,
    STDMETHOD(c_int32, "EnumAdapters1", (c_uint32, POINTER(POINTER(IDXGIAdapter1)))),
    STDMETHOD(c_int32, "IsCurrent", ()),
]

IDXGIAdapter1._methods_ = [
    *IDXGIAdapter._methods_,
    STDMETHOD(c_int32, "GetDesc1", (POINTER(DXGI_ADAPTER_DESC1),)),
]

IDXGIDevice1._methods_ = [
    *IDXGIDevice._methods_,
    STDMETHOD(c_int32, "SetMaximumFrameLatency", (c_uint32,)),
    STDMETHOD(c_int32, "GetMaximumFrameLatency", (POINTER(c_uint32),)),
]
