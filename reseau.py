class Reseau:
    def __init__(self, name='Network', learn='sigmoide', error=0.001):

        self.name = name # Network name
        if 'tangente' == str.lower(learn):
            self.fun_learn = tangente
            self.name_fun_learn = 'tangente'
        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'
        
        self.error = error # Erreur detectee
        self.couche = [] # Number of couches and nb of neurones by couches
        self.link = [] # all weights tab
        self.valueds = [] # Tab who has the differents neurones values

        self.control = 0 # Controller