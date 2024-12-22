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
- Python 3.12 or higher
- `pip` for package management

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Nav-jangra/JobPortalUpdater.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JobPortalUpdater
   ```
3. Activate the virtual Env
   ```bash
   python3 -m venv virtual      # create virtual environment for installing dependencies
   source virtual/bin/activate   # source ./.venv/bin/activate  # command for macOS/linux
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Configure the `values.yaml` file with your job portal credentials and preferences.
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to update your profiles.

---

## Configuration

Update the `values.yaml` file with the following structure:
```yaml
naukri:
  username: "my_user_name or email"
  password: "my_password"
  mob: "my_phone"

foundit:
  username: "my_user_name or email"
  password: "my_password"
  mob: "my_phone"

shine:
  username: "my_user_name or email"
  password: "my_password"
  mob: "my_phone"

resume: 
  originalResumePath: "/address/to/my/resume.pdf"
  modifiedResumePath: "/address/to/save/my/updated/resume.pdf"

headless: False  #for browser to work in backgroung
updatePDF: True  # for updating and adding some invisible characters to resume 

updateProfiles:
  naukri : True  #True if you want your naukri profile updated
  foundIt: True
  shine: True

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

For queries or support, raise an issue in the repository.

