#include <Wire.h>
#include <SPI.h>
#include <Adafruit_LSM9DS0.h>
#include <Adafruit_Sensor.h>
#include <Mouse.h>


// ################ 	SETTINGS	 ################
//


int calX = 735;			// Calibration values
int calY = 355;

int interval = 2;		// Milliseconds between samples

int maxOut = 50;

//
// ################ 	/SETTINGS	 ################


Adafruit_LSM9DS0 lsm = Adafruit_LSM9DS0();
int maxIn = 32760;
int minIn = -32760;
long loopTimer = millis();

void setupSensor()
{
	// 1.) Set the accelerometer range
	lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_2G);
	//lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_2G);
	//lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_4G);
	//lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_6G);
	//lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_8G);
	//lsm.setupAccel(lsm.LSM9DS0_ACCELRANGE_16G);

	// 2.) Set the magnetometer sensitivity
	lsm.setupMag(lsm.LSM9DS0_MAGGAIN_2GAUSS);
	//lsm.setupMag(lsm.LSM9DS0_MAGGAIN_2GAUSS);
	//lsm.setupMag(lsm.LSM9DS0_MAGGAIN_4GAUSS);
	//lsm.setupMag(lsm.LSM9DS0_MAGGAIN_8GAUSS);
	//lsm.setupMag(lsm.LSM9DS0_MAGGAIN_12GAUSS);

	// 3.) Setup the gyroscope
	lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_2000DPS);
	//lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_245DPS);
	//lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_500DPS);
	//lsm.setupGyro(lsm.LSM9DS0_GYROSCALE_2000DPS);
}

void setup() {
	Mouse.begin();
	lsm.begin();
	Serial.begin(115200);
	delay(2000);
	Serial.println("Start");
}


void loop() {
	if (millis() - loopTimer >= interval) {

	lsm.read();

	/*
	int accX = map(lsm.accelData.x, minIn, maxIn, (maxOut * -1), maxOut);
	int accY = map(lsm.accelData.y, minIn, maxIn, (maxOut * -1), maxOut);
	int accZ = map(lsm.accelData.z, minIn, maxIn, (maxOut * -1), maxOut);

	int magX = map(lsm.magData.x, minIn, maxIn, (maxOut * -1), maxOut);
	int magY = map(lsm.magData.y, minIn, maxIn, (maxOut * -1), maxOut);
	int magZ = map(lsm.magData.z, minIn, maxIn, (maxOut * -1), maxOut);
	*/

	int gyroX = map((lsm.gyroData.x), minIn, maxIn, (maxOut * -1), maxOut);
	int gyroY = map((lsm.gyroData.y + calY), minIn, maxIn, (maxOut * -1), maxOut);
	int gyroZ = map((lsm.gyroData.z + calX), minIn, maxIn, (maxOut * -1), maxOut);

	while (Serial.available()) {
		char letter = (char)Serial.read();
		if (letter == 'X') {
			calX += 1;
			Serial.print("X:");
			Serial.println(calX);
		} else if (letter == 'x') {
			if (calX > 1) {
				calX -= 1;
			}
			Serial.print("X:");
			Serial.println(calX);
		} else if (letter == 'Y') {
			calY += 1;
			Serial.print("Y:");
			Serial.println(calY);
		} else if (letter == 'y') {
			if (calY > 1) {
				calY -= 1;
			}
			Serial.print("Y:");
			Serial.println(calY);
		} else if (letter == 'M') {
			maxOut += 1;
			Serial.print("M:");
			Serial.println(maxOut);
		} else if (letter == 'm') {
			if (maxOut > 1) {
				maxOut -= 1;
			}
			Serial.print("M:");
			Serial.println(maxOut);
		}
	}

	/*
	Serial.print(lsm.gyroData.x);
	Serial.print(" ");
	Serial.print(lsm.gyroData.y);
	Serial.print(" ");
	Serial.println(lsm.gyroData.z);

	Serial.print(gyroX);
	Serial.print(" ");
	Serial.print(gyroY);
	Serial.print(" ");
	Serial.print(gyroZ);
	Serial.println(" ");

	Serial.print((int)accX);
	Serial.print(",");
	Serial.print((int)accY);
	Serial.print(",");
	Serial.print((int)accZ);
	Serial.print(" ");

	Serial.print((int)magX);
	Serial.print(",");
	Serial.print((int)magY);
	Serial.print(",");
	Serial.print((int)magZ);
	Serial.print(" ");

	Serial.print((int)gyroX);
	Serial.print(",");
	Serial.print((int)gyroY);
	Serial.print(",");
	Serial.print((int)gyroZ);
	Serial.println("");

	*/

	Mouse.move(gyroZ, gyroY);
	loopTimer = millis();
	}
}
