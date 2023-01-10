from titration.utils.ui_state import ui_state
from titration.utils import lcd_interface, constants
from titration.utils.ui_state.user_value.user_value import UserValue


class Pump(ui_state.UIState):
    def __init__(self, titrator, state):
        ui_state.__init__("Pump", titrator)
        self.titrator = titrator
        self.values = {"p_direction": 0}
        self.subState = 1
        self.previousState = state

    def name(self):
        return "Pump"

    def handleKey(self, key):
        if self.subState == 1:
            self._setNextState(UserValue(self.titrator, self, "Volume: "), True)
            self.subState += 1

        elif self.subState == 2:
            if key == constants.KEY_0 or key == constants.KEY_1:
                self.values["p_direction"] = key
                self.subState += 1

        elif self.subState == 3:
            self._setNextState(self.previousState, True)

    def loop(self):
        if self.subState == 1:
            lcd_interface.lcd_out("Set Volume", line=1)
            lcd_interface.lcd_out("", line=2)
            lcd_interface.lcd_out("Press any to cont", line=3)
            lcd_interface.lcd_out("", line=4)

        elif self.subState == 2:
            lcd_interface.lcd_out("In/Out (0/1):", line=1)
            lcd_interface.lcd_out("", line=2)
            lcd_interface.lcd_out("", line=3)
            lcd_interface.lcd_out("", line=4)

        elif self.subState == 3:
            lcd_interface.lcd_out("Pumping volume", line=1)
            lcd_interface.lcd_out("", line=2)
            lcd_interface.lcd_out("Press any to cont", line=3)
            lcd_interface.lcd_out("", line=4)