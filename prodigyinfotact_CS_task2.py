from PIL import Image

def process_image(dw1, output_path, keys):
    """
    Encrypts or decrypts an image using a multi-channel XOR cipher.
    keys: A tuple of three integers (R_key, G_key, B_key)
    """
    # 1. Load the image and ensure it is in RGB format
    img = Image.open(dw1)
    img = img.convert("RGB") 
    pixels = img.load()
    width, height = img.size

    # 2. Extract individual keys from the tuple
    key_r, key_g, key_b = keys

    # 3. Iterate through every pixel in the grid
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Apply the XOR operation (^) to each channel
            # We use % 256 to ensure values stay within the 0-255 range
            new_r = r ^ key_r
            new_g = g ^ key_g
            new_b = b ^ key_b
            
            pixels[x, y] = (new_r, new_g, new_b)

    # 4. Save the result as a PNG (lossless)
    img.save(output_path)
    print(f"Success! Processed image saved as: {output_path}")

# --- Example Usage ---

# Define your secret keys (0-255)
# Using different numbers for each channel makes it stronger!
my_secret_keys = (142, 57, 210) 

# Step 1: Encrypt the original image
# Make sure "input.jpg" exists in your folder!
process_image("dw1.png", "encrypted_photo.png", my_secret_keys)

# Step 2: Decrypt (Run the encrypted file back through with the SAME keys)
process_image("encrypted_photo.png", "restored_photo.png", my_secret_keys)