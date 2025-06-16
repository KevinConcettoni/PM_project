from pm4py.algo.evaluation.replay_fitness import algorithm as replay_fitness_evaluator
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay


class TokenReplay:
    def __init__(self):
        self.replayed_traces = None
        self.fitness_results = None
    
    def replay_log(self, log, net, initial_marking, final_marking):
        print("Performing token replay...")
        self.replayed_traces = token_replay.apply(log, net, initial_marking, final_marking)
        return self.replayed_traces
    
    def calculate_fitness(self):
        if self.replayed_traces is None:
            print("No replay results available. Please replay log first.")
            return None
        
        print("Calculating fitness metrics...")
        self.fitness_results = replay_fitness_evaluator.evaluate(self.replayed_traces)
        return self.fitness_results
    
    def get_fitness_summary(self):
        if self.fitness_results is None:
            return "No fitness results available."
        
        summary = {
            'log_fitness': self.fitness_results.get('log_fitness', 'N/A'),
            'perc_fit_traces': self.fitness_results.get('perc_fit_traces', 'N/A'),
            'average_trace_fitness': self.fitness_results.get('average_trace_fitness', 'N/A')
        }
        
        return summary
    
    def print_fitness_report(self, miner_name):
        if self.fitness_results is None:
            print(f"{miner_name} - No fitness results available.")
            return
        
        print(f"{miner_name} Fitness: {self.fitness_results['log_fitness']:.4f}")
        
        if 'perc_fit_traces' in self.fitness_results:
            print(f"{miner_name} - Percentage of fitting traces: {self.fitness_results['perc_fit_traces']:.2%}")
        
        if 'average_trace_fitness' in self.fitness_results:
            print(f"{miner_name} - Average trace fitness: {self.fitness_results['average_trace_fitness']:.4f}")
    
    def has_results(self):
        return self.replayed_traces is not None
    
    def has_fitness(self):
        return self.fitness_results is not None
    
    def get_log_fitness(self):
        if self.fitness_results is None:
            return None
        return self.fitness_results.get('log_fitness', None)