# Simple tests for an counter module

import cocotb
import random
from cocotb.triggers import Timer
from cocotb.types import LogicArray
import logging


@cocotb.test()     
async def test(dut):
     dut.a.value = 12
     dut.b.value = 15
     await Timer(10, unit = 'ns') 
               