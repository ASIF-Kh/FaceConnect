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


# def recognize_and_label_faces(current_image_encodings, known_encodings_with_meta):
# 	"""
# 	Recognize faces from a list of images and label them using a list of known encodings with metadata.
# 	:param images: List of image files to be checked.
# 	:param known_encodings_with_meta: List of tuples, each containing an encoding and its associated metadata.
# 	:return: List of detected encodings with corresponding metadata.
# 	"""
# 	detected_faces_with_meta = []
# 	email_added = []

# 	for encoding in current_image_encodings:

# 		for known_encoding, meta in known_encodings_with_meta:
# 			result = face_recognition.compare_faces([known_encoding], encoding) # tolerance=0.6
# 			if any(result) and meta['email'] not in email_added:
# 				email_added.append(meta['email'])
# 				detected_faces_with_meta.append((encoding, meta))
# 				break
# 	return detected_faces_with_meta





def recognize_and_label_faces_v2(current_image_encodings, known_encodings_with_meta):
	"""
	Recognize faces from a list of images and label them using a list of known encodings with metadata.
	:param images: List of image files to be checked.
	:param known_encodings_with_meta: List of tuples, each containing an encoding and its associated metadata.
	:return: List of detected encodings with corresponding metadata.
	"""
	detected_faces_with_meta = []
	for encoding in current_image_encodings:
		result = face_recognition.compare_faces([ke for ke, _ in known_encodings_with_meta], encoding, tolerance=0.4)
		print("result: ", result)
		for i, match in enumerate(result):
			if match:
				detected_faces_with_meta.append(known_encodings_with_meta[i])
	return detected_faces_with_meta
