# Road Lane Detection using OpenCV

## Overview

Road Lane Detection is a Computer Vision project that detects road lane boundaries in images using Python and OpenCV.

The system processes an input road image through multiple image processing stages and produces an output image with the detected left and right lane boundaries highlighted.

## Features

- Road lane detection from images
- Grayscale conversion
- Gaussian Blur
- Canny Edge Detection
- Region of Interest (ROI) masking
- Hough Line Transform
- Left and right lane separation
- Lane visualization
- Intermediate image generation
- Command-line execution

## Technologies Used

- Python
- OpenCV
- NumPy

## Computer Vision Pipeline

Input Road Image
        ↓
Grayscale Conversion
        ↓
Gaussian Blur
        ↓
Canny Edge Detection
        ↓
Region of Interest
        ↓
Hough Line Transform
        ↓
Left/Right Lane Separation
        ↓
Lane Visualization
        ↓
Output Image

## Project Structure

Road-lane-detection/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── input/
│   └── road_image1.jpg
│
└── output/
    ├── grayscale.jpg
    ├── edges.jpg
    ├── roi.jpg
    └── lane_detected.jpg

## Requirements

- Python 3.x
- OpenCV
- NumPy

All required Python packages are listed in requirements.txt.

## Installation

Clone the repository:

git clone https://github.com/ParthGupta0806/Road-lane-detection.git

cd Road-lane-detection

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

## Usage

Run the program by providing the path to the input road image:

python main.py input/road_image1.jpg

The final lane detection result will be saved as:

output/lane_detected.jpg

You can also process another road image by providing its path:

python main.py input/another_road.jpg

You can specify a custom output location:

python main.py input/road_image1.jpg --output output/my_result.jpg

## Results

### 1. Original Input

<img width="612" height="413" alt="road_image1" src="https://github.com/user-attachments/assets/deca91d0-f372-4dae-98bf-6024fa710242" />


### 2. Grayscale Image

<img width="612" height="413" alt="image" src="https://github.com/user-attachments/assets/c6a0bed9-acc3-4c79-a2c6-2c417e3fdb8d" />


### 3. Canny Edge Detection

<img width="612" height="413" alt="image" src="https://github.com/user-attachments/assets/618450f1-9b4a-449e-b8ea-3b676a26c0d6" />


### 4. Region of Interest

<img width="612" height="413" alt="image" src="https://github.com/user-attachments/assets/c187337a-956c-4652-bead-282c68ab3350" />


### 5. Final Lane Detection

<img width="612" height="413" alt="image" src="https://github.com/user-attachments/assets/9c93990b-f374-43f3-99d2-99816527bcf6" />


## Limitations

The current implementation is optimized for relatively straight roads with clearly visible lane markings.

Detection performance may decrease with:

- Sharply curved roads
- Poor lighting
- Heavy shadows
- Faded lane markings
- Rain or fog
- Obstructions on the road

## Future Improvements

- Support for curved lane detection
- Real-time lane detection from video
- Improved detection under different lighting conditions
- More robust lane tracking
- Improved performance in complex road environments

## Conclusion

This project demonstrates a basic Computer Vision pipeline for road lane detection using OpenCV. It combines image preprocessing, edge detection, region-based filtering, and Hough Line Transform to identify and visualize lane boundaries.

## Author

Parth Gupta
