# Krackhack
Herein we will share our solution of the P.S that we are working on i.e. making an AI which will create website based on user prompts. For making this we are using agent.ai for providing agent to create website using the input.

-Command to run code
we need the following libraries given in text file to run te code.

-Repository Structure
1. frontend
2. backend
3. agent.ai
4. API to connect them
   
- Concise Summary of Code
  This AI based website genertor createswebsite based user prompts using agent.ai
  The backend (Python + Flask) sends user input to Agent.ai, retrieves the generated HTML/CSS/JS, and displays the output, the output file is saved in the PC which is then pushed to the git repo.
  Tech Stack:
Python (requests, os, subprocess) - for backend
Agent.ai API - fo providing ai agent
HTML, CSS, JavaScript- for frontend

The prompt in the input should be like this Generate code for the given file with {{filename}} with context {{context}}}
for example: Generate code for the given file calculator.html with context : make a website that shows a calculator.

*We accidently added wrong files as because of my system crash my files weren't saved properly. We got the permission from GDG mentor to make changes and add proper files.
