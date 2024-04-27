import face_recognition

def encode_faces(image):
	"""
	This function takes an image file and returns the face encodings for all detected faces in the image.
	:param image: An image file that contains one or more faces.
	:return: A list of face encodings (each encoding is a numpy array).
	"""
	try:
		# Load the image into a numpy array
		image_array = face_recognition.load_image_file(image)
		# Get face encodings for any faces in the uploaded image
		encodings = face_recognition.face_encodings(image_array)
		print("encoding: ", encodings)
	except:
		return None
	return encodings



def recognize_and_label_faces_v2(current_image_encodings, known_encodings_with_meta, image):
    """
    Recognize faces from an image and label them using a list of known encodings with metadata.
    :param current_image_encodings: List of face encodings detected in the current image.
    :param known_encodings_with_meta: List of tuples, each containing an encoding and its associated metadata.
    :param image: The image file where faces are being recognized.
    :return: List of detected encodings with corresponding metadata and face locations.
    """
    detected_faces_with_meta = []
    # Load the image to find face locations
    image_array = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(image_array)

    for index, encoding in enumerate(current_image_encodings):
        result = face_recognition.compare_faces([ke for ke, _ in known_encodings_with_meta], encoding, tolerance=0.4)
        print("result: ", result)
        for i, match in enumerate(result):
            if match:
                # Append encoding, metadata, and face location
                detected_faces_with_meta.append((known_encodings_with_meta[i][0], known_encodings_with_meta[i][1], face_locations[index]))
                break

    return detected_faces_with_meta