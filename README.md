<div align="center">

# 📸 SnapClass

### 🚀 AI-Powered Smart Attendance Management System using Face Recognition & Voice Recognition

<p align="center">
Streamline classroom attendance with Computer Vision, Speaker Recognition, and Cloud Database Integration.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-blue?style=for-the-badge)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-orange?style=for-the-badge)
![Voice Recognition](https://img.shields.io/badge/Voice-Recognition-success?style=for-the-badge)

</p>

<p align="center">

<a href="https://github.com/ABHINAY945/SnapClass">Repository</a> •
<a href="https://your-streamlit-app.streamlit.app">Live Demo</a> •
<a href="https://youtu.be/your-demo-video">Demo Video</a>

</p>

---

<img src="https://i.ibb.co/YTYGn5qV/logo.png" width="180">

### Making Attendance Faster using Artificial Intelligence

</div>

---

# 📖 Overview

SnapClass is an AI-powered attendance management system designed to modernize classroom attendance by combining **Face Recognition**, **Voice Recognition**, and **Cloud Database Management** into one intuitive platform.

Instead of manually marking attendance, teachers can capture classroom photos or record classroom audio, allowing AI to automatically identify students and generate attendance records.

The system also provides students with secure FaceID login, optional voice enrollment, attendance tracking, and seamless course enrollment through QR codes or join links.

---

# ✨ Key Features

## 👨‍🎓 Student Features

- 🔐 Face Recognition Login
- 📝 Automatic Student Registration
- 🎤 Optional Voice Enrollment
- 📚 Subject Enrollment using Subject Code
- 🔗 One-click Enrollment via Shared Link
- 📱 QR Code Based Enrollment
- 📊 Attendance Statistics
- 🚪 Unenroll from Subjects
- 👤 Personalized Dashboard

---

## 👨‍🏫 Teacher Features

- 🔐 Secure Login System
- 📝 Teacher Registration
- 📚 Create Subjects
- 📤 Share Subject Code
- 📱 Generate QR Codes
- 📷 Capture Classroom Photos
- 🖼 Upload Multiple Classroom Images
- 😀 AI Face Attendance
- 🎤 AI Voice Attendance
- 📈 Attendance Reports
- 📊 Student Statistics

---

## 🤖 AI Features

- Face Detection
- Facial Landmark Detection
- Face Embedding Generation
- Linear SVM Classification
- Voice Embedding Generation
- Speaker Recognition
- Multi-Face Detection
- Multi-Image Attendance Processing
- Automatic Classifier Retraining

---

## ☁️ Cloud Features

- Supabase Database
- Secure Password Hashing
- Attendance History
- Subject Management
- Student Management
- Teacher Management

---

# 🌟 Why SnapClass?

Traditional attendance systems suffer from:

- Manual attendance
- Proxy attendance
- Time consumption
- Human errors

SnapClass solves these problems by combining **Computer Vision** and **Speaker Recognition** to automate attendance while providing a smooth user experience through an intuitive web interface.

---


# 🏗️ System Architecture

```text
                           SnapClass
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
   Home Screen            Student Portal          Teacher Portal
        │                       │                        │
        │                Face Authentication      Password Login
        │                       │                        │
        └───────────────┬───────┴─────────────┬──────────┘
                        │                     │
                  Face Pipeline        Voice Pipeline
                        │                     │
                        └──────────┬──────────┘
                                   │
                            Supabase Database
                                   │
          ┌────────────────────────┼─────────────────────────┐
          │                        │                         │
      Students                 Teachers                 Subjects
                                   │
                          Attendance Logs
```

---

# 🧠 How It Works

## Student Workflow

```text
Open SnapClass

        │

Student Portal

        │

Capture Face

        │

Face Recognition

        │
 ┌──────┴────────┐
 │               │
Known        Unknown
Student      Student
 │               │
 │         Register Face
 │         + Voice (Optional)
 │               │
 └──────┬────────┘
        │
Student Dashboard
        │
View Subjects
Attendance
Enroll Courses
```

---

## Teacher Workflow

```text
Teacher Login

      │

Dashboard

      │

Create Subject

      │

Share QR / Join Link

      │

Take Attendance

      │

Upload Photos
or
Record Audio

      │

AI Recognition

      │

Attendance Preview

      │

Confirm Attendance

      │

Attendance Stored
```

---

# 🤖 Face Recognition Pipeline

SnapClass performs attendance using **facial embeddings** rather than comparing raw images.

```text
Classroom Image

      │

Face Detection
(dlib)

      │

Facial Landmark Detection

      │

128-D Face Embeddings

      │

Linear SVM Classifier

      │

Distance Verification

      │

Recognized Students

      │

Attendance Report
```

### Face Recognition Technologies

- dlib Face Detector
- Facial Landmark Predictor
- Face Recognition Model
- 128-D Face Embeddings
- Scikit-Learn Linear SVM
- Euclidean Distance Matching

### Performance Optimizations

- Cached AI models
- Automatic classifier retraining
- Multi-face detection
- Multi-image classroom scanning

---

# 🎤 Voice Recognition Pipeline

Students can optionally register a voice profile.

During attendance, teachers record classroom audio and the system identifies speakers.

```text
Audio Recording

      │

Librosa Audio Processing

      │

Speech Segmentation

      │

Resemblyzer Encoder

      │

Voice Embeddings

      │

Cosine Similarity Matching

      │

Recognized Speakers

      │

Attendance Report
```

### Voice Technologies

- Resemblyzer
- Librosa
- Speaker Embeddings
- Cosine Similarity Matching

---

# 🗄️ Database Design

SnapClass uses **Supabase** as the cloud backend.

### Teachers

| Field | Description |
|-------|-------------|
| teacher_id | Unique Teacher ID |
| username | Login Username |
| password | bcrypt Hashed Password |
| name | Teacher Name |

---

### Students

| Field | Description |
|-------|-------------|
| student_id | Unique Student ID |
| name | Student Name |
| face_embedding | Face Feature Vector |
| voice_embedding | Voice Feature Vector |

---

### Subjects

| Field | Description |
|-------|-------------|
| subject_id | Subject ID |
| subject_code | Unique Join Code |
| name | Subject Name |
| section | Section |
| teacher_id | Owner Teacher |

---

### Subject Students

Many-to-Many Mapping

```text
Students
     │
     │
Subject_Students
     │
     │
Subjects
```

---

### Attendance Logs

| Field | Description |
|-------|-------------|
| student_id | Student |
| subject_id | Subject |
| timestamp | Attendance Time |
| is_present | Present/Absent |

---

# 📂 Project Structure

```text
SNAPCLASS
│
├── .streamlit/
│   └── secrets.toml
│
├── src/
│   ├── components/
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── teacher_screen.py
│   │   └── student_screen.py
│   │
│   └── ui/
│       └── base_layout.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit
- HTML
- CSS
- Google Fonts

---

## Backend

- Python

---

## Machine Learning

- Scikit-Learn
- Linear SVM

---

## Computer Vision

- dlib
- face_recognition_models

---

## Speaker Recognition

- Resemblyzer
- Librosa

---

## Database

- Supabase

---

## Authentication

- bcrypt

---

## Utilities

- NumPy
- Pandas
- Pillow
- Segno

---

# 🔒 Security Features

- Passwords secured using **bcrypt hashing**
- Teacher authentication with encrypted passwords
- Face embedding verification before login
- Voice similarity threshold verification
- Duplicate enrollment prevention
- Attendance confirmation before saving
- Session-based authentication using Streamlit Session State

---


# 🚀 Getting Started

Follow these steps to run SnapClass locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ABHINAY945/SnapClass.git
cd SnapClass
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Supabase

Create the following file:

```
.streamlit/secrets.toml
```

Add your Supabase credentials:

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
```

> ⚠️ Never commit `secrets.toml` to GitHub.

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

The application will start on:

```
http://localhost:8501
```

---

# 📖 Usage Guide

## 👨‍🏫 Teacher

### Register

- Create a teacher account.
- Login using your username and password.

### Create Subject

- Click **Create Subject**
- Enter:
  - Subject Code
  - Subject Name
  - Section

### Share Class

Generate:

- Subject Code
- Join Link
- QR Code

Students can join using any of these.

---

### Face Attendance

1. Select Subject
2. Capture classroom photos OR upload images
3. Run AI Face Analysis
4. Review attendance
5. Save attendance

---

### Voice Attendance

1. Select Subject
2. Record classroom audio
3. Analyze audio
4. Review identified students
5. Save attendance

---

## 👨‍🎓 Student

### Login

Open Student Portal.

Capture your face.

If recognized:

- Login successful.

Otherwise:

- Register new profile.

---

### Registration

Provide:

- Name
- Face Image
- (Optional) Voice Sample

SnapClass automatically creates your profile.

---

### Enroll in Subject

You can join using:

- Subject Code
- Shared Link
- QR Code

---

### Dashboard

Students can

- View enrolled subjects
- View attendance statistics
- Unenroll from courses

---

# 📸 Screenshots

> Add screenshots inside an **assets/** folder.

```
assets/
│
├── home.png
├── teacher_dashboard.png
├── student_dashboard.png
├── create_subject.png
├── face_attendance.png
├── voice_attendance.png
├── attendance_report.png
└── qr_join.png
```

---

## Home Page

![Home](assets/home.png)

---

## Teacher Dashboard

![Teacher Dashboard](assets/teacher_dashboard.png)

---

## Student Dashboard

![Student Dashboard](assets/student_dashboard.png)

---

## Face Attendance

![Face Attendance](assets/face_attendance.png)

---

## Voice Attendance

![Voice Attendance](assets/voice_attendance.png)

---

## Attendance Report

![Attendance Report](assets/attendance_report.png)

---

## QR Code Enrollment

![QR Join](assets/qr_join.png)

---

# 🎯 Project Highlights

✅ AI-powered Face Authentication

✅ AI-powered Voice Attendance

✅ QR Code Enrollment

✅ Join Link Enrollment

✅ Classroom Image Processing

✅ Multiple Image Attendance

✅ Speaker Recognition

✅ Attendance Analytics

✅ Automatic Classifier Training

✅ Cloud Database Integration

✅ Modern Dashboard UI

---

# 🌐 Deployment

### Live Application

```
https://snapclass-genz-coders.streamlit.app/
```

---

### Demo Video

```
https://youtu.be/your-demo-video
```

---

### GitHub Repository

```
https://github.com/ABHINAY945/SnapClass
```

---

# 📈 Future Improvements

- 📊 Attendance Analytics Dashboard
- 📈 Attendance Graphs
- 📄 Export Attendance to PDF
- 📥 Export Attendance to Excel
- 📧 Email Notifications
- 📱 Mobile Responsive Interface
- 🎥 Video-based Attendance
- 🌍 Multi-language Support
- 🧑‍💼 Admin Dashboard
- 🔔 Push Notifications
- 🧠 Deep Learning Face Recognition (FaceNet / ArcFace)
- ☁️ Docker Deployment
- 📅 Timetable Integration
- 📍 GPS-Based Attendance Verification
- 🧾 Attendance Certificates

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 🐞 Known Limitations

- Face recognition performance depends on image quality.
- Voice recognition accuracy decreases in noisy environments.
- Internet connectivity is required for database synchronization.
- Large classrooms may require multiple images for better accuracy.

---

# 📚 Acknowledgements

This project uses several amazing open-source libraries:

- Streamlit
- Supabase
- dlib
- face_recognition_models
- Resemblyzer
- Librosa
- Scikit-learn
- Pillow
- NumPy
- Pandas
- bcrypt
- Segno

Huge thanks to the maintainers of these projects.

---

# 👨‍💻 Author

### Abhinay Srivastava

B.Tech Information Technology

IIIT Bhopal

📧 Email

```
abhinay.soft06@gmail.com
```

💼 LinkedIn

```
https://www.linkedin.com/in/abhinay-srivastava-bb0206290/
```

🐙 GitHub

```
https://github.com/ABHINAY945
```

---

# ⭐ Support

If you found this project useful,

please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

<div align="center">

### 🚀 Built with Python, Streamlit, Machine Learning & ❤️

**SnapClass — Making Attendance Faster using Artificial Intelligence**

</div>
