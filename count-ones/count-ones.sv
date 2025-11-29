module count_ones #(parameter WIDTH = 8) (
    input logic clk,
    input logic rst,
    input logic [WIDTH-1:0] in,
    output logic [$clog2(WIDTH+1)-1:0] out
);

logic [$clog2(WIDTH+1)+1:0] counter = 0;
integer i;

always_ff @(posedge clk or posedge rst) begin
    if(rst)
        out <= '0;
    else begin
        out <= counter;
    end
end

always_comb begin
    counter = 0;
    for(i = 0; i < WIDTH ; i++)
        begin
            if(in[i])
                counter = counter + 1;
        end
end

initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0, count_ones);
end

endmodule