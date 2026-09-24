# Face Recognition Attendance System

Automatic classroom attendance on a Raspberry Pi. A USB camera recognizes students' faces in real time, marks them present, and emails the attendance report when class ends.

> Built in 2020 as an IoT + computer vision project.

## How It Works

1. **Enroll** – `dataset.py` captures 30 face images for each student ID.
2. **Train** – `training.py` trains an OpenCV LBPH face recognizer and saves it to `trainer.yml`.
3. **Take attendance** – `recognition.py` watches the camera until the class stop time, marks recognized students present, and emails the present and absent lists.

## Tech Stack

- Python 3
- OpenCV (Haar cascade face detection + LBPH face recognition)
- Raspberry Pi + USB camera
- SMTP (Gmail) for the report email

## Project Structure

```
dataset.py         # capture face images for a student
training.py        # train the face recognizer
recognition.py     # live recognition + email report
requirements.txt   # Python dependencies
```

## Getting Started

### 1. Install

```bash
pip install -r requirements.txt
mkdir data dataset
```

Download `haarcascade_frontalface_default.xml` from the [OpenCV repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) into the `data/` folder.

### 2. Configure email

Set these environment variables. Use a Gmail **app password**, never your real account password.

```bash
export ATTENDANCE_EMAIL="you@gmail.com"
export ATTENDANCE_EMAIL_PASSWORD="your-app-password"
export ATTENDANCE_REPORT_TO="teacher@example.com"
```

### 3. Run

```bash
python dataset.py       # run once per student
python training.py
python recognition.py
```

Edit the `names` list and the `stop` time at the top of `recognition.py` to match your class.

## Limitations and Future Work

- Accuracy drops with poor lighting, partial faces, or crowded rooms.
- Support multiple IP cameras and merge their results for larger classrooms.
- Save attendance to a database instead of email only.
