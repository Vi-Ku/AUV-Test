const byte sbc_input_pin = 5;
const byte thruster_control_pin = 13;
// Variables
bool stateChanged = false;
bool previousState;
unsigned long startTime;
bool  jetson_heart_beat_status_previous ;

void setup() {

  // put your setup code here, to run once:
pinMode(sbc_input_pin , INPUT);
pinMode(thruster_control_pin , OUTPUT);
digitalWrite(thruster_control_pin, LOW);
  // Initial state

  // Start time
  startTime = millis();
  bool  jetson_heart_beat_status_previous = digitalRead(sbc_input_pin);
}

void loop() {

  if (digitalRead(sbc_input_pin) != jetson_heart_beat_status_previous) {

    stateChanged = true;
    startTime = millis();
  }
  else
  {
    stateChanged =  false;
  }

  // Check if 2 seconds have passed without state change
  if (!stateChanged && (millis() - startTime >= 2000)) {
    digitalWrite(thruster_control_pin, LOW);  // Set control pin LOW
  }
  else
  {
    digitalWrite(thruster_control_pin, HIGH);
  }

  // Update previous state
  bool  jetson_heart_beat_status_previous = digitalRead(sbc_input_pin);
}
