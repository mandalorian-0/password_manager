# 🚀 Password Manager – A Secure & Simple Tool

A cross-platform desktop password manager built with **Python 3** and **Tkinter**. This application allows users to securely store, retrieve, and generate strong passwords for different websites while maintaining a clean, intuitive interface.

## 📦 Features

- ✅ **Generate Strong Passwords**: Automatically creates random, secure passwords with a mix of letters, numbers, and symbols.
- ✅ **Search Stored Passwords**: Look up saved credentials by website name.
- ✅ **Save Credentials**: Store email and password pairs in a local JSON file (`vault.json`).
- ✅ **User-Friendly UI**: Clean, responsive layout with intuitive navigation.
- ✅ **Error Handling**: Gracefully handles missing files, empty inputs, and invalid data.
- ✅ **Clipboard Integration**: Automatically copies generated passwords to the clipboard for easy use.

## 🔐 Security Notes

- All data is stored locally in a JSON file (`vault.json`) and is **not transmitted** over the network.
- Passwords are stored in plain text (for simplicity in this demo). In production, consider encryption (e.g., using `pycryptodome` or `cryptography`).
- The app does not use any external APIs or cloud services.

## 📂 File Structure

```
project/
│
├── vault.json          → Stores saved website credentials (email & password)
├── password_manager.py → Main application script
└── logo.png            → Application logo (required for UI)
```

> ⚠️ **Note**: The `logo.png` file must be present in the same directory as the script for the app to display the logo properly.

## 🛠️ How to Run

1. Ensure you have **Python 3.6+** installed on your system.
2. Place the `logo.png` file in the same folder as `password_manager.py`.
3. Open a terminal or command prompt and run:

```bash
python password_manager.py
```

4. The application will launch with a clean interface. You can now:
   - Enter a website name and click **Search** to retrieve saved data.
   - Generate a new password using the **Generate** button.
   - Save your credentials by clicking **Add** (after confirming with a pop-up).

## 📝 Usage Example

| Step | Action |
|------|--------|
| 1 | Enter website name (e.g., `Google`) |
| 2 | Click **Search** → View stored email and password |
| 3 | Enter email and generate a new password |
| 4 | Click **Add** → Confirm and save to `vault.json` |

## 📚 Technical Details

- **Framework**: Tkinter (Python's standard GUI library)
- **Randomization**: Uses `random` and `string` modules to generate secure passwords.
- **Data Persistence**: JSON format for storing and loading credentials.
- **Input Validation**: Ensures no fields are empty before saving.
- **Error Handling**: Manages missing file paths and invalid data gracefully.

## 🚧 Limitations & Future Improvements

- 🔒 Passwords are stored in plaintext — future versions could use encryption.
- 📝 No password recovery or backup functionality.
- 📱 No mobile support — designed for desktop use only.
- 🔄 Could add features like password strength checking or auto-fill.

## 📝 License

This project is free and open-source. You may use, modify, and distribute it under the terms of your choice.

---

> ✅ **Created with care** — A practical tool for everyday digital security.  
> 💡 *For educational or personal use only. Not intended for production or enterprise environments.*
