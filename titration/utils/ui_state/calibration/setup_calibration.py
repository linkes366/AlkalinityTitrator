from titration.utils.ui_state import ui_state
from titration.utils import lcd_interface, constants
from titration.utils.ui_state.calibration.calibrate_ph import CalibratePh
from titration.utils.ui_state.calibration.calibrate_temp import CalibrateTemp


class SetupCalibration(ui_state.UIState):
    def __init__(self, titrator, state):
        ui_state.__init__(
            "SetupCalibration",
            titrator,
        )
        self.titrator = titrator
        self.previousState = state
        self.subState = 1

    def name(self):
        return "SetupCalibration"

    def handleKey(self, key):
        if key == constants.KEY_1:
            self._setNextState(CalibratePh(self.titrator, self), True)

        elif key == constants.KEY_2:
            self._setNextState(CalibrateTemp(self.titrator, self), True)

        elif key == constants.KEY_3:
            self._setNextState(self.previousState, True)

    def loop(self):
        lcd_interface.lcd_out("1. pH", line=1)
        lcd_interface.lcd_out("2. Temperature", line=2)
        lcd_interface.lcd_out("3. Return", line=3)
        lcd_interface.lcd_out("", line=4)