#include <OneWire.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ArduinoJson.h>
#include <Ethernet.h>
#include <SPI.h>

// Data wire is plugged into pin 2 on the Arduino 
#define ONE_WIRE_BUS 2
// Setup a oneWire instance to communicate with any OneWire devices  
OneWire oneWire(ONE_WIRE_BUS); 
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);


byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
EthernetServer server(80);

void setup() {
  // Initialize serial port
  Serial.begin(9600);
  sensors.begin(); 
  while (!Serial) continue;

  // Initialize Ethernet libary
  if (!Ethernet.begin(mac)) {
    Serial.println(F("Failed to initialize Ethernet library"));
    return;
  }

  // Start to listen
  server.begin();

  Serial.println(F("Server is ready."));
  Serial.print(F("Please connect to http://"));
  Serial.println(Ethernet.localIP());
}

void loop() {
  sensors.requestTemperatures();
  // Wait for an incomming connection
  EthernetClient client = server.available();

  // Do we have a client?
  if (!client) return;

  Serial.println(F("New client"));

  // Read the request (we ignore the content in this example)
  while (client.available()) client.read();

  // Allocate JsonBuffer
  // Use arduinojson.org/assistant to compute the capacity.
  StaticJsonBuffer<100> jsonBuffer;

  // Create the root object
  JsonObject& root = jsonBuffer.createObject();

  float temp = sensors.getTempCByIndex(0);
  root["temperature"] =temp;

  Serial.print(F("Sending: "));
  root.printTo(Serial);
  Serial.println();

  // Write response headers
  client.println("HTTP/1.0 200 OK");
  client.println("Content-Type: application/json");
  client.println("Connection: close");
  client.println();

  // Write JSON document
  root.prettyPrintTo(client);

  // Disconnect
  client.stop();
}
