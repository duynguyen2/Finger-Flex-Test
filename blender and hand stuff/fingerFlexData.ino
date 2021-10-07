/*
 * Code is compatible with the blender file, vrhand.blend with flex_vr_hand.py
 * Subject to change as the driver is built, will probably build a copy of this code to edit later and keep this as reference
 */

// the baudrate to be set to
const long unsigned int BAUDRATE = 115200;

// delay time
const long unsigned int DELAY_TIME = 5;

const int OFFSET = 1023;
const double SCALE_ADJUSTMENT = 1023;

const int THRESHOLD_GRAB = 100000;

// all values are for Duy's physical components, if you would like to mess with this yourself please measure and change accordingly
// 1 is the proximal phalanx, 2 is middle and 3 is distal
// adjust the inputs to what you'd like, this is simply just what Duy decided to do
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

// the open positions are assumed to be the starting position, so initialize to 0
int openProximal = 0;
int openMiddle = 0;
int openDistal = 0;

// the closed position would be the max amount the finger can be closed, unable to set to 0 as that may cause inaccuracy
int closedProximal;
int closedMiddle;
int closedDistal;

// initializing the variables that will store the raw data and calculation from the respective flex sensors
float indexProximal = 0;
float indexMiddle = 0;
float indexDistal = 0;

// initializing the variables that will store the calculation from the respective flex sensors to return
float indexProximalBend = 0;
float indexMiddleBend = 0;
float indexDistalBend = 0;

// sets baudrate and flex sensors as analog inputs
void setup()
{
  Serial.begin(BAUDRATE);
  Serial.flush();
  
  pinMode(FLEX_PIN1, INPUT);
  pinMode(FLEX_PIN2, INPUT);
  pinMode(FLEX_PIN3, INPUT);


  closedProximal = analogRead(FLEX_PIN1);
  closedMiddle = analogRead(FLEX_PIN2);
  closedDistal = analogRead(FLEX_PIN3);
}

void loop() 
{
  if(Serial.available() > 0){

    String readCommandFromPC = Serial.readStringUntil('\n');
    
    if(readCommandFromPC == "READ VALUES"){

      // collect the raw data
      indexProximal = analogRead(FLEX_PIN1);
      indexMiddle = analogRead(FLEX_PIN2);
      indexDistal = analogRead(FLEX_PIN3);

      // calculate the resistance values of the flex sensors
      float flexV1 = indexProximal * VCC / 1023.0;
      float flexV2 = indexMiddle * VCC / 1023.0;
      float flexV3 = indexDistal * VCC / 1023.0;
      
      float flexR1 = R_DIV1 * (VCC / flexV1 - 1.0);
      float flexR2 = R_DIV2 * (VCC / flexV2 - 1.0);
      float flexR3 = R_DIV3 * (VCC / flexV3 - 1.0);

      // if the calculation is less than the min, set new min
      //if(indexProximal < openProximal)
      //  openProximal = indexProximal;
      //if(indexMiddle < openMiddle)
      //  openMiddle = indexMiddle;
      //if(indexDistal < openDistal)
      //  openDistal = indexDistal;

      // if the calculation is greater than the max, set new max
      if(indexProximal > closedProximal)
        closedProximal = indexProximal;
      if(indexMiddle > closedMiddle)
        closedMiddle = indexMiddle;
      if(indexDistal > closedDistal)
        closedDistal = indexDistal;

      indexProximalBend = map(flexR1, STRAIGHT_RESISTANCE1, BEND_RESISTANCE1, 0.0, 90.0);
      indexMiddleBend = map(flexR2, STRAIGHT_RESISTANCE2, BEND_RESISTANCE2, 0.0, 90.0);
      indexDistalBend = map(flexR3, STRAIGHT_RESISTANCE3, BEND_RESISTANCE3, 0.0, 90.0);

      Serial.print(indexProximalBend);
      Serial.print(" "); Serial.print(indexMiddleBend);
      Serial.print(" "); Serial.print(indexDistalBend);
      Serial.println("");

      Serial.flush();
    }
  }

  delay(DELAY_TIME);

}
