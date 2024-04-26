# FaceConnect

## Project Goal
Recognizes the people in a photo and sends them that photo via email.

## Installation Steps

### 1. Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone git@github.com:Anurag9689/FaceConnect.git
```

### 2. Navigate to the Cloned Repository
Change directory to the cloned repository:
```bash
cd FaceConnect
```

### 3. Create a Python Virtual Environment
Create a Python virtual environment to manage the dependencies:

#### For Linux/macOS:
```bash
python3 -m venv env
```

#### For Windows:
```cmd
python -m venv env
```

### 4. Activate the Virtual Environment

#### For Linux/macOS:
```bash
source env/bin/activate
```

#### For Windows:
```cmd
env\Scripts\activate
```

### 5. Install the dependencies
```bash
pip3 install -r requirements.txt
```


### 6. Copy Local Settings
Copy the sample local settings file to create your local configuration:
```bash
cp FaceConnect/sample_local_settings.py FaceConnect/local_settings.py
```
#### For Windows:
```cmd
copy FaceConnect\sample_local_settings.py FaceConnect\local_settings.py
```

### 7. Set Credentials in `local_settings.py`
Open `local_settings.py` and set the required credentials and settings. Look for `TODO` comments in the file to find what needs to be replaced or filled.

### 8. Apply Migrations
Apply the Django database migrations:
```bash
python3 manage.py migrate
```

### 9. Create a Superuser
Create an administrative user for the Django admin:
```bash
python3 manage.py createsuperuser
```

### 10. Run the Development Server
Run the development server to start the application:
```bash
python3 manage.py runserver 0:8000
```

## Usage
Access the application through `http://localhost:8000` in your web browser.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests with any enhancements or bug fixes.




# Project working

### **Project Overview: FaceConnect**
- **Goal**: FaceConnect is designed to recognize individuals from a set of uploaded images and automatically send them an email with a link to download the image in which they were recognized.

### **Key Functionalities and Workflow:**
1. **Image Upload**:
   - Users start by uploading one or more individual images through the `upload_individuals` view.
   - Each uploaded image is processed to detect faces and extract face encodings using the `encode_faces` function from the `face_recognizer` module.

2. **Face Detection**:
   - Users can upload group images via the `detect_individuals` view.
   - The application utilizes previously stored face encodings to recognize and label faces in the new group images using the `recognize_and_label_faces_v2` function.
   - Detected faces and their metadata (e.g., name, email) are compiled and displayed on the `share_image.html` template for user interaction.

3. **Email Notification**:
   - After recognizing faces, the application facilitates sending personalized emails to the individuals recognized in the images.
   - Emails are sent concurrently using the `send_emails_concurrently` function from the `email_sender` module, which utilizes multi-threading to enhance performance and responsiveness.
   - Each email contains a link allowing the recipient to download the image they appear in.

### **Technical Details:**
- **Face Recognition**:
  - Built using the `face_recognition` library to handle the complex task of face detection and recognition efficiently.
  - Includes robust encoding and matching algorithms to ensure accurate identification with minimal false positives.

- **Concurrent Email Dispatch**:
  - Uses Python threading to manage simultaneous sending of multiple emails, ensuring that the application remains responsive and scalable.

- **Django Framework**:
  - Utilizes Django’s robust framework for handling web requests, routing, model management, and template rendering.
  - Ensures a secure and scalable backend, suitable for handling sensitive data and user interactions.

### **Security and Compliance**:
- Ensures data protection and privacy, crucial for handling personal data such as names, emails, and biometric data (faces).
- Implements CSRF protection and secure handling of file uploads and personal data, aligning with best practices and potentially GDPR requirements.

### **Presentation Strategy for Hackathon**:
- **Problem Statement and Solution**: Clearly define the problem your project addresses and how FaceConnect provides a novel solution.
- **Demonstration**: Plan a live demo or a detailed walkthrough of the project, showcasing the ease of uploading images, the effectiveness of the face recognition, and the simplicity of the email notification system.
- **Impact and Scalability**: Highlight how the project can be scaled and its potential impact on various sectors, including security, personal media management, and social networking.
