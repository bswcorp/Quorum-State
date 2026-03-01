import tkinter as tk
from tkinter import messagebox
from src.quantum_logic.kernel.h2k_bridge import H2KBridge

class QuorumDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Quorum-State v3.0.0 | Node Controller")
        self.root.geometry("400x300")
        self.root.configure(bg="#000428")

        # Label Status
        self.label = tk.Label(root, text="QUORUM-STATE NODE", fg="#00D2FF", bg="#000428", font=("Orbitron", 14, "bold"))
        self.label.pack(pady=20)

        # Tombol Start H2K
        self.start_btn = tk.Button(root, text="ACTIVATE H2K BRIDGE", command=self.activate_h2k, bg="#9D50BB", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.start_btn.pack(pady=10)

        self.status_text = tk.Label(root, text="Status: IDLE", fg="white", bg="#000428")
        self.status_text.pack(pady=20)

    def activate_h2k(self):
        bridge = H2KBridge()
        res = bridge.connect_to_kernel("INITIAL_SYNC")
        self.status_text.config(text=f"Status: {res['status']}\nChecksum: {res['checksum']}", fg="#00D2FF")
        messagebox.showinfo("Success", "h2k Bridge Connected to Kernel v3.0.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuorumDashboard(root)
    root.mainloop()
