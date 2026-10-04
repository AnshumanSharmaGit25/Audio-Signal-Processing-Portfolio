import os
import json
import glob

README_HEADER = """# Audio Signal Processing & DSP Portfolio

This repository tracks my hands-on implementation of digital signal processing (DSP) concepts, focusing on electroacoustics, signal analysis, and algorithmic audio filtering in Python.

## Automated Progress Log
"""

README_FOOTER = """
## Technical Stack
* **Languages:** Python
* **Libraries:** `NumPy`, `Matplotlib`
* **Focus:** Audio Acoustics, Electroacoustics, Signal Processing

## About the Developer
B.Tech Electronics & Communication Engineering student bridging audio production and embedded DSP systems.
"""

entries = []

# Find all notebooks in numerical/alphabetical order
notebooks = sorted(glob.glob("*.ipynb"))

for nb_file in notebooks:
    try:
        with open(nb_file, 'r', encoding='utf-8') as f:
            nb_data = json.load(f)
            # Find the first markdown cell
            for cell in nb_data.get('cells', []):
                if cell.get('cell_type') == 'markdown':
                    content = "".join(cell.get('source', []))
                    entries.append(f"### `{nb_file}`\n\n{content}\n\n---")
                    break
    except Exception as e:
        print(f"Error reading {nb_file}: {e}")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README_HEADER + "\n\n" + "\n\n".join(entries) + "\n\n" + README_FOOTER)

print("README.md updated successfully!")