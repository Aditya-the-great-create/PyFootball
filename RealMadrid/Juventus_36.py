class National_Compeititions:
    def __init__(self, SerieA, Coppa_Italia, Supercoppa_Italiana):
        self.SerieA = SerieA
        self.Coppa_Italia = Coppa_Italia
        self.Supercoppa_Italiana = Supercoppa_Italiana

    def topplayer(self):
        if self.SerieA >= 5:
            return True
        elif self.Coppa_Italia >= 5:
            return True
        elif self.Supercoppa_Italiana >= 5:
            return True
        else:
            return False
