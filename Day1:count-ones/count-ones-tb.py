# Simple tests for an counter module
import cocotb
import random
from cocotb.triggers import Timer, RisingEdge
from cocotb.types import LogicArray
from cocotb.clock import Clock
import logging

@cocotb.test()     
async def test(dut):
    cocotb.start_soon(Clock(dut.clk, 10, 'ns', period_high=3).start())
    dut.rst.value = 1
    await Timer(5, 'ns')
    dut.rst.value = 0
    for i in range(0,256):
        await Timer(2, unit = 'ns') 
        rand_val = i
        dut['in'].value = LogicArray(f"{rand_val:0{8}b}")
        await RisingEdge(dut.clk) 
        await Timer(2, unit = 'ns')
        assert dut.out.value == rand_val.bit_count(), f"data should be {rand_val.bit_count()}, got {dut.out.value}"
               