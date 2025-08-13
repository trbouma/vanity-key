# Deterministic Biometric Nostr Key Generator

A web-based tool that generates deterministic Nostr keys from facial biometric data. The same face will always generate the same keys.

## 🔒 Security & Privacy

- **100% Client-Side**: All processing happens in your browser
- **No Data Storage**: No biometric data is stored or transmitted
- **Deterministic**: Same facial features = same keys every time
- **Open Source**: Fully auditable code

## 🚀 Features

- Real-time face detection using face-api.js
- Deterministic key generation from facial geometry
- Measurement stability indicator
- Valid Nostr keys (nsec/npub) with proper bech32 encoding
- Works with any webcam

## 🛠️ Technical Details

- Uses normalized facial ratios for consistency across lighting/angles
- Implements secp256k1 elliptic curve cryptography
- Generates valid bech32-encoded Nostr keys
- Compatible with all Nostr clients and tools

## ⚠️ Important Notes

1. **Experimental**: This is a proof-of-concept for deterministic biometric key generation
2. **Security Considerations**: Facial features are not secret - anyone with your photo could potentially generate your keys
3. **Use Responsibly**: Consider this as an interesting experiment rather than a primary security method

## 🔧 Technologies Used

- face-api.js for facial detection
- nostr-tools for key generation
- CryptoJS for hashing
- Pure JavaScript (no backend required)

## 📝 License

MIT