from pm4py.algo.discovery.alpha import algorithm as alpha_miner


class AlphaMiner:
       
    def __init__(self):
        self.net = None
        self.initial_marking = None
        self.final_marking = None
        self.fitness_score = None
    
    def discover_process(self, log):
        print("Discovering process with Alpha Miner...")
        self.net, self.initial_marking, self.final_marking = alpha_miner.apply(log)
        return self.net, self.initial_marking, self.final_marking
    
    def get_model_info(self):
        if self.net is None:
            return "No model discovered yet."
        
        return {
            'places': len(self.net.places),
            'transitions': len(self.net.transitions),
            'fitness': self.fitness_score
        }
    
    def set_fitness(self, fitness_score):
        self.fitness_score = fitness_score
    
    def has_model(self):
        return self.net is not None