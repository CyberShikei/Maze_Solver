#!/bin/bash

# Ensure the script stops on the first error
set -e

export PYTHONPATH=$(pwd)

# Run all tests using pytest
pytest src/tests

# Optional: Print success message if all tests pass
echo "All tests ran successfully."
