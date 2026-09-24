**Overview**(Created on 2020)

This project proposes an automated attendance system using face recognition, designed to streamline the attendance-taking process in educational environments. Traditional manual attendance methods are time-consuming and disruptive to class productivity. This system leverages real-time face detection and recognition using a Raspberry Pi and the OpenCV framework to efficiently record student attendance.

**How It Works**
The system operates by:

Student Face Data Pre-storage: Student faces are pre-stored in a class database.

Real-time Capture: A USB camera captures student faces in real-time.

Face Comparison & Recognition: Captured faces are compared against the pre-stored database.

Automated Attendance: If a match is found, the student is marked as present. Attendance data is then sent via email.

This automated approach aims to significantly reduce the time spent on attendance, allowing for more productive teaching and learning.

**Key Features**
Automated Attendance: Eliminates manual attendance taking.

Face Recognition: Utilizes an efficient algorithm with OpenCV for real-time face detection and recognition.

Raspberry Pi Integration: Deploys the system on a cost-effective Raspberry Pi.

Improved Efficiency: Maximizes teaching time by minimizing attendance-related delays.

Enhanced Security: Provides a more secure and discreet attendance recording method.

**Experimental Results**
The system's functionality is demonstrated through the execution of three core Python programs: dataset.py, training.py, and recognition.py.

1. dataset.py
This program is responsible for collecting and storing student face data for training purposes. Users enter a unique ID and look at the camera to capture images, which form the dataset.

Input: Unique student ID.

Output: Captured images stored for the dataset.

2. training.py
After the dataset is created, training.py processes and trains the facial recognition model. Upon successful execution, it displays information about the number of faces trained.

Input: Stored image data from dataset.py.

Output: A trained facial recognition model, with a confirmation of the number of faces trained.

3. recognition.py
This is the main attendance recording program. It continuously captures faces until a predefined "stop time." After this time, it displays and processes attendance data, separating present and absent students.

**Input: Live video feed from the USB camera.**

**Output: Real-time face recognition, with a final display of present and absent student data.**

**Conclusion**
This automated student attendance system addresses the inefficiencies of traditional methods by integrating face recognition. It aims to save effort and time for both teachers and students, improving the overall efficiency and security of the attendance management process. While existing facial recognition systems have limitations (e.g., accuracy, lighting), this proposed system strives to mitigate these challenges, leading to:

Minimizing attendance marking time.

Maximizing actual teaching time.

Increasing overall system efficiency.

Improving security by enabling discreet attendance.

**Future Scope**
The project has promising avenues for further development:

Higher Accuracy: The system's accuracy can be further improved for partial and dense images.

Multi-Camera Support: Integrating two or more IP cameras and merging their processed results can lead to better accuracy in denser classroom environments


## How to Run

1. Install dependencies (Raspberry Pi with a USB camera):
   ```bash
   pip install -r requirements.txt
   ```
2. Download `haarcascade_frontalface_default.xml` from the [OpenCV repo](https://github.com/opencv/opencv/tree/master/data/haarcascades) into a `data/` folder, and create an empty `dataset/` folder.
3. Set the email settings as environment variables (use a Gmail app password):
   ```bash
   export ATTENDANCE_EMAIL="you@gmail.com"
   export ATTENDANCE_EMAIL_PASSWORD="your-app-password"
   export ATTENDANCE_REPORT_TO="teacher@example.com"
   ```
4. Run the three steps in order:
   ```bash
   python dataset.py      # capture face images for each student ID
   python training.py     # train the recognizer (creates trainer.yml)
   python recognition.py  # take attendance and email the report
   ```
