import cdl_desc
from cdl_desc import CdlModule, CModel, Verilog

class Library(cdl_desc.Library):
    name="std"
    pass

class TechModules(cdl_desc.Modules):
    name = "tech"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    cdl_include_dirs = ["cdl"]
    export_dirs      = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CdlModule("tech_sync_bit") ]
    modules += [ CdlModule("tech_sync_flop") ]
    pass

class SramModules(cdl_desc.Modules):
    name = "sram"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    cdl_include_dirs = ["cdl"]
    export_dirs      = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CModel("srams",src_dir=c_src_dir) ]
    pass

class VerilogModules(cdl_desc.Modules):
    name = "sram_verilog"
    src_dir     = "verilog"
    modules = []
    modules += [ Verilog("srw_srams") ]
    modules += [ Verilog("mrw_srams") ]
    pass
