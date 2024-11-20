import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation

def dilate_white_areas(image_path, lower_threshold, upper_threshold, dilation_iterations):
    # Load the image
    image = Image.open(image_path)
    # Convert the image to grayscale mode
    image = image.convert("L")
    # Get the image dimensions
    width, height = image.size

    # Create a new blank image with black background
    result_image = Image.new("L", (width, height), 0)

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel value at (x, y)
            pixel = image.getpixel((x, y))
            # Check if the pixel is within the white range
            if lower_threshold <= pixel <= upper_threshold:
                # Set the corresponding pixel in the result image to white
                result_image.putpixel((x, y), 255)

    # Convert the result image to a numpy array
    result_array = np.array(result_image)

    # Perform dilation on the white areas
    dilated_array = binary_dilation(result_array, iterations=dilation_iterations)

    # Create a new blank image with black background for the dilated areas
    dilated_image = Image.new("L", (width, height), 0)

    # Iterate over each pixel in the dilated array
    for x in range(width):
        for y in range(height):
            # Get the pixel value at (x, y)
            pixel = dilated_array[y, x]
            # Check if the pixel is white after dilation
            if pixel:
                # Set the corresponding pixel in the dilated image to white
                dilated_image.putpixel((x, y), 255)

    return dilated_image

# Example usage
input_image_path = "tmp1.jpg"
output_image_path = "output_image.png"
lower_threshold = 200  # Modify this as per your requirement
upper_threshold = 255  # Modify this as per your requirement
dilation_iterations = 5  # Modify this as per your requirement
result_image = dilate_white_areas(input_image_path, lower_threshold, upper_threshold, dilation_iterations)
result_image.save(output_image_path)
