begin_memory_edit -hardware_name "USB-Blaster \[3-2\]" -device_name "@1: EP3C16/EP4CE15 (0x020F20DD)"
write_content_to_memory -instance_index 0 -content [lindex $argv 0] -start_address 0 -word_count 1
end_memory_edit