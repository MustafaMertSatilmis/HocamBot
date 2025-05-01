import json
import os
import sys

# Constants
INPUT_FILE = r"C:\Users\musta\OneDrive\Desktop\Projeler\HocamBot\Data\Metu_website\oidb_data.json"
OUTPUT_DIR = r"C:\Users\musta\OneDrive\Desktop\Projeler\HocamBot\Data\Metu_website\split_files"
MAX_FILE_SIZE = 500000  # Max file size in bytes (500KB)


def get_size(obj):
    """Calculate the size of a JSON object in bytes."""
    return sys.getsizeof(json.dumps(obj, ensure_ascii=False).encode("utf-8"))


def split_large_text(text, max_chunk_size=10000):
    """Splits large text into smaller chunks, ensuring no chunk exceeds max_chunk_size characters."""
    return [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]


def split_json_file(input_file, output_dir, max_file_size):
    """Splits a large JSON file into multiple smaller JSON files."""
    
    # Load the original JSON data
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    current_batch = []
    current_size = 0
    file_index = 1

    for item in data:
        item_size = get_size(item)

        if item_size > max_file_size:
            # If a single document is too large, split its text
            print(f"Splitting large document: {item['url']}")
            text_chunks = split_large_text(item["content"])

            for chunk in text_chunks:
                chunk_obj = {"url": item["url"], "title": item["title"], "content": chunk}
                chunk_size = get_size(chunk_obj)

                if current_size + chunk_size > max_file_size:
                    # Save the current batch
                    output_path = os.path.join(output_dir, f"oidb_data_part_{file_index}.json")
                    with open(output_path, "w", encoding="utf-8") as out_f:
                        json.dump(current_batch, out_f, ensure_ascii=False, indent=4)
                    print(f"Saved: {output_path} ({current_size} bytes)")

                    # Start a new batch
                    current_batch = []
                    current_size = 0
                    file_index += 1

                current_batch.append(chunk_obj)
                current_size += chunk_size
        else:
            if current_size + item_size > max_file_size:
                # Save the current batch
                output_path = os.path.join(output_dir, f"oidb_data_part_{file_index}.json")
                with open(output_path, "w", encoding="utf-8") as out_f:
                    json.dump(current_batch, out_f, ensure_ascii=False, indent=4)
                print(f"Saved: {output_path} ({current_size} bytes)")

                # Start a new batch
                current_batch = []
                current_size = 0
                file_index += 1

            current_batch.append(item)
            current_size += item_size

    # Save the last batch
    if current_batch:
        output_path = os.path.join(output_dir, f"oidb_data_part_{file_index}.json")
        with open(output_path, "w", encoding="utf-8") as out_f:
            json.dump(current_batch, out_f, ensure_ascii=False, indent=4)
        print(f"Saved: {output_path} ({current_size} bytes)")

# Run the function
split_json_file(INPUT_FILE, OUTPUT_DIR, MAX_FILE_SIZE)
