import cv2
import numpy as np
import argparse


def region_of_interest(image):
    height, width = image.shape[:2]

    mask = np.zeros_like(image)

    polygon = np.array([
        [
            (0, height),
            (width, height),
            (int(width * 0.55), int(height * 0.60)),
            (int(width * 0.45), int(height * 0.60))
        ]
    ])

    cv2.fillPoly(mask, polygon, 255)

    return cv2.bitwise_and(image, mask)


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters

    height = image.shape[0]

    y1 = height
    y2 = int(height * 0.60)

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    return np.array([x1, y1, x2, y2])


def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []

    if lines is None:
        return []

    height, width = image.shape[:2]

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)

        if x2 == x1:
            continue

        slope, intercept = np.polyfit(
            (x1, x2),
            (y1, y2),
            1
        )

        if abs(slope) < 0.5:
            continue

        # Find where the detected line reaches the bottom of the image
        x_bottom = int((height - intercept) / slope)

        # Ignore lines near the center of the road
        if x_bottom < int(width * 0.45):
            left_fit.append((slope, intercept))

        elif x_bottom > int(width * 0.55):
            right_fit.append((slope, intercept))

    lane_lines = []

    if left_fit:
        left_average = np.average(left_fit, axis=0)
        lane_lines.append(
            make_coordinates(image, left_average)
        )

    if right_fit:
        right_average = np.average(right_fit, axis=0)
        lane_lines.append(
            make_coordinates(image, right_average)
        )

    return lane_lines


def display_lines(image, lines):
    line_image = np.zeros_like(image)

    if lines is not None:
        for line in lines:
            if len(line) == 4:
                x1, y1, x2, y2 = line

                cv2.line(
                    line_image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    10
                )

    return line_image


def detect_lanes(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    edges = cv2.Canny(
        blur,
        50,
        150
    )

    cropped_edges = region_of_interest(edges)

    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=50,
        maxLineGap=100
    )

    averaged_lines = average_slope_intercept(
        image,
        lines
    )

    line_image = display_lines(
        image,
        averaged_lines
    )

    result = cv2.addWeighted(
        image,
        0.8,
        line_image,
        1,
        1
    )

    return result, gray, edges, cropped_edges


def main():

    parser = argparse.ArgumentParser(
        description="Road Lane Detection using OpenCV"
    )

    parser.add_argument(
        "input",
        help="Path to the input road image"
    )

    parser.add_argument(
        "--output",
        default="output/lane_detected.jpg",
        help="Path to save the output image"
    )

    args = parser.parse_args()

    image = cv2.imread(args.input)

    if image is None:
        print(f"ERROR: Could not load image: {args.input}")
        return

    result, gray, edges, cropped_edges = detect_lanes(image)

    cv2.imwrite("output/grayscale.jpg", gray)
    cv2.imwrite("output/edges.jpg", edges)
    cv2.imwrite("output/roi.jpg", cropped_edges)
    cv2.imwrite(args.output, result)

    print("Lane detection completed successfully!")
    print(f"Input: {args.input}")
    print(f"Output: {args.output}")
    
    result, gray, edges, cropped_edges = detect_lanes(image)

    cv2.imwrite("output/grayscale.jpg", gray)
    cv2.imwrite("output/edges.jpg", edges)
    cv2.imwrite("output/roi.jpg", cropped_edges)
    cv2.imwrite("output/lane_detected.jpg", result)

    print("Lane detection completed successfully!")
    print("Files saved in the output folder.")


if __name__ == "__main__":
    main()