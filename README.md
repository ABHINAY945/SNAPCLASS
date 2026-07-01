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
