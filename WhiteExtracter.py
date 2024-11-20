from PIL import Image

def extract_white_range(image_path, lower_threshold, upper_threshold):
    # Load the image
    image = Image.open(image_path)
    # Convert the image to RGBA mode
    image = image.convert("RGBA")
    # Get the image dimensions
    width, height = image.size

    # Create a new blank image with black background
    result_image = Image.new("RGBA", (width, height), (0, 0, 0, 255))

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel color at (x, y)
            pixel = image.getpixel((x, y))
            # Check if the pixel is within the white range
            if (
                lower_threshold <= pixel[0] <= upper_threshold
                and lower_threshold <= pixel[1] <= upper_threshold
                and lower_threshold <= pixel[2] <= upper_threshold
            ):
                # Put the white pixel on the result image
                result_image.putpixel((x, y), pixel)

    return result_image

# Example usage
input_image_path = "tmp1.jpg"
output_image_path = "output_image.png"
lower_threshold = 200  # Modify this as per your requirement
upper_threshold = 255  # Modify this as per your requirement
result_image = extract_white_range(input_image_path, lower_threshold, upper_threshold)
result_image.save(output_image_path)
