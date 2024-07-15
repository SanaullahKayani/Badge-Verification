
# Badge Verification and Conversion

This repository contains a Python script to verify and convert user-uploaded badges. The badges are avatars within a circle, and the script ensures the following:

- The badge image size is 512x512 pixels.
- Only non-transparent pixels are within a circle.
- The colors in the badge give a "happy" feeling.

Additionally, the repository includes a function to convert any image to the specified badge format.

## Features

- **Badge Verification**: Verifies that the uploaded badge meets the specified criteria.
- **Badge Conversion**: Converts any image to the specified badge format (512x512 pixels, circular avatar).

## Requirements

- Python 3.x
- Pillow
- NumPy

## Usage

### Convert an Image to Badge Format

Convert any image to a circular badge with a size of 512x512 pixels.

```python
from badge_verification import convert_image_to_badge

input_image_path = "path/to/your/image.png"
output_image_path = "path/to/your/output_badge.png"

convert_image_to_badge(input_image_path, output_image_path)
