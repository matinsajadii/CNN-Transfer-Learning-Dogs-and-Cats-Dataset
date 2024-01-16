# Dog or Cat Image Classifier

This application is a simple image classifier that predicts whether an uploaded image contains a dog or a cat.

## Description

This application is built using Streamlit and TensorFlow. It uses a pre-trained model to predict whether the uploaded image is of a dog or a cat.

## How to Use

1. Clone the repository or download the files.
2. Install the necessary Python libraries (if not already installed) by running:

    ```bash
    pip install -r requirements.txt
    ```

    ```bash
    pip install streamlit tensorflow matplotlib
    ```

3. Place your trained model file (e.g., `InceptionV3.h5`) in the `best_model` directory.
4. Run the application by executing the command:

    ```bash
    streamlit run your_file.py
    ```

5. Once the application is running, you can upload an image file (in JPG, JPEG, or PNG format) using the "Upload an image of a dog or a cat" button.
6. After uploading the image, click the "Predict" button to predict whether the image contains a dog or a cat.

## Requirements

- Streamlit
- TensorFlow
- opencv-python
- tqdm

## File Structure

The file structure should look like this:

- best_model/
    - InceptionV3.h5
    - ResNet101.h5
    - VGG16.h5
    - DenseNet.h5
- web_app.py
- README.md


## Notes

- Make sure the image uploaded is clear and contains a dog or a cat to get an accurate prediction.
- The trained model file (e.g., `InceptionV3.h5`) must be placed in the `best_model` directory for the application to work correctly.
