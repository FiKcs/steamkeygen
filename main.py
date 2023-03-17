import random
import string
import os

# Create strings in the desired format

def generate_random_string(format):
    if format == 1:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    elif format == 2:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    elif format == 3:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Prompt the user to select a string format (5-5-5/ 5-5-5-5/ 5-5-5-5-5)




print("   _____ _                         _  __             _____            ")
print(" / ____| |                        | |/ /            / ____|           ")
print(" | (___ | |_ ___  __ _ _ __ ___   | ' / ___ _   _  | |  __  ___ _ __  ")
print("  \___ \| __/ _ \/ _` | '_ ` _ \  |  < / _ \ | | | | | |_ |/ _ \ '_ \ ")
print("  ____) | ||  __/ (_| | | | | | | | . \  __/ |_| | | |__| |  __/ | | |")
print(" |_____/ \__\___|\__,_|_| |_| |_| |_|\_\___|\__, |  \_____|\___|_| |_|")
print("                                             __/ |                    ")
print("                                            |___/                     ")


while True:
    format = input("Select a string format:\n1. XXXXX-XXXXX-XXXXX\n2. XXXXX-XXXXX-XXXXX-XXXXX\n3. XXXXX-XXXXX-XXXXX-XXXXX-XXXXX\n")
    if format.isdigit() and int(format) in [1, 2, 3]:
        format = int(format)
        break
    else:
        print("Invalid input. Please enter a number from 1 to 3.")
        continue

# Get the number of output files already generated

output_files = [f for f in os.listdir('.') if f.startswith('output')]
output_file_num = len(output_files) + 1

# Prompt the user to enter the number of strings to generate

while True:
    num_strings = input("Enter the number of strings to generate: ")
    if num_strings.isdigit():
        num_strings = int(num_strings)
        break
    else:
        print("Invalid input. Please enter a number.")
        continue

# Generate the specified number of strings in the selected format and write them to a new output file

with open(f"output{output_file_num}.txt", "w") as f:
    for i in range(num_strings):
        f.write(generate_random_string(format) + "\n")

print(f"{num_strings} strings generated in the {format} format and saved to output{output_file_num}.txt")
