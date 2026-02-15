import logging
from typing import Dict, List, Optional

class AIController:
    def __init__(self):
        self.logger = logging.getLogger("AIController")
        self.performance_tracker = PerformanceTracker()
        self.link_optimizer = LinkOptimizer()
        
    def decide_link_placement(self, content: str, links: List[str]) -> Dict[int, int]:
        """Decide optimal positions for affiliate links within the given content."""
        try:
            self.logger.info("Evaluating optimal link placement...")
            return self.link_optimizer.optimize_links(content, links)
        except Exception as e:
            self.logger.error(f"Error during link optimization: {str(e)}")
            raise
        
    def analyze_performance(self, metrics: Dict) -> None:
        """Analyze performance metrics and update system strategies."""
        try:
            self.performance_tracker.update(metrics)
            insights = self.performance_tracker.generate_insights()
            self.logger.info("Performance analysis complete. Insights generated.")
        except Exception as e:
            self.logger.error(f"Error during performance analysis: {str(e)}")
            raise