from playwright.sync_api import sync_playwright
import time

def refresh_dashboard(url, refresh_interval):
    """
    Opens a URL in a browser and refreshes it periodically.

    Args:
        url (str): The URL of the dashboard to refresh.
        refresh_interval (int): Time in seconds between each refresh.
    """
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)  # Set headless=True if you don't want a visible browser
        context = browser.new_context()
        page = context.new_page()

        # Open the URL
        page.goto(url)
        print(f"Opened {url} in the browser.")

        try:
            while True:
                time.sleep(refresh_interval)
                page.reload()  # Refresh the page
                print(f"Refreshed {url}")
        except KeyboardInterrupt:
            print("\nStopped refreshing.")
        finally:
            browser.close()

# Example usage
if __name__ == "__main__":
    target_url = input("Enter the dashboard URL: ")
    interval = int(input("Enter refresh interval in seconds (e.g., 5): "))
    refresh_dashboard(target_url, interval)
