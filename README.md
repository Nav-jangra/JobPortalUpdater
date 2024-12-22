# JobPortalUpdater

**JobPortalUpdater** is a Python application designed to automate the process of updating resumes and profiles on popular job portals, including **Shine**, **Naukri**, and **Foundit**. This tool saves time and effort by ensuring your profiles stay updated, giving you better visibility to recruiters.

---

## Features

- **Automated Resume Uploads**: Seamlessly update your resume on multiple platforms.
- **Profile Synchronization**: Keep your professional details consistent across job portals.
- **Multi-Platform Support**: Supports Shine, Naukri, and Foundit with plans to expand.
- **User-Friendly**: Simple setup and execution for non-technical users.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` for package management

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/JobPortalUpdater.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JobPortalUpdater
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Configure the `config.json` file with your job portal credentials and preferences.
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to update your profiles.

---

## Configuration

Create a `config.json` file with the following structure:
```json
{
  "shine": {
    "username": "your_email",
    "password": "your_password"
  },
  "naukri": {
    "username": "your_email",
    "password": "your_password"
  },
  "foundit": {
    "username": "your_email",
    "password": "your_password"
  }
}
```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Special thanks to the open-source community for inspiring this project.
- Icons and libraries used in this application.

---

## Contact

For queries or support, contact **your_email@example.com** or raise an issue in the repository.

