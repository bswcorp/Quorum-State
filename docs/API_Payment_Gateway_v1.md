# 🔌 QSTATE HYBRID API DOCUMENTATION (v1.0)
**Subjek:** Gerbang Pembayaran Instan & Anti-Pending ($QSTATE Gateway)  
**Status:** NIST Post-Quantum Compliant 🛡️

---

## 1. AUTHENTICATION
Setiap permintaan API wajib menyertakan `X-QSTATE-KEY` di dalam header untuk validasi identitas pengembang.
*   **Header:** `Authorization: Bearer <YOUR_NIST_TOKEN>`
*   **Protocol:** HTTPS TLS 1.3 (NIST-Ready)

---

## 2. CREATE TRANSACTION (POST)
Gunakan *endpoint* ini untuk memicu transaksi instan tanpa menunggu konvensional bank.

**Endpoint:** `https://api.quorumstate.international`

### Request Body (JSON):
```json
{
  "sender_address": "QSTATE_BINTARO_001",
  "receiver_id": "VENDOR_DOMAIN_INTERNATIONAL",
  "amount": 150.00,
  "currency": "USD_EQUIVALENT",
  "priority": "INSTANT_NON_BLOCKING"
}
