# 🕵️‍♂️ PhantomNet v2.0 — AI Honeypot Mesh
# PhantomNet v2.0

## Overview
PhantomNet is an advanced cybersecurity framework designed to simulate, monitor, and analyze network attacks in a controlled environment. It combines a high-interaction honeypot system with a blockchain-based logging mechanism, a web dashboard for real-time monitoring, and an API for automation and integration.

PhantomNet is ideal for cybersecurity researchers, ethical hackers, and network administrators who want to study attack patterns, track intrusions, and improve network defenses.

---

## Features

### Honeypot Agent
- Simulates vulnerable services on configurable ports (e.g., SSH, HTTP, MySQL)  
- Captures and logs attack data in real time  
- Can emulate multiple attack scenarios simultaneously  

### Backend API
- Built with FastAPI for lightweight and fast interactions  
- Provides endpoints for retrieving logs, managing honeypot configurations, and monitoring activity  

### Dashboard Frontend
- Real-time visualization of attacks and system status  
- Graphs and tables for IP addresses, attack frequency, and affected ports  
- Easy-to-use web interface for monitoring PhantomNet from anywhere  

### Blockchain Layer
- Logs attack events immutably using blockchain technology  
- Ensures integrity and tamper-proof audit trails  

### Security
- Advanced filtering and alerting for suspicious activity  
- Role-based access to dashboard and API  

---

## Installation

1. Clone the repository:  
```bash
git clone git@github.com:Arjun22347/PhantomNet-v2.0.git
cd PhantomNet-v2.0
2. Install Python dependencies:



pip install -r requirements.txt

3. Start the backend API:



cd backend_api
uvicorn app:app --reload

4. Start the PhantomNet agent:



python phantomnet_agent/agent.py

5. Access the dashboard frontend in your browser (if configured).




---

Usage

Connect to the honeypot using Telnet, SSH, HTTP, or MySQL to simulate attacks.

View real-time attack logs in logs/attacks.log.

Use the backend API to retrieve data programmatically.


Example:

telnet 127.0.0.1 2222


---

Contributions

Contributions are welcome!

Please fork the repository, make your changes, and submit a pull request.



---

License

PhantomNet v2.0 is released under the MIT License.

Use responsibly and ethically — for research and educational purposes only.



---

Contact

GitHub: https://github.com/Arjun22347/PhantomNet-v2.0

Author: Arjun22347
