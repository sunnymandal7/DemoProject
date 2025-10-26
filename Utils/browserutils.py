import os
import datetime
import pytest
import base64

class browserutils:

    def __init__(self, driver):
        self.driver = driver
        self.step_counter = 1
        self.evidence_dir = os.path.abspath("./Reports/Evidence")
        os.makedirs(self.evidence_dir, exist_ok=True)

    def gettitle(self):
        return self.driver.title

    def capture_step(self, comment: str = ""):
        """
        Capture screenshot, save it, and embed it as base64 in the pytest-html report.
        """
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = f"{timestamp}.png"
        file_path = os.path.join(self.evidence_dir, file_name)

        # 1. Save screenshot to file
        try:
            self.driver.save_screenshot(file_path)
            print(f"[STEP {self.step_counter}] {comment} | Screenshot saved at {file_path}")
        except Exception as e:
            print(f"[STEP {self.step_counter}] {comment} | FAILED to save screenshot: {e}")
            self.step_counter += 1
            return  # Stop if saving failed

        # 2. Attach screenshot to pytest-html report
        if hasattr(pytest, "html"):
            try:
                # 2a. Read the saved image file in binary mode
                with open(file_path, "rb") as image_file:
                    # 2b. Encode it to a base64 string
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

                extra = getattr(pytest, "html").extras
                pytest_html = getattr(pytest, "html")

                # 2c. Create HTML content with the embedded Base64 image
                # This uses a 'data URI' to embed the image directly
                html_content = (
                    f"<div style='margin-bottom:10px; border: 1px solid #ddd; padding: 10px; border-radius: 5px;'>"
                    f"<b>Step {self.step_counter}:</b> {comment}<br>"
                    f"<img src='data:image/png;base64,{encoded_string}' style='width: 600px; border: 1px solid #ccc; margin-top: 5px;'>"
                    f"</div>"
                )

                # 2d. Append the custom HTML to the report
                pytest_html.extras.append(extra.html(html_content))

            except Exception as e:
                print(f"Failed to embed screenshot in HTML report: {e}")

        self.step_counter += 1