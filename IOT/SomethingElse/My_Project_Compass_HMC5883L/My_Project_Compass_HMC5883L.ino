#define ENB   D6          // Enable/speed motors Left         GPIO12(D6)
#define IN_3  D4          // L298N in3 motors Left            GPIO2(D4)
#define IN_4  D3          // L298N in4 motors Left            GPIO0(D3)
#define SERVO D5
#include <Wire.h>
#include <HMC5883L.h>
#include <MPU6050.h>
HMC5883L compass;
MPU6050 mpu;
#include <Servo.h>
int global_heading = 0; //use to save origin heading
int temp_global_heading = 0; //use to save currently heading
int default_compass = 91; //that is val of compass
Servo servo;
void setupOriginHeading()
{
  global_heading = round(readHeading());
}
void setupServo()
{
  servo.attach(D5);
  servo.write(default_compass);
}
void setupMotor()
{
 pinMode(ENB, OUTPUT);  
 pinMode(IN_3, OUTPUT);
 pinMode(IN_4, OUTPUT); 
}
void setupCompass()
{
   while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }

  mpu.setI2CMasterModeEnabled(false);
  mpu.setI2CBypassEnabled(true) ;
  mpu.setSleepEnabled(false);

  // Initialize Initialize HMC5883L
  Serial.println("Initialize HMC5883L");
  while (!compass.begin())
  {
    Serial.println("Could not find a valid HMC5883L sensor, check wiring!");
    delay(500);
  }

  // Set measurement range
  compass.setRange(HMC5883L_RANGE_1_3GA);

  // Set measurement mode
  compass.setMeasurementMode(HMC5883L_CONTINOUS);

  // Set data rate
  compass.setDataRate(HMC5883L_DATARATE_30HZ);

  // Set number of samples averaged
  compass.setSamples(HMC5883L_SAMPLES_8);

  // Set calibration offset. See HMC5883L_calibration.ino
  compass.setOffset(0, 0); 
}
void setup() 
{
 Serial.begin(115200);
 setupMotor();
 setupCompass();
 setupServo();
 setupOriginHeading();
 Serial.print("SET UP IS CALLED\n");
}
//int getMin(int origin_heading, int temp_heading)
//{
//  if(origin_heading > temp_heading)
//  {
//    return temp_heading;
//  }
//  return origin_heading;
//}
//int getMax(int origin_heading, int temp_heading)
//{
//  if(origin_heading > temp_heading)
//  {
//    return origin_heading;
//  }
//  return temp_heading;
//}
bool isSpecialCase(int origin_heading, int temp_heading)
{
  if(origin_heading > 270 && origin_heading <= 360 && temp_heading > 0 && temp_heading <= 90)
  {
    return true;
  }
  if(temp_heading > 270 && temp_heading <= 360 && origin_heading > 0 && origin_heading <= 90)
  {
    return true; 
  }
  return false;
} 
int get_subtraction(int origin_heading, int temp_heading)
{
  int subtraction = origin_heading - temp_heading;
  int result = 0;
  if (abs(subtraction) > 180)
  {
    if(isSpecialCase(origin_heading, temp_heading) == true)
    {
      int min_degree = min(origin_heading, temp_heading);
      int max_degree = max(origin_heading, temp_heading);
      result = min_degree + 360 - max_degree;
      if(origin_heading > temp_heading)
      {
        return -result;
      }
      return result;
    }
    else
    {
      return 0;
    }
  }
  result = subtraction;
  return result;
}
bool validDegree(int degree)
{
  if(abs(degree) > 180)
  {
    return false;
  }
  return true;
}
//int get_subtraction(int origin_heading, int temp_heading)
//{
//  int subtraction = 0;
//  if(isSpecialCase(origin_heading, temp_heading)== true)
//  {
//    int min_degree = min(origin_heading, temp_heading);
//    int max_degree = max(origin_heading, temp_heading);
//    subtraction = min_degree + 360 - max_degree;
//    if(origin_heading > temp_heading)
//    {
//       subtraction = -subtraction;
//    }
//  }
//  else
//  {
//    subtraction = origin_heading - temp_heading;
//  }
//  return subtraction;
//}
int speedCar = 410;
void stopRobot(){  
      digitalWrite(IN_3, LOW);
      digitalWrite(IN_4, LOW);
      analogWrite(ENB, speedCar);
 }
void goAhead(){ 
      int origin_heading = global_heading;
      int temp_heading = round(readHeading());
      //default value of goAhead = 90;
      int default_value = default_compass;
      int subtraction = get_subtraction(origin_heading, temp_heading);
      Serial.print("origin ");
      Serial.println(origin_heading);
      Serial.print("temp ");
      Serial.println(temp_heading);
      Serial.print("subtraction ");
      Serial.println(subtraction);
      if (subtraction <= -5 || subtraction >= 5)
      {
        if(abs(subtraction) > 45)
        {       
          if(subtraction < 0)
          {
            servo.write(default_value - 45);
          }
          else
          {
            servo.write(default_value + 45);
          }
        }
        else
        {
          Serial.print("Subtraction that have to rotate ");
          Serial.println(subtraction);
          servo.write(default_value + subtraction);
          Serial.print("Subtraction ");
          Serial.println(subtraction);
        }
      }
      else
      {
          Serial.print("Subtraction that not have to rotate ");
          Serial.println(subtraction);
          servo.write(default_value);
      }
       digitalWrite(IN_3, LOW);
       digitalWrite(IN_4, HIGH);
       analogWrite(ENB, speedCar);
}
void goBack(){ 
      digitalWrite(IN_3, HIGH);
      digitalWrite(IN_4, LOW);
      analogWrite(ENB, speedCar);
  }
void goRight(){
      digitalWrite(IN_3, LOW);
      digitalWrite(IN_4, HIGH);
      analogWrite(ENB, speedCar);
  }
 void goLeft(){
      digitalWrite(IN_3, HIGH);
      digitalWrite(IN_4, LOW);
      analogWrite(ENB, speedCar);
  }
float readHeading()
{
    Vector norm = compass.readNormalize();

  // Calculate heading
  float heading = atan2(norm.YAxis, norm.XAxis);

  // Set declination angle on your location and fix heading
  // You can find your declination on: http://magnetic-declination.com/
  // (+) Positive or (-) for negative
  // For Bytom / Poland declination angle is 4'26E (positive)
  // Formula: (deg + (min / 60.0)) / (180 / M_PI);
  float declinationAngle = (4.0 + (26.0 / 60.0)) / (180 / M_PI);
  heading += declinationAngle;

  // Correct for heading < 0deg and heading > 360deg
  if (heading < 0)
  {
    heading += 2 * PI;
  }
 
  if (heading > 2 * PI)
  {
    heading -= 2 * PI;
  }

  // Convert to degrees
  float headingDegrees = heading * 180/M_PI; 
  return headingDegrees;
}
void loop()
{
  goAhead();
}
