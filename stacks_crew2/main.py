import os
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()
from stacks_crew2.crew import StacksCrew

def run():
  print("## Welcome to Stacks Crew")
  inputs = {
    'default_wallet': 'ST16F22ERP2XNNQ9ZZSPTMMAKFGMPVSK3D5EFGTY7'
  }
  StacksCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()