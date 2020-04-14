import cdl_desc
from cdl_desc import CdlModule, CModel

class TechModules(cdl_desc.Modules):
    name = "tech"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    modules = []
    modules += [ CdlModule("tech_sync_bit") ]
    modules += [ CdlModule("tech_sync_flop") ]
    modules += [ CModel("srams",src_dir=c_src_dir) ]
    pass

class SramhModules(cdl_desc.Modules):
    name = "sram"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    modules = []
    modules += [ CModel("srams",src_dir=c_src_dir) ]
    pass

modules=cdl_desc.Modules.__subclasses__
