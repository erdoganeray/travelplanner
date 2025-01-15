from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from travelplanner.tools.duckduckgo_tool import DuckDuckGoSearchTool

memory_config = {
    "provider": "mem0",
    "config": {"user_id": "User"},
}

@CrewBase
class MyProject:
	"""MyProject crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# Register tools
	researcher_tools = [DuckDuckGoSearchTool()]

	@agent
	def chat_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['chat_agent'],
			memory=True,
			memory_config=memory_config,
			verbose=True,
		)

	@task
	def chat_task(self) -> Task:
		return Task(
			config=self.tasks_config['chat_task'],
			verbose=True,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MyProject crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
