import os
import pm4py
from pm4py.visualization.petri_net import visualizer as pn_visualizer


class HeuristicMiner:
    
    def __init__(self):
        self.net = None
        self.initial_marking = None
        self.final_marking = None
        self.fitness_score = None
    
    def discover_process(self, log):
        print("Discovering process with Heuristic Miner...")
        self.net, self.initial_marking, self.final_marking = pm4py.discover_petri_net_heuristics(log)
        return self.net, self.initial_marking, self.final_marking
    
    def get_model_info(self):
        if self.net is None:
            return "No model discovered yet."
        
        return {
            'places': len(self.net.places),
            'transitions': len(self.net.transitions),
            'fitness': self.fitness_score
        }
    
    def print_model_details(self):
        if self.net is None:
            print("No model discovered yet.")
            return
        
        print(f"Heuristics Net - Places: {len(self.net.places)}, Transitions: {len(self.net.transitions)}")
        
        print("Heuristics Net Places:")
        for i, place in enumerate(self.net.places):
            print(f"  {i+1}. {place}")
        
        print("Heuristics Net Transitions:")
        for i, trans in enumerate(self.net.transitions):
            if trans.label:  # Only visible transitions
                print(f"  {i+1}. {trans.label}")
            else:
                print(f"  {i+1}. [Silent transition]")
    
    def visualize_model(self, filename="heuristics_miner.png"):
        if self.net is None:
            print("No model to visualize. Please discover a process first.")
            return False
        
        try:
            print(f"Generating visualization...")
            gviz = pn_visualizer.apply(self.net, self.initial_marking, self.final_marking)
            pn_visualizer.save(gviz, filename)
            print(f"Visualization saved as '{filename}'")
            
            # Try to open the file automatically
            full_path = os.path.abspath(filename)
            print(f"File location: {full_path}")
            try:
                os.startfile(full_path)  # Windows
                print("Opening the image automatically...")
            except:
                print(f"💡 Open '{filename}' to view the process model")
            
            return True
            
        except Exception as e:
            print(f"Could not save visualization: {e}")
            print("Make sure Graphviz is installed on your system")
            return False
    
    def set_fitness(self, fitness_score):
        self.fitness_score = fitness_score
    
    def has_model(self):
        return self.net is not None