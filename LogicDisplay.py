class LogicDisplay:
    def __init__(self, strip, offset):
        self.strip = strip
        self.offset = offset

    def SetColor(self, r, g, b):
        for i in range(3):
            self.strip.setPixelColorRGB(self.offset + i, r, g, b)
        self.strip.show()

class FrontTopLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 3)

    def SetDefault(self):
        self.SetColor(100, 100, 100)

class FrontBottomLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 6)

    def SetDefault(self):
        self.SetColor(0, 0, 0)

class SideLogicDisplay(LogicDisplay):
    def __init__(self, strip):
        LogicDisplay.__init__(self, strip, 0)

    def SetDefault(self):
         self.SetColor(0, 50, 120)

