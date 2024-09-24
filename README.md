# Instagram Profile Picture Updater

This script automates the process of updating the profile picture on Instagram at the start of every minute. It logs into your Instagram account, generates a new profile picture with the current date and time, and then uploads it automatically.

## Requirements

- Python 3.x
- Selenium
- Webdriver Manager
- Pillow (PIL)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ilham3169/InstagramLivePP
    cd InstagramLivePP
    ```

2. Install the required packages:
    ```bash
    pip install selenium webdriver-manager Pillow
    ```

3. Download and install the web driver manager for Chrome:
    ```bash
    pip install webdriver-manager
    ```

4. Ensure you have the Chrome browser installed, as the script uses the ChromeDriver to interact with Instagram.

## Usage

1. Open the script file and replace the placeholder credentials:
    ```python
    username = 'your_username' # replace with your Instagram username
    password = 'your_password' # replace with your Instagram password
    ```

2. Set the path to your desired background image in the code and make sure the font `arialbd.ttf` is available in the same directory or specify the correct path to it.

3. Run the script:
    ```bash
    python main.py
    ```

## Script Workflow

1. The script opens Instagram's account settings page and logs in using the provided credentials.
2. It waits for the current time's seconds to reach `00`.
3. At the start of every minute, the script:
   - Loads a background image (`bg.jpeg`).
   - Overlays the current date and time on the image.
   - Saves the new image (`sample-out.jpeg`).
   - Uploads the generated image as the new profile picture on Instagram.
4. This loop continues indefinitely until manually stopped.

## Notes

- This script is for educational purposes only. Instagram may block or restrict accounts that use automation scripts in violation of their terms of service.
- Make sure to modify the sleep time or interaction rates to avoid being detected as a bot by Instagram.

## Troubleshooting

1. **WebDriver not working?**
   Ensure that ChromeDriver is installed and that your Chrome browser version matches the driver. If needed, update both.

2. **Profile picture upload not working?**
   Check the XPaths used in the script. Instagram's HTML structure may change, requiring an update to the XPaths.

3. **Missing `arialbd.ttf` font?**
   Download the font or change the path in the script to point to a valid font file.


