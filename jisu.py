from seleniumbase import SB

with SB(uc=True, test=True) as jisu:

    if True:
        url = "https://kick.com/brutalles"
        jisu.uc_open_with_reconnect(url, 5)
        jisu.uc_gui_click_captcha()
        jisu.sleep(1)
        jisu.uc_gui_handle_captcha()
        jisu.sleep(1)
        if jisu.is_element_present('button:contains("Accept")'):
            jisu.uc_click('button:contains("Accept")', reconnect_time=4)
        if jisu.is_element_visible('#injected-channel-player'):
            while jisu.is_element_visible('#injected-channel-player'):
                jisu.sleep(10)
