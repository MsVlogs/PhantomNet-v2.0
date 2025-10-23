# PhantomNet v2.0 Development Guidelines

## Architecture Overview
PhantomNet is a distributed honeypot system with four main components:
- **Honeypot Agent** (`phantomnet_agent/agent.py`): Core component that simulates vulnerable services
- **Backend API** (`backend_api/app.py`): FastAPI service for log retrieval and management
- **Blockchain Layer** (`blockchain_layer/blockchain_client.py`): Immutable logging infrastructure
- **Dashboard Frontend** (`dashboard_frontend/`): React-based monitoring interface

## Key Patterns and Conventions

### Agent Configuration
- Port configurations and device profiles are managed in `phantomnet_agent/config.json`
- Example configuration:
```json
{
  "ports": [2222, 8080, 3306],
  "device_profile": "Smart Router",
  "encryption": true
}
```

### Event Handling Flow
1. Agent captures connection attempts (`agent.py:honeypot_listener`)
2. Events are logged locally and encrypted (`utils/logger.py`, `utils/crypto.py`)
3. AI analysis is performed (`ai_analyzer.py`)
4. Events are submitted to blockchain (`blockchain_client.py`)

### Development Workflow
1. Start the backend API:
```bash
cd backend_api
uvicorn app:app --reload
```

2. Run the honeypot agent:
```bash
python phantomnet_agent/agent.py
```

### Testing
- Simulate attacks using standard tools (telnet, curl) against configured ports
- Monitor `logs/attacks.log` for event capture
- Access API endpoints at `http://localhost:8000/logs` for verification

## Integration Points
- Backend API: FastAPI endpoints in `backend_api/app.py`
- Blockchain Interface: `blockchain_layer/blockchain_client.py`
- Agent-Dashboard Communication: Real-time event streaming via API

## Security Notes
- All captured data must be encrypted before storage (`utils/crypto.py`)
- The system assumes controlled environment deployment
- Production deployments should implement proper authentication

## Common Tasks
- Adding new honeypot ports: Update `phantomnet_agent/config.json`
- Implementing new attack analysis: Extend `ai_analyzer.py`
- Adding API endpoints: Follow FastAPI patterns in `backend_api/app.py`