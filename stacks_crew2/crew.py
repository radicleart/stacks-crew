from json import tool
from crewai import Agent, Task, Process, Crew
#from langchain_groq import ChatGroq
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from stacks_crew2.tools.wallet import check_balance_tool
from stacks_crew2.tools.wallet import make_purchase_tool
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

@CrewBase
class StacksCrew():
    """StacksCrew crew """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:

        self.groq_llm = ChatOpenAI(
            temperature=0,
            model_name="crewai-llama3",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )
    
    @agent
    def nft_researcher(self) -> Agent:
        print(self.agents_config['nft_researcher'])
        return Agent(
            config = self.agents_config['nft_researcher'],
            llm = self.groq_llm
        )
        
    @agent
    def nft_purchaser(self) -> Agent:
        print(self.agents_config['nft_purchaser'])
        return Agent(
            config = self.agents_config['nft_purchaser'],
            llm = self.groq_llm
        )
        
    @task
    def research_nfts(self) -> Task:
        return Task(
            config = self.tasks_config['research_nfts'],
            agent = self.nft_researcher()
        )
    
    @task
    def make_nft_report(self) -> Task:
        return Task(
            config = self.tasks_config['make_nft_report'],
            agent = self.nft_researcher()
        )
    
    @task
    def get_balance(self) -> Task:
        return Task(
            config = self.tasks_config['get_balance'],
            agent = self.nft_purchaser(),
            tools=[
                check_balance_tool
            ]
        )
    
    @task
    def make_purchase(self) -> Task:
        return Task(
            config = self.tasks_config['get_balance'],
            agent = self.nft_purchaser(),
            tools=[
                make_purchase_tool
            ]
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new StacksCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )