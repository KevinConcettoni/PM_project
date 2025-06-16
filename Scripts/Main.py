

import os
from pm4py.objects.log.importer.xes import importer as xes_importer
from AlphaMiner import AlphaMiner
from HeuristicMiner import HeuristicMiner
from TokenReplay import TokenReplay


class ProcessMiningMain:
    
    def __init__(self, log_path):
        self.log_path = log_path
        self.log = None
        self.alpha_miner = AlphaMiner()
        self.heuristic_miner = HeuristicMiner()
        self.token_replay_alpha = TokenReplay()
        self.token_replay_heuristic = TokenReplay()
    
    def load_log(self):
        if not os.path.exists(self.log_path):
            print("Log file not found. Please check the path.")
            return False
        
        print("Loading event log...")
        try:
            self.log = xes_importer.apply(self.log_path)
            print(f"Log loaded: {len(self.log)} traces")
            return True
        except Exception as e:
            print(f"Error loading log: {e}")
            return False
    
    def run_alpha_miner_analysis(self):
        """Run complete Alpha Miner analysis."""
        if self.log is None:
            print("No log loaded. Please load log first.")
            return
        
        print("\n=== ALPHA MINER ===")
        
        # Discover process
        net, im, fm = self.alpha_miner.discover_process(self.log)
        
        # Perform token replay and calculate fitness
        self.token_replay_alpha.replay_log(self.log, net, im, fm)
        fitness_results = self.token_replay_alpha.calculate_fitness()
        
        # Set fitness in miner and print report
        if fitness_results:
            self.alpha_miner.set_fitness(fitness_results['log_fitness'])
            self.token_replay_alpha.print_fitness_report("Alpha Miner")
    
    def run_heuristic_miner_analysis(self):
        """Run complete Heuristic Miner analysis."""
        if self.log is None:
            print("No log loaded. Please load log first.")
            return
        
        print("\n=== HEURISTICS MINER ===")
        
        # Discover process
        net, im, fm = self.heuristic_miner.discover_process(self.log)
        
        # Print model details
        self.heuristic_miner.print_model_details()
        
        # Perform token replay and calculate fitness
        self.token_replay_heuristic.replay_log(self.log, net, im, fm)
        fitness_results = self.token_replay_heuristic.calculate_fitness()
        
        # Set fitness in miner and print report
        if fitness_results:
            self.heuristic_miner.set_fitness(fitness_results['log_fitness'])
            self.token_replay_heuristic.print_fitness_report("Heuristics Miner")
        
        # Generate visualization
        print("\nGenerating visualization...")
        self.heuristic_miner.visualize_model("heuristics_miner.png")
    
    def run_complete_analysis(self):
        """Run the complete process mining analysis."""
        # Load log
        if not self.load_log():
            return
        
        # Run both mining algorithms
        self.run_alpha_miner_analysis()
        self.run_heuristic_miner_analysis()
        
        # Print comparison summary
        self.print_comparison_summary()
    
    def print_comparison_summary(self):
        """Print a comparison summary of both mining algorithms."""
        print("\n=== COMPARISON SUMMARY ===")
        
        alpha_info = self.alpha_miner.get_model_info()
        heuristic_info = self.heuristic_miner.get_model_info()
        
        # Handle case where models might not be discovered
        if isinstance(alpha_info, dict) and isinstance(heuristic_info, dict):
            print(f"Alpha Miner Model - Places: {alpha_info['places']}, Transitions: {alpha_info['transitions']}")
            print(f"Heuristic Miner Model - Places: {heuristic_info['places']}, Transitions: {heuristic_info['transitions']}")
            
            if alpha_info['fitness'] and heuristic_info['fitness']:
                print(f"Alpha Miner Fitness: {alpha_info['fitness']:.4f}")
                print(f"Heuristic Miner Fitness: {heuristic_info['fitness']:.4f}")
                
                if heuristic_info['fitness'] > alpha_info['fitness']:
                    print(" Heuristic Miner achieved better fitness!")
                elif alpha_info['fitness'] > heuristic_info['fitness']:
                    print(" Alpha Miner achieved better fitness!")
                else:
                    print(" Both miners achieved equal fitness!")
        else:
            print("Could not generate comparison - one or both models not discovered successfully.")
    
    def get_alpha_results(self):
        return self.alpha_miner, self.token_replay_alpha
    
    def get_heuristic_results(self):
        return self.heuristic_miner, self.token_replay_heuristic
    
    def get_log(self):
        return self.log


def main():
    log_path = "Logs/HospitalBilling.xes.gz"
    
    # Create and run the analysis
    process_mining = ProcessMiningMain(log_path)
    process_mining.run_complete_analysis()


if __name__ == "__main__":
    main()