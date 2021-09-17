/******************************************************************************
Flex_Sensor_Example.ino
Example sketch for SparkFun's flex sensors
  (https://www.sparkfun.com/products/10264)
Jim Lindblom @ SparkFun Electronics
April 28, 2016

Create a voltage divider circuit combining a flex sensor with a 47k resistor.
- The resistor should connect from A0 to GND.
- The flex sensor should connect from A0 to 3.3V
As the resistance of the flex sensor increases (meaning it's being bent), the
voltage at A0 should decrease.

Development environment specifics:
Arduino 1.6.7
******************************************************************************/
const int FLEX_PIN1 = A0; // Pin connected to voltage divider output
const int FLEX_PIN2 = A1; // Pin connected to voltage divider output
const int FLEX_PIN3 = A3; // Pin connected to voltage divider output

// Measure the voltage at 5V and the actual resistance of your
// 47k resistor, and enter them below:
const float VCC = 4.81; // Measured voltage of Ardunio 5V line
const float R_DIV1 = 46200.0; // measured resistance of 4.7k resistor
const float R_DIV2 = 46800.0; // measured resistance of 4.7k resistor
const float R_DIV3 = 46500.0; // measured resistance of 4.7k resistor

// Upload the code, then try to adjust these values to more
// accurately calculate bend degree.
const float STRAIGHT_RESISTANCE1 = 26800.0; // measured resistance when straight
const float STRAIGHT_RESISTANCE2 = 27600.0; // measured resistance when straight
const float STRAIGHT_RESISTANCE3 = 26200.0; // measured resistance when straight

const float BEND_RESISTANCE1 = 73500.0; // resistance at 90 deg
const float BEND_RESISTANCE2 = 72800.0; // resistance at 90 deg
const float BEND_RESISTANCE3 = 73600.0; // resistance at 90 deg

void setup() 
{
  Serial.begin(9600);
  pinMode(FLEX_PIN1, INPUT);
  pinMode(FLEX_PIN2, INPUT);
  pinMode(FLEX_PIN3, INPUT);
}

void loop() 
{
  // Read the ADC, and calculate voltage and resistance from it
  int flexADC1 = analogRead(FLEX_PIN1);
  int flexADC2 = analogRead(FLEX_PIN2);
  int flexADC3 = analogRead(FLEX_PIN3);
  
  float flexV1 = flexADC1 * VCC / 1023.0;
  float flexV2 = flexADC2 * VCC / 1023.0;
  float flexV3 = flexADC3 * VCC / 1023.0;
  
  float flexR1 = R_DIV1 * (VCC / flexV1 - 1.0);
  float flexR2 = R_DIV2 * (VCC / flexV2 - 1.0);
  float flexR3 = R_DIV3 * (VCC / flexV3 - 1.0);

  // Use the calculated resistance to estimate the sensor's
  // bend angle:
  float angle1 = map(flexR1, STRAIGHT_RESISTANCE1, BEND_RESISTANCE1,
                   0, 90.0);
  float angle2 = map(flexR2, STRAIGHT_RESISTANCE2, BEND_RESISTANCE2,
                   0, 90.0);
  float angle3 = map(flexR3, STRAIGHT_RESISTANCE3, BEND_RESISTANCE3,
                   0, 90.0);
  
  Serial.println("Resistance1: " + String(flexR1) + " ohms");
  Serial.println("Resistance2: " + String(flexR2) + " ohms");
  Serial.println("Resistance3: " + String(flexR3) + " ohms");

  Serial.println("Bend 1: " + String(angle1) + " degrees");
  Serial.println("Bend 2: " + String(angle2) + " degrees");
  Serial.println("Bend 3: " + String(angle3) + " degrees");
  Serial.println();

  delay(500);
}
