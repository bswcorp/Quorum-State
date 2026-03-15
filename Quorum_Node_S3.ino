#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Konfigurasi OLED (Sesuaikan PIN SDA/SCL ESP32-S3 Anda)
#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64 
#define OLED_RESET    -1 
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Simulasi Logika Quorum
int totalNodes = 4;
int requiredQuorum = 3;
int currentVotes = 0;
String systemState = "IDLE";
unsigned long lastActivity = 0;
const long displayTimeout = 10000; // Layar mati setelah 10 detik idle

void setup() {
  Serial.begin(115200);
  
  // Inisialisasi I2C (Default S3: SDA=8, SCL=9 atau sesuaikan board Anda)
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("OLED gagal diinisialisasi"));
    for(;;);
  }
  
  display.clearDisplay();
  updateDisplay("SISTEM READY", "QUORUM-STATE");
  lastActivity = millis();
}

void loop() {
  // Simulasi proses voting kuorum secara otomatis
  if (millis() - lastActivity < displayTimeout) {
    simulateQuorumProcess();
  } else {
    display.clearDisplay();
    display.display(); // Matikan layar untuk proteksi OLED
  }

  // Tekan tombol (atau kirim karakter via Serial) untuk bangunkan layar/reset
  if (Serial.available() > 0) {
    Serial.read();
    resetSystem();
  }
  
  delay(1500); 
}

void simulateQuorumProcess() {
  if (currentVotes < totalNodes) {
    currentVotes++;
    systemState = "VOTING...";
    
    // Cek apakah mencapai Kuorum
    String status = (currentVotes >= requiredQuorum) ? "QUORUM REACHED" : "WAITING...";
    updateDisplay(systemState, "Votes: " + String(currentVotes) + "/" + String(totalNodes));
    
    if (currentVotes >= requiredQuorum) {
      delay(1000);
      updateDisplay("STATE VALID", "HASH: 0xQubicoin...");
      Serial.println("State Validated by Quorum!");
    }
  }
}

void updateDisplay(String header, String body) {
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  
  // Header
  display.setTextSize(1);
  display.setCursor(0,0);
  display.println("QUORUM-STATE v1.0");
  display.drawLine(0, 10, 128, 10, SSD1306_WHITE);
  
  // Status
  display.setTextSize(2);
  display.setCursor(0, 20);
  display.println(header);
  
  // Detail
  display.setTextSize(1);
  display.setCursor(0, 45);
  display.println(body);
  
  display.display();
}

void resetSystem() {
  currentVotes = 0;
  systemState = "RESTARTING";
  lastActivity = millis();
  updateDisplay("RESETTING", "Starting New State");
  delay(1000);
}
