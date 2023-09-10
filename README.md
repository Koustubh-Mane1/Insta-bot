# InstaBot
### Installing Python:

1. *Download Python:* Visit the official Python website at https://www.python.org/downloads/ and download the latest version of Python for your operating system (Windows).

2. *Run the Installer:* Run the downloaded installer. Make sure to check the box that says "Add Python X.Y to PATH" during the installation process (replace X.Y with your Python version). This option ensures that Python is added to your system's PATH environment variable, making it easier to run Python from the command line.

3. *Verify Installation:* Open a command prompt or terminal window and enter the following command to verify that Python was installed successfully:

   shell
   python --version
   

   You should see the Python version you installed displayed in the output.

### Installing the Chrome WebDriver:

1. *Check Chrome Version:* Open Google Chrome, click the three-dot menu icon in the top-right corner, go to "Help," and select "About Google Chrome." Note the version number.

2. *Download Chrome WebDriver:* Visit the Chrome WebDriver download page at https://sites.google.com/chromium.org/driver/ and download the WebDriver that corresponds to your Chrome version.

3. *Extract WebDriver:* After downloading the WebDriver, extract the executable file (e.g., `chromedriver.exe` on Windows) from the archive.

4. *Move WebDriver to a Directory:* It's a good practice to move the WebDriver executable to a directory that's included in your system's PATH environment variable. Common locations include `/usr/local/bin` on macOS and Linux or `C:\Program Files\PythonX.Y\Scripts` on Windows (replace X.Y with your Python version). Alternatively, you can add the directory containing the WebDriver to your system's PATH.

5. *Verify Installation:* Open a command prompt or terminal window and enter the following command to verify that the WebDriver was installed successfully:

   shell
   chromedriver --version
   

   You should see the WebDriver version displayed in the output.
### Opening the Folder
1. Download VS Code(preferrable) as a Code Editor. Download this repository as a zip file , then extract it and Open this folder in the code editor.
### Functions

1. MassDM -> This file is responsible for sending Dm's to all the usernames in the User_List Excel file. To run this code type python MassDM.py in the terminal, All the users to which the message has been sent will be moved to the Blacklist Excel file so that there should be not repeat messages to the same user.
2. Like_Recent -> This file is responsible for liking the recent page of all the usernames in the User_List Excel file. To run this code type python Like_Recent.py in the terminal.
3. RecentPostSend -> This file is responsible for sending a DM with the recent post of the sender to all the usernames in the User_List Excel file. To run this code type python RecentPostSend.py in the terminal.
4. Unfollow -> This file is responsible for Unfollowing  all the usernames in the User_List Excel file. To run this code type python Unfollow.py in the terminal.

   
   
