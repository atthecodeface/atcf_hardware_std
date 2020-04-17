# atcf_hardware_std

This repository contains the CDL source code and C models for the
ATCF standard libraries.

This currently is a set of SRAMs and technology independent flops for
synchronization.

## Status

The repository is in use in two grip repositories: for the BBC
microcomputer and for RISC-V systems

# SRAMs

CDL does not provide an inferred memory system; it requires explicit
memory instantiation. This is in part due to the requirement of
silicon testability - every memory requires (in modern processes) BIST
(built-in self test) and possibly redundancy - and this requires extra
wiring and more.

So CDL requires instantiations of SRAMs; this repository provides a
small standard set, using the CDL simulation engine model for C
simulation. Verilog simulation currently requires hand-crafted or
machine-generated verilog models; for the FPGAs this is performed
with a Python 2 script that requires porting in to this repository.

# Synchronization flops

Designs with asynchronous clocks often require synchronization flops.
This repository includes two technology-derived flops; the first is
purely that, a flop. It should in a real design (as in, for silicon or
FPGA) be replaced by a metastable resistant flop.

The second is a synchronization bit; this should be a chain of the
required length of the reuired metastable resistant flops. Most
designs may assume that this will synchronize a bit with a worst case
timing of a source clock period and two destination clock periods.
