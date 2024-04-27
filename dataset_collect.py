import cv2
import os


output_dir = 'shaurya'


os.makedirs(output_dir, exist_ok=True)


cap = cv2.VideoCapture(0)


image_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the captured frame
    cv2.imshow('Frame', frame)
    
    # Wait for the 'q' key to be pressed to capture the image
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):

        image_count += 1
        image_name = f'image_{image_count}.jpg'
        image_path = os.path.join(output_dir, image_name)
        cv2.imwrite(image_path, frame)
        print(f'Saved {image_name}')
        
        if image_count >= 45:
            break

cap.release()
cv2.destroyAllWindows()
