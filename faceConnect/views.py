from . import email_sender
from .face_recognizer import encode_faces, recognize_and_label_faces_v2
from django.shortcuts import render, redirect, HttpResponse
from .models import UserIndividualImage, UserMultipleImage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
import numpy as np
import base64
import json
import io


def upload_individuals(request):
	if request.method == 'POST':
		images = request.FILES.getlist('images')
		names = request.POST.getlist('name')
		mobile_numbers = request.POST.getlist('mobile_number')
		emails = request.POST.getlist('email')

		for i, file in enumerate(images):
			print(f"i:{i} | file: {file}")
			try:
				face_encoding = encode_faces(file)[0]  # Assumes encode_faces can handle Django file objects
				if face_encoding is not None:
					# Create a new UserIndividualImage instance and populate fields
					new_image = UserIndividualImage(
						i_image=file, 
						mobile_number=mobile_numbers[i] if i < len(mobile_numbers) else None,
						email=emails[i] if i < len(emails) else None,
						name=names[i] if i < len(names) else None  # Assuming you have a 'name' field in your model
					)
					new_image.set_numpy_array(face_encoding)  # Assuming this method exists to handle numpy array storage
					new_image.save()
				else:
					print("No faces detected in the image.")
			except Exception as e:
				print(f"Error processing file {file.name}: {e}")
				return HttpResponse(f"Error processing file {file.name}: {e}", status=400)

		return redirect(to="detection/", status=200)
	else:
		return render(request, 'faceConnect/upload_images.html')



def get_known_encodings():
	"""
	Retrieve all face encodings and their associated metadata from the database.
	:return: List of tuples (encoding, metadata_dict)
	"""
	known_encodings_with_meta = []
	individuals = UserIndividualImage.objects.all()
	for individual in individuals:
		encoding = individual.get_numpy_array()  # Assuming this is how numpy arrays are stored and retrieved
		metadata = {
			'name': individual.name,
			'mobile_number': individual.mobile_number,
			'email': individual.email
		}
		known_encodings_with_meta.append((encoding, metadata))
	return known_encodings_with_meta

def detect_individuals(request):
	if request.method == 'POST':
		known_encodings_with_meta = get_known_encodings()
		print("known_encodings_with_meta: ", known_encodings_with_meta)
		detected_faces = {}
		for file in request.FILES.getlist('group_images'):
			print("file: ", file)
			try:
				current_image_encoding = encode_faces(file)  # Assumes encode_faces can handle Django file objects
				new_image = UserMultipleImage(m_image=file)
				new_image.set_numpy_array(current_image_encoding)  # Assuming this method exists to handle numpy array storage
				new_image.save()

				detected_faces[new_image.m_image.name] = {
					'url' : new_image.m_image.storage.url(new_image.m_image.name),
					'faces_found' : [meta for _, meta in recognize_and_label_faces_v2(current_image_encoding, known_encodings_with_meta)]
				}

				print("detected_faces: ", detected_faces)

			except Exception as e:
				print(f"Error processing file {file.name}: {e}")
				return HttpResponse(f"Error processing file {file.name}: {e}", status=400)

		return render(request, 'faceConnect/share_image.html', context={
			'detected_faces': detected_faces
		})

	return render(request, 'faceConnect/detection.html')




@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        emails = [email.replace("Email: ", "") for email in data.get('emails', [])]
        image_url = data.get('imageUrl', '')

        # Assuming your send_emails_concurrently function accepts emails, subject, body
        if emails and image_url:
            email_subject = "Photo Available for Download"
            email_body = f"Please download the image from the following link: {image_url}"
            email_sender.send_emails_concurrently(emails, email_subject, email_body, image_url)

            return JsonResponse({'message': 'Emails have been sent successfully!'}, status=200)
        else:
            return JsonResponse({'message': 'Missing email addresses or image URL'}, status=400)

    return JsonResponse({'message': 'Invalid request'}, status=400)

