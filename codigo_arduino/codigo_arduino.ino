int led1 = 13;
int led2 = 12;
int senal =A0;
char dato;

void setup() {
  
  Serial.begin(9600);
  pinMode(senal,INPUT);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);

}

void loop() {
  int lectura = analogRead(senal);  
  float lectura_float = (5.0/1023)*lectura;
  Serial.println(lectura_float);
  delay(500);

  if (Serial.available()>0)
  {
    dato=Serial.read();
    if(dato == '1')
    {
      digitalWrite(led1,HIGH);
    }
    if(dato == 'A')
    {
      digitalWrite(led2,HIGH);
    }
    if(dato == '2')
    {
      digitalWrite(led1,LOW);
    }
    if(dato == 'B')
    {
      digitalWrite(led2,LOW);
    }
  }

}
