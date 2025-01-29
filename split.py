import json
import os

def split_json(input_file, output_dir, n):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Split the data into chunks of size n
    for i in range(0, len(data), n):
        chunk = data[i:i + n]
        output_file = os.path.join(output_dir, f'output_{i // n + 1}.json')

        # Write each chunk to a separate JSON file
        with open(output_file, 'w') as chunk_file:
            json.dump(chunk, chunk_file, indent=4)

        print(f'Chunk saved to {output_file}')

if __name__ == "__main__":
    input_file = 'output.json'  # Replace with the path to your input .json file
    output_dir = 'output_chunks'  # Directory where split files will be saved
    n = 100  # Number of items per file

    split_json(input_file, output_dir, n)