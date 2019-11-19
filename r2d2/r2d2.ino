#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const int SH = A0, SL = A1, SM = A2, del = 1000, ledMove = 13;
int H, L, M, T, A;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(ledMove, OUTPUT);
}

void loop() {
  send_data();
  delay(del);
}

void move_sensor(int value){
  if(value > 700){
    digitalWrite(ledMove, HIGH);
  }else{
    digitalWrite(ledMove, LOW);
  }
}

void send_data(){
  H = analogRead(SH);
  L = analogRead(SL);
  M = analogRead(SM);
  T = dht.readTemperature();
  A = dht.readHumidity();
  Serial.println(crypto());
  move_sensor(M);
}

String attach_value(char sensorLetter,int sensorValue){
  String resultado = "@";
  resultado.concat(sensorLetter);
  resultado.concat(":");
  resultado.concat(sensorValue);
  return resultado;
}

String crypto(){
  String text = "";
  text.concat(attach_value('H',H));
  text.concat(attach_value('L',L));
  text.concat(attach_value('M',M));
  text.concat(attach_value('T',T));
  text.concat(attach_value('A',A));
  return text;
}
