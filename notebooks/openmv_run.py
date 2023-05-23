import sensor
import tf

# Load the TensorFlow Lite model from the SD card
model = tf.load("model.tflite", load_to_fb=True)

# setup the camera sensor
sensor.reset()

# Set pixel format to GRAYSCALE
sensor.set_pixformat(sensor.GRAYSCALE)

sensor.set_framesize(sensor.B320X320)

# Wait 2s for settings take effect
sensor.skip_frames(time=2000)

# main loop
while True:
    # get an image from the camera sensor
    img = sensor.snapshot()
    img.lens_corr(1.8)  # strength of 1.8 is good for the 2.8mm lens.

    img.scale(0.1, 0.1)

    img.crop(roi=(0, 0, 27, 27))

    img.mul(img.binary([(240, 255)]))

    # get the model output for the image
    classification_result = model.classify(img)
    model_output = classification_result[0].output()

    second_highest_index = -1
    max_index = 0
    list_len = len(model_output)
    for index in range(list_len):
        if model_output[index] > model_output[max_index]:
            second_highest_index = max_index
            max_index = index

    print("Index of the maximum element is:", max_index)