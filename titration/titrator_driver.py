"""
The file for the Alkalinity Titrator driver
"""
import threading

from titration import mock_config
from titration.gui import GUI
from titration.titrator import Titrator

import PH_probe_test as testing


def run():
    """
    The function that drives sets up threading for the Titrator and GUI
    """
    titrator = Titrator(testing.ph_gains)
    testing.ph_test(titrator.ph_probe())

    if mock_config.MOCK_ENABLED:
        thread = threading.Thread(target=run_gui, args=[titrator], daemon=True)
        thread.start()

    while True:
        titrator.loop()


def run_gui(titrator):
    """
    The function that drives the Alkalinity Titrator's GUI
    """
    GUI(titrator)
