<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# AI Security Scanner for Python

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-security-audit)

**Author:** sshahann31@gmail.com  
**Email:** sshahann31@gmail.com

---

![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec4e5f6)

---

## Introducing Today's Project!

In this project, I'm going to build a security scanner that detects vulnerabilities in Python code with color coded severity ratings. This will help me learn about CLI tools, SQL injection, hardcoded secrets and weak cryptography. I'm interested in this because I want to move beyond just writing code that works and start writing code that is resilient. I believe that security shouldn't be an afterthought or a separate department, it should be baked into the development process from the very first line.

### Key tools and concepts

Tools I used were the Gemini API, Python, and the colorama library for colored output, along with Python virtual environments for managing dependencies. Key concepts I learned include leveraging the Gemini API for security analysis, crafting structured prompts for consistent AI responses, and implementing color-coded output for vulnerability severity. I also gained a deeper understanding of common vulnerabilities like SQL injection, hardcoded secrets, and weak cryptography. The most important skill was learning to leverage AI for practical security tasks and building a functional security tool.

### Challenges and wins

This project took me approximately 2 hours to complete it today, focusing on leveraging AI for practical security tasks. The most challenging part was understanding the purpose and application of the Gemini API for security scanning, as well as grasping the concept of hardcoded secrets and why they pose a security risk. I also found ensuring all project validations were correctly marked as complete to be a recurring challenge. It was most rewarding to successfully build a functional AI-powered security scanner, especially seeing the color-coded severity ratings in action and implementing the capability to scan real Python files. Crafting structured prompts for consistent AI responses and leveraging AI for practical security tasks directly met my learning goals.

### Why I did this project

I did this project today because I wanted to learn how to leverage AI for practical security tasks and build a functional tool. This project met my goals by teaching me how to use the Gemini API for code analysis, craft structured prompts for consistent results, and implement clear, color-coded output for vulnerability severity. Next, I plan to integrate this scanner into my development workflow or explore how to expand its capabilities to other programming languages.

---

## Connecting to Gemini API

In this step, I'm setting up the Gemini API connection. This involves creating a new project folder and setting up Python environment, obtaining the Google API key, setting up a .env file to securely store the API key and then test the connection to Gemini. I need to do this so I can integrate Gemini's powerful code analysis capabilities into my security scanner, allowing it to detect vulnerabilities in the Python code.

![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec2c3d4)

I verified the connection by running 'python scanner.py' Gemini responded with "Hello, security scanner!" which confirmed that API was correctly setup and linked to Google's servers.


![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec4e5f6)

My scanner.py file works by sending a prompt to Gemini with specified code. When I ran it, Gemini identified multiple issues, namely the plaintext storage of the password, hardcoded values, no hashing and more. This shows that the Gemini API can detect vulnerabilities in my code.

---

## Building the Vulnerability Scanner

In this step, I'm building a vulnerability scanner that analyzes code for security issues. This will allow me to detect various vulnerabilities in Python code such as hardcoded secrets, detection of SQL injection and usage of weak passwords.

![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec7h8i9)

The vulnerabilities Gemini detected were SQL injection, hardcoded secrets, and weak cryptography. The security prompt I crafted asked for details for each issue like the vulnerability type, why it's vulnerable, its impact, and a secure code fix. This structured output helps me to get structured and actionable responses from Gemini, rather than vague information.

---

## Adding Severity Ratings

In this step, I'm adding severity ratings which will categorize the detected vulnerabilities like CRITICAL, HIGH, MEDIUM, LOW which helps you to quickly understand the impact and intensity of each issue, I'm also installing colorama to add color-coded output to the terminal, making the security report of each issue more readable and visually highlighted.

![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec0k1l2)

I updated the security prompt to include a SEVERITY field with CRITICAL/HIGH/MEDIUM/LOW options, which guides Gemini to rate the impact of each vulnerability. The add_colors_to_output function works by replacing the plain text severity ratings in Gemini's output with Colorama formatted versions, applying specific colors and styles. When I see CRITICAL in red, it tells me that the detected vulnerability is of the highest severity, requiring immediate attention and prioritization.

---

## Scanning Real Python Files

In this secret mission, I'm adding the capability for my scanner to analyze real Python files. This lets the scanner take a file path as input, read the code from that file, and then send that code to Gemini for analysis. Professional tools do this because it's a fundamental requirement for any practical security scanner. It allows the scanner to be used on actual codebases
integrate into CI/CD pipelines, and perform comprehensive security audits on entire projects, rather than just isolated snippets.

![Image](http://learn.nextwork.org/happy_cyan_vibrant_tangerine/uploads/ai-security-audit_sec3n4o5)

I scanned vulnerable.py by running python scanner.py vulnerability.py in my terminal. The vulnerabilities detected were SQL injection, hardcoded secrets, and weak cryptography. The scan_file function works by taking the file path (e.g., vulnerable.py) as an argument, reading the code from that file, and then sending the file's content to Gemini for security analysis.

---

## Wrap-up

---

---
