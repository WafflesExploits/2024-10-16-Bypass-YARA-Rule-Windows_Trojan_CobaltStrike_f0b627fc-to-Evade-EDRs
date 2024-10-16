# Made by WafflesExploits
# Generate alternatives to EAX to 0x00FFFFFF
import random
from sys import argv

# Check for correct number of arguments
if len(argv) < 3:
    print("./Replace_bytes.py <file.bin> <output_path>")
    exit()

file_path = argv[1]
output_path = argv[2]

# Desired byte length for replacement
DESIRED_LENGTH = 10

# List of safe padding instructions (bytes) without null bytes
padding_instructions = [
     b'\x90',             # NOP (1 byte)
     b'\x87\xC0'          # NOP (2 bytes) xchg   eax,eax 
]
# List of alternative byte sequences to set EAX to 0x00414141
alternatives = [
    # Alternative 1: MOV EAX, 0x00414141 (SET EAX TO 0X00414141)
    [b'\xB8\x41\x41\x41\x00'],

    # Alternative 2: XOR EAX,EAX (SET EAX TO 0); MOV EAX, 0X00414141
    [b'\x31\xC0',b'\xB8\x41\x41\x41\x00']
]

def distribute_padding(padding_bytes_needed, positions):
    """
    Distributes padding bytes randomly across the available positions.

    :param padding_bytes_needed: Total number of padding bytes to distribute.
    :param positions: List of positions where padding can be inserted.
    :return: Dictionary with position as key and list of padding instructions as value.
    """
    padding_distribution = {pos: [] for pos in positions}

    while padding_bytes_needed > 0:
        pos = random.choice(positions)
        instr = random.choice(padding_instructions)
        instr_length = len(instr)
        if instr_length <= padding_bytes_needed:
            padding_distribution[pos].append(instr)
            padding_bytes_needed -= instr_length

    return padding_distribution

def insert_padding(instruction_list, desired_length=DESIRED_LENGTH):
    """
    Inserts padding instructions randomly into the instruction list to reach the desired byte length.

    :param instruction_list: List of instruction byte sequences.
    :param desired_length: The total desired byte length after insertion.
    :return: Byte sequence with padding instructions inserted.
    """
    # Calculate the total byte length of the instructions
    total_instr_length = sum(len(instr) for instr in instruction_list)

    # Calculate the number of padding bytes needed
    padding_bytes_needed = desired_length - total_instr_length

    if padding_bytes_needed < 0:
        raise ValueError(f"Instruction list exceeds desired length of {desired_length} bytes.")

    # Positions where padding can be inserted: start, between instructions, end
    positions = ['start'] + [i for i in range(len(instruction_list))] + ['end']

    # Distribute padding bytes randomly among the positions
    padding_distribution = distribute_padding(padding_bytes_needed, positions)

    final_bytes = b''

    # Add padding at the start
    for pad in padding_distribution.get('start', []):
        final_bytes += pad

    for i, instr in enumerate(instruction_list):
        # Add the instruction
        final_bytes += instr

        # Add padding after the instruction
        for pad in padding_distribution.get(i, []):
            final_bytes += pad

    # Add padding at the end
    for pad in padding_distribution.get('end', []):
        final_bytes += pad

    return final_bytes

def replace_bytes(input_filename, output_filename, replacement_bytes):
    """
    Replaces a specific byte sequence in the input file with the replacement bytes.

    :param input_filename: Path to the input binary file.
    :param output_filename: Path to save the modified binary file.
    :param replacement_bytes: Byte sequence to replace the search pattern with.
    """
    # Search pattern to replace (10 bytes)
    search_bytes = b"\x25\xff\xff\xff\x00\x3d\x41\x41\x41\x00"

    with open(input_filename, "rb") as input_file:
        content = input_file.read()

    if search_bytes not in content:
        print("Search pattern not found in input file.")
        exit()

    # Ensure replacement_bytes is exactly DESIRED_LENGTH bytes
    if len(replacement_bytes) != DESIRED_LENGTH:
        print(f"Replacement bytes length ({len(replacement_bytes)}) does not match desired length ({DESIRED_LENGTH}).")
        exit()

    # Perform the replacement
    modified_content = content.replace(search_bytes, replacement_bytes)

    with open(output_filename, "wb") as output_file:
        output_file.write(modified_content)

    print(f"Modified content saved to {output_filename}.")

def main():
    # Select a random alternative
    selected_alternative = random.choice(alternatives)
    selected_index = alternatives.index(selected_alternative) + 1
    print(f"Selected Alternative: {selected_index}")

    # Insert padding instructions
    try:
        final_sequence = insert_padding(selected_alternative)
    except ValueError as ve:
        print(f"Error: {ve}")
        exit()

    # Print the byte sequence in hexadecimal format
    hex_sequence = ''.join(['\\x{:02X}'.format(b) for b in final_sequence])
    print(f"Final Byte Sequence with Padding Instructions:\n\"{hex_sequence}\"")

    # Replace Bytes
    replace_bytes(file_path, output_path, final_sequence)

if __name__ == "__main__":
    main()
