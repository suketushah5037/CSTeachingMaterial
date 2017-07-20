#include <Keyboard.h>
#include <SoftwareSerial.h>

//10, 9 is the connection with the idiot ware shield , cross connection 
SoftwareSerial mySerial(10, 9); // RX, TX

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(57600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  //put the jumper on the shield, pin 4 for the LED to get on and off
  pinMode(4, OUTPUT);

  //arduino serial is RX and TX - cannot use it for software serial
  Serial.println("Bluetooth connection - arduino serial!");

  // set the data rate for the SoftwareSerial port
  //Baud rate set on the bluetooth using the USB to TTL connector or Arduino by giving the key pin a high and powering up together
  //observe the light flashes, slow flashes is AT mode and rapid flashes deotes connection and data transfer

  //The connection is established when the computer or android phone has bluetooth turned on and paired with the device manually, pairing passoword is 1234, see the HC-05 datasheet, name
  //of the device needs to be copied to program from device manager. from the COM ports list you will get the COM ports it is connected to
  //The COM port can be connectd to using termite or blueterm at 38400 to see what is written /read on the software serial ports - 10,9 - similarlly you will see two ports on the computer
  //on android you can pair it and write app inventor code to see the data being written on to software serial
  //Software serial, 38400 is the one set to ports 10, 9
  mySerial.begin(38400);
  mySerial.println("Hello, world?");
}

//To receive and send temperature
void loop() { // run over and over
  //A0 LM35 is connected to on the shield
  int value = analogRead(A0);
  float voltage = (5000.0/1024.0);
  
  //10mV is 1 degree
  float calc = voltage/10.0;
  float cel = value*calc;
  Serial.println(cel);
  if (mySerial.available()) {
    Serial.write(mySerial.read());
  }
  if (Serial.available()) {
  mySerial.write(cel);
 
  }
  delay(1000);
}
}

//To receive LED data
//void loop()
//{
//  if(mySerial.available())
//  {
//     byte text = mySerial.read();
//     //Serial.println(text);
//     if(text == 1)
//     {
//        digitalWrite(4, HIGH);
//     }
//     else if(text == 0)
//     {
//        digitalWrite(4, LOW);
//     }
//     
//  }
  
}
//dont forget to change the jumper from lm35 to led from http://idiotware.io/start/
//and read a byte only as serial sends bytweise and for led, remove serial if using the first led

