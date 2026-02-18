import os

# Put the path to your training folder here
train_dir = "./train"

for filename in os.listdir(train_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(train_dir, filename)
        new_lines = []
        
        with open(filepath, 'r') as f:
            for line in f:
                if line.strip():
                    parts = line.split(',')
                    # Replace the first element with '4'
                    parts[0] = '4'
                    # Join them back with the original commas
                    new_lines.append(",".join(parts))
        
        with open(filepath, 'w') as f:
            f.writelines(new_lines)

print("Done. All IDs replaced with 4.")