/*t t_bit_delay_op */
typedef enum [2] {
    bit_delay_op_none,
    bit_delay_op_load,
    bit_delay_op_inc,
    bit_delay_op_dec
} t_bit_delay_op;

/*t t_bit_delay_config */
typedef struct {
    bit    select  "If a delay pair, which delay to update";
    t_bit_delay_op op;
    bit[9] value;
} t_bit_delay_config;

/*t t_bit_delay_response */
typedef struct {
    bit    op_ack;
    bit[9] delay_value;
    bit    sync_value;
} t_bit_delay_response;

