`timescale 1ns/1ps

module adder(
input logic [3:0] a, b,
output logic [4:0] y
);

assign y = a + b;


initial begin
$dumpfile("dump.vcd");
$dumpvars(1,adder);
end

endmodule