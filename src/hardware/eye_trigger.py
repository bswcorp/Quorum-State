import cv2
import time
import sys
import os

# Menghubungkan ke Core Quorum-State
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core')))
from qstate_core import QuorumStateCore

def start_blink_detection():
    # Inisialisasi Kamera & Mesin Core
    cap = cv2.VideoCapture(0)
    node = QuorumStateCore()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    print("=== QSTATE H2K EYE-TRIGGER ACTIVE ===")
    print("Mencari identitas biometrik... Kedipkan mata untuk transaksi 1T.")

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            # LOGIKA KEDIPAN: Jika wajah terdeteksi tapi mata "hilang" sejenak
            if len(eyes) < 2:
                print("[H2K EVENT] Kedipan Terdeteksi! Memproses Transaksi Kuantum...")
                # Pemicu Transaksi Nyata di Ledger
                status = node.mint("ANDI-MUHAMMAD-HARPIANTO", 1000000000000)
                if status:
                    print(f"💰 BERHASIL: 1T $QSTATE Terkirim via Kedipan Mata.")
                    time.sleep(5) # Jeda agar tidak double transaction
            
        cv2.imshow('QSTATE Biometric Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_blink_detection()
