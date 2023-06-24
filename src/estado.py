class Estado:
    def __init__(self, name, is_final=False, is_initial=False):
        self.name = name
        self.is_final = is_final
        self.is_initial = is_initial

    def setFinal(self):
        self.is_final = True

    def setInitial(self):
        self.is_initial = True
