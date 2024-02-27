import cv2

# Initialize webcam
# vary this index from 0 upwards to select webcam source
cap = cv2.VideoCapture(2)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Mirror the frame
    frame = cv2.flip(frame, 1)

    # Dimensions of the frame
    height, width, _ = frame.shape

    # Draw horizontal and vertical lines to divide the frame into a 3x3 grid
    cv2.line(frame, (width // 3, 0), (width // 3, height), (0, 255, 0), 1)
    cv2.line(frame, (2 * width // 3, 0), (2 * width // 3, height), (0, 255, 0), 1)
    cv2.line(frame, (0, height // 3), (width, height // 3), (0, 255, 0), 1)
    cv2.line(frame, (0, 2 * height // 3), (width, 2 * height // 3), (0, 255, 0), 1)

    # Show the frame with grid lines
    cv2.imshow('Mirrored Grid', frame)

    # Close window when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
