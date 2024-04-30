import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = ""

search_tool = SerperDevTool()

# Define your agents with roles and goals
publichealth_researcher = Agent(
  role='Senior Research Analyst',
  goal='Research the link between human conflict and HIV/AIDS.',
  backstory="""You work at a leading public health research organization.
  Your expertise lies in identifying emerging trends and synthesizing information.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

conflict_researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover developments in conflict in Ethiopia.',
  backstory="""You work at a leading conflict monitoring organization.
  Your expertise lies in identifying emerging trends.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

conflict_researcher2 = Agent(
  role='Senior Research Analyst',
  goal='Uncover developments in conflict in Ethiopia.',
  backstory="""You work at a leading conflict monitoring organization.
  Your expertise lies in identifying emerging trends.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
)

writer = Agent(
  role='Public Health Content Writer',
  goal='Craft compelling content on HIV/AIDS and conflict in Ethiopia.',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You consolidate multiple sources of information.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest developments on conflict in 2024 in Ethiopia.
  Use sites like the Council on Foreign Relations, Crisis Group, ACLED, Harvard, etc. to identify ongoing conflicts.
  Identify key events and conflict hotspot areas in Ethiopia.""",
  expected_output="Full analysis report in bullet points",
  agent=conflict_researcher
)

task2 = Task(
  description="""Conduct a comprehensive analysis of the latest developments on human movement or migration due to conflict in 2024 in Ethiopia.
  Report on where people are moving from and to due to conflict.""",
  expected_output="Full analysis report in bullet points",
  agent=conflict_researcher2
)

task3 = Task(
  description="""Conduct a comprehensive analysis of the latest research on the impact of conflict on HIV/AIDS in Ethiopia.
  Identify key trends, potential public health impacts, and key recommendations for policymakers and health organizations.""",
  expected_output="Full analysis report in bullet points",
  agent=publichealth_researcher
)

task4 = Task(
  description="""Using the insights provided, develop a policy brief for policymakers
  that highlights the most significant conflict areas in Ethiopia for HIV/AIDS response.
  Describe major conflict events in 2024 and include the who, what, where, and why.
  Also predict areas of tension where conflict may escalate or breakout.
  Describe where people are fleeing from conflict and to (is it nearby regions within the country or nearby countries?) so that policymakers can anticipate health needs.
  Summarize the key recommendations for policymakers in terms of humanitarian aid and HIV/AIDS response.
  Be specific in your recommendations and provide actionable steps.
  Do not use any superfluous words or jargon.""",
  expected_output="Policy brief for policymakers in Ethiopia on the link between conflict and HIV/AIDS.",
  agent=writer
) 

# Instantiate your crew with a sequential process (task done one after another)
crew = Crew(
  agents=[publichealth_researcher, conflict_researcher, conflict_researcher2, writer],
  tasks=[task1, task2, task3, task4],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
