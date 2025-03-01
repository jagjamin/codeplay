import cv2
import serial

# 시리얼 포트 설정 (아두이노와 연결된 포트로 변경)
ser = serial.Serial('COM6', 9600)

# 얼굴 인식 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # 얼굴이 인식되면 아두이노에 신호 전송
        ser.write(b'1')

    cv2.imshow('img', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()



'''

#include <Servo.h>

const int buttonPinA0 = A0; // A0 핀에 3개의 버튼 연결
const int buttonPinA1 = A1; // A1 핀에 3개의 버튼 연결
const int buttonPinA2 = A2; // A2 핀에 3개의 버튼 연결
const int buttonPinA3 = A3; // A3 핀에 3개의 버튼 연결
const int buzzerPin = 10; // 피에조 부저 핀
Servo myservo; // 서보 모터 객체 생성

int password[4] = {1, 2, 3, 4}; // 초기 비밀번호 설정
int inputPassword[4]; // 입력된 비밀번호 저장
int inputIndex = 0; // 입력된 비밀번호 인덱스
bool faceDetected = false; // 얼굴 인식 여부

void setup() {
  Serial.begin(9600); // 시리얼 통신 시작
  pinMode(buzzerPin, OUTPUT); // 부저 핀을 출력으로 설정
  myservo.attach(9); // 서보 모터 핀 설정
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      faceDetected = true;
    }
  }

  if (faceDetected) {
    int buttonValueA0 = analogRead(buttonPinA0);
    int buttonValueA1 = analogRead(buttonPinA1);
    int buttonValueA2 = analogRead(buttonPinA2);
    int buttonValueA3 = analogRead(buttonPinA3);

    if (buttonValueA0 < 50) {
      handleButtonPress(1);
    } else if (buttonValueA0 < 150) {
      handleButtonPress(2);
    } else if (buttonValueA0 < 950) {
      handleButtonPress(3);
    } else if (buttonValueA1 < 50) {
      handleButtonPress(4);
    } else if (buttonValueA1 < 150) {
      handleButtonPress(5);
    } else if (buttonValueA1 < 950) {
      handleButtonPress(6);
    } else if (buttonValueA2 < 50) {
      handleButtonPress(7);
    } else if (buttonValueA2 < 150) {
      handleButtonPress(8);
    } else if (buttonValueA2 < 950) {
      handleButtonPress(9);
    } else if (buttonValueA3 < 50) {
      handleButtonPress('*');
    } else if (buttonValueA3 < 150) {
      handleButtonPress(0);
    } else if (buttonValueA3 < 950) {
      handleButtonPress('#');
    }
    delay(100); // 버튼 읽기 주기
  }
}

void handleButtonPress(int button) {
  tone(buzzerPin, 1000, 100); // 버튼을 누를 때마다 비프음
  inputPassword[inputIndex] = button;
  inputIndex++;

  if (inputIndex == 4) {
    if (checkPassword()) {
      tone(buzzerPin, 2000, 500); // 띠리리~ 효과음
      myservo.write(180); // 서보 모터 180도 회전
      delay(5000); // 5초 대기
      myservo.write(0); // 서보 모터 원위치
      faceDetected = false; // 얼굴 인식 상태 초기화
    } else {
      tone(buzzerPin, 500, 500); // 비밀번호 틀렸을 때 효과음
    }
    inputIndex = 0; // 입력 인덱스 초기화
  }
}

bool checkPassword() {
  for (int i = 0; i < 4; i++) {
    if (inputPassword[i] != password[i]) {
      return false;
    }
  }
  return true;
}

'''