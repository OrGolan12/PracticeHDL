# Count-Ones

## Description
`Count-Ones` is a simple digital module that counts the number of active (high) bits in an 8-bit input vector. At every rising edge of the clock, the module outputs a 4-bit value representing the number of `1`s in the input.

## Ports

| Name | Direction | Width | Description |
|------|-----------|-------|-------------|
| rst  | input     | 1     | Active-high reset signal |
| clk  | input     | 1     | Clock signal |
| in   | input     | 8     | 8-bit input vector |
| out  | output    | 4     | 4-bit output representing number of high bits in `in` |

## Functionality
- On every rising edge of `clk`:
  - `out` is updated to reflect the number of `1`s in `in`.
- `rst` can be used to asynchronously reset the output if implemented.

## Example
| in      | out |
|---------|-----|
| 00000000 | 0000 |
| 10101010 | 0100 |
| 11111111 | 1000 |

## Waveform
<img width="1602" height="170" alt="image" src="https://github.com/user-attachments/assets/3d992dd5-5081-4feb-b337-d60838b636e0" />



