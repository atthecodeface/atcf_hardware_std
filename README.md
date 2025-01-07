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

# Technology library modules

## Serdes modules

The library provides headers for differential DDR (double data rate)
serializers and deseerializers, and for delay modules (which are used
on input signals to delay them by a configurable delay value, measured
in 'delay taps').

Actual device implementations of these may need to be provided to map
a design to a real device.

An example of use would be with SGMII where the transmit data is
serialized from 4 bits and deserialized into 4 bits, with some module
managing the delays to center the deserializer of the data pin to the
center of the eye of the data.

The `cascaded_delay_pair` module is applied to the SGMII receive clock
(625MHz) and the output of that registered based on a derived sgmii
receive data clock of half that frequency and which thus can be used
(by tweaking the delay configuration) to find the delay in delay taps
of a single phase of the clock.

### `diff_ddr_serializer4` module

This module takes a high speed serial clock and a lower data clock,
and N=4 bits of data per data clock, and it serializes the input data
to a differential output pin pair. If N is 4 then the data clock is
expected to be half of the high speed serial clock, as the data pin is
expected to be DDR (changing on both edges of the serial clock).

### `diff_ddr_deserializer4` module

TODO: note serialization order

This module takes a differential input pin pair, delays each one
(separately) and then deserializes both the positive and negative pins
to separate values using the serial clock, presenting the positive
data as `data` and the negative data as `tracker`.

The two delay modules are configured through the `delay_config`
interface, which runs on the `delay_clk`. This input includes a select
pin which is 0 to adjust the delay module for `data` and 1 to adjust
the delay module for `tracker`.

### `cascaded_delay_pair` module

This module is a technology-specific implementation of a *pair* of
delay modules back-to-back, each using the same delay configuration.
