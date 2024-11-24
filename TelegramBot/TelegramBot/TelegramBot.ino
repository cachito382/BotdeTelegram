
char dato;

void setup() {

  pinMode(LED_BUILTIN , OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available()>0){

    dato=Serial.read();

    if(dato=='1'){ digitalWrite(LED_BUILTIN , HIGH);}

    if(dato=='A'){ digitalWrite(LED_BUILTIN , LOW);}

  }

}
