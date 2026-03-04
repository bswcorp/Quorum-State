import hashlib

class WizardGatekeeper:
    def __init__(self):
        self.pilar_inti = 5
        self.macro_evolution_ready = False
        self.moral_threshold = 99  # Ambang batas moralitas absolut

    def filter_entry(self, person_id, greed_index, moral_score):
        """
        Filter Wizard: Hanya yang bermoral tinggi yang bisa masuk.
        Yang rakus & egois? KEY GO TO HELL!
        """
        if moral_score < self.moral_threshold or greed_index > 10:
            print(f"[ACCESS DENIED] {person_id}: RAKUS/EGOIS DETECTED. KEY GO TO HELL!")
            return False
        
        print(f"[WELCOME] {person_id}: Pilar masa depan. Selamat bergabung dalam evolusi $QSTATE.")
        return True

    def student_check(self, student_id, test_score):
        """
        Pemeriksaan Siswa: Jika tidak lulus, suruh pulang belajar lagi.
        """
        if test_score < 75:
            return f"[STUDENT] {student_id}: Belum lulus paradigma. Back to ur mum! Belajar keras dulu di rumah."
        return f"[STUDENT] {student_id}: Lulus. Selamat datang di paradigma jaman baru."
