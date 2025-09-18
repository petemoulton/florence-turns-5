#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time

def test_invitation():
    with sync_playwright() as p:
        # Launch browser in headful mode to see what's happening
        browser = p.chromium.launch(headless=False)

        # Create both desktop and mobile contexts
        desktop_context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        mobile_context = browser.new_context(
            viewport={'width': 390, 'height': 844},  # iPhone 14 Pro size
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        )

        # Test desktop view
        desktop_page = desktop_context.new_page()
        desktop_page.goto('http://localhost:8000')

        # Wait for content to load
        desktop_page.wait_for_selector('.header', timeout=5000)

        # Check if Kuromi is visible
        kuromi = desktop_page.locator('.kuromi-character')
        if kuromi.count() > 0:
            print("✓ Kuromi element found in DOM")
            is_visible = kuromi.is_visible()
            print(f"  Kuromi visible: {is_visible}")

            # Get position
            box = kuromi.bounding_box()
            if box:
                print(f"  Position: top={box['y']}, right={1920-box['x']-box['width']}")
                print(f"  Size: {box['width']}x{box['height']}")
        else:
            print("✗ Kuromi element NOT found in DOM")

        # Check creature elements
        creatures = desktop_page.locator('.creature-emoji')
        print(f"\n✓ Found {creatures.count()} creature emojis")

        # Take screenshots
        desktop_page.screenshot(path='/tmp/desktop_view.png', full_page=True)
        print("\nDesktop screenshot saved to /tmp/desktop_view.png")

        # Test mobile view
        mobile_page = mobile_context.new_page()
        mobile_page.goto('http://localhost:8000')
        mobile_page.wait_for_selector('.header', timeout=5000)

        # Check Kuromi on mobile
        kuromi_mobile = mobile_page.locator('.kuromi-character')
        if kuromi_mobile.count() > 0:
            is_visible_mobile = kuromi_mobile.is_visible()
            print(f"\nMobile - Kuromi visible: {is_visible_mobile}")

        mobile_page.screenshot(path='/tmp/mobile_view.png', full_page=False)
        print("Mobile screenshot saved to /tmp/mobile_view.png")

        # Keep browser open for manual inspection
        print("\n🔍 Browser will stay open for 10 seconds for inspection...")
        time.sleep(10)

        browser.close()

if __name__ == "__main__":
    test_invitation()