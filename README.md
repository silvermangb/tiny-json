# Tiny JSON

Tiny JSON is a Python project that provides functions for encoding and decoding JSON data into a more compact form. The goal is to reduce the size of the JSON for more efficient transmission or storage.

Scripts
This repository contains two main scripts:

tiny_json.py: This script provides the command-line interface to encode, decode, and templatize JSON data. It can be used directly from the command line or imported into another Python script.

test.py: This script is used to test the functionality of the main tiny_json.py script. It loads JSON test vectors, encodes and decodes them, and compares the output to the original input to verify correctness.

Example

$ python3 tiny_json.py encode --json '{"key": "value"}'
value,

$ python3 tiny_json.py decode --encoded-json value, --json-template '{"key": ""}'
{"key": "value"}


Usage

From the command line

To encode JSON data:

python3 tiny_json.py encode --json '{"key": "value"}'


To decode JSON data:

python3 tiny_json.py decode --encoded-json '<encoded_json>' --json-template '<json_template>'

To create a JSON template:

python3 tiny_json.py templatize --json '{"key": "value"}'

By embedding

import tiny_json

call encode, decode, and, templatize.

Contributing
Contributions are welcome. Please open an issue to discuss your idea or submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

## Getting Started

Clone the repository:

git clone https://github.com/silvermangb/tiny-json.git
