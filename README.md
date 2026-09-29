#  Eventify AI — Intelligent Multi-Agent Event Planning Platform

Eventify AI is an intelligent, AI-powered event planning platform that helps users design and organize events through a team of specialized AI agents.

From discovering suitable venues and catering options to creating event timelines, invitations, visual concepts, and event proposals, Eventify AI brings multiple planning tasks together into a single intelligent workflow.

---

## ✨ Overview

Planning an event often requires managing multiple decisions simultaneously — venue selection, catering, budgeting, decoration, scheduling, invitations, and more.

**Eventify AI** simplifies this process by using a **multi-agent AI architecture**, where specialized agents work on different aspects of event planning and contribute to a unified event plan.

The platform can be used for events such as:

* 💍 Weddings
* 🎂 Birthday celebrations
* 🏢 Corporate events
* 🎓 College events
* 🎉 Private parties
* 🌸 Social gatherings

---

## 🚀 Key Features

### 🤖 Multi-Agent Event Planning

Eventify AI divides event planning into specialized AI agents that collaborate to produce a complete plan.

### 📍 Venue Recommendations

Find suitable venues based on event requirements, location, capacity, preferences, and budget.

### 🍽️ Catering Planning

Generate catering suggestions based on event type, guest requirements, preferences, and budget constraints.

### 💰 Budget-Aware Planning

Create event plans while considering the user's available budget and allocating resources across different requirements.

### 🎨 AI-Powered Event Visualization

Generate AI-based visual concepts to help users imagine the look and feel of their event.

### 💌 Invitation Generation

Create personalized event invitations and generate voice-based invitation content.

### 📅 Event Timeline

Generate an organized timeline containing important activities and planning milestones.

### 🤝 Sponsorship Suggestions

Identify potential sponsorship opportunities based on the event and its requirements.

### 📄 Event Proposal Generation

Generate a structured event proposal containing the major planning details.

---

## 🧠 Multi-Agent Architecture

Eventify AI follows a modular multi-agent architecture.

```text
                        ┌─────────────────────┐
                        │        User         │
                        └──────────┬──────────┘
                                   │
                                   ▼
                     ┌─────────────────────────┐
                     │  Event Planning Agent   │
                     └────────────┬────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼
   ┌────────────┐          ┌────────────┐          ┌────────────┐
   │Venue Agent │          │Budget Agent│          │Catering    │
   │            │          │            │          │Agent       │
   └────────────┘          └────────────┘          └────────────┘
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
                     ┌────────────▼────────────┐
                     │ Event Planning Engine  │
                     └────────────┬────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
        ┌───────────┐       ┌────────────┐      ┌────────────┐
        │ Timeline  │       │Invitation  │      │ Proposal   │
        │ Generator │       │ Generator  │      │ Generator  │
        └───────────┘       └────────────┘      └────────────┘
```

Each agent is responsible for a specific planning task, allowing the system to remain modular and extensible.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### AI & Agent Framework

* Google ADK
* Large Language Models
* Multi-Agent Architecture

### Generative AI

* LLM-based planning
* AI image generation
* AI-generated invitation content
* Voice generation

### Application

* Streamlit

### External Services

* Google Maps
* OpenAI
* Gemini
* ElevenLabs

### Supporting Libraries

* ReportLab
* Python utilities
* Data processing libraries

---

## 📂 Project Structure

```text
Eventify-AI/
│
├── agents/
│   ├── venue_agent/
│   ├── catering_agent/
│   ├── budget_agent/
│   └── planning_agent/
│
├── tools/
│   ├── venue_tools/
│   ├── catering_tools/
│   ├── event_tools/
│   └── visualization_tools/
│
├── data/
│
├── configs/
│
├── utils/
│
├── assets/
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Eventify-AI.git
```

### 2. Navigate into the project

```bash
cd Eventify-AI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Configuration

Eventify AI uses external AI and service APIs for several capabilities.

Create a `.env` file in the project root and add the required API credentials.

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

> Some features may require specific API credentials depending on the configuration being used.

**Never commit your `.env` file or API keys to GitHub.**

---

## ▶️ Running the Application

After installing the dependencies and configuring the required API keys:

```bash
streamlit run app.py
```

The application will start locally and can be accessed through the Streamlit interface.

---

## 🔄 How It Works

### Step 1 — Event Requirements

The user provides information such as:

* Event type
* Location
* Number of guests
* Budget
* Preferred date
* Theme
* Requirements

### Step 2 — AI Planning

The main planning workflow analyzes the requirements and delegates tasks to specialized agents.

### Step 3 — Specialized Recommendations

Individual agents generate recommendations for:

* Venues
* Catering
* Budget allocation
* Event activities
* Timeline
* Decorations

### Step 4 — Content Generation

The platform can generate:

* Event concepts
* Invitation content
* Visual concepts
* Voice invitations
* Sponsorship suggestions

### Step 5 — Final Event Plan

The collected results are combined into a structured event proposal.

---

## 🎯 Example Use Case

A user wants to organize a birthday celebration for 50 people with a limited budget.

They provide:

```text
Event: Birthday Party
Guests: 50
Location: Hyderabad
Budget: ₹1,00,000
Theme: Elegant & Minimal
```

Eventify AI can then assist with:

```text
Venue
   ↓
Catering
   ↓
Budget Allocation
   ↓
Decoration Concept
   ↓
Event Timeline
   ↓
Invitation
   ↓
Final Event Proposal
```

---

## 🔮 Future Enhancements

The platform can be extended with:

* 🏪 Vendor marketplace
* ⭐ Vendor ratings and reviews
* 💳 Real-time budget tracking
* 📊 Event expense analytics
* 📅 Calendar integration
* 👥 Guest management
* 🪑 AI seating arrangement
* 🎨 Advanced event decoration generation
* 📱 WhatsApp invitation integration
* 📧 Email invitation automation
* 🔎 Vendor discovery and comparison
* 🧠 Personalized event recommendations
* 📍 Real-time venue availability
* 💬 Voice-based event planning

---

## 🔒 Privacy & Security

API credentials should be stored using environment variables and should never be committed to source control.

For production deployment, additional security measures such as authentication, authorization, rate limiting, input validation, and secure secret management should be implemented.

---

## 📌 Project Highlights

```text
✓ Python-based AI application
✓ Multi-agent AI architecture
✓ Generative AI
✓ Event recommendation
✓ AI image generation
✓ Voice generation
✓ Budget-aware planning
✓ Venue & catering assistance
✓ Automated event proposal generation
✓ Interactive Streamlit interface
```

---

## 👩‍💻 Author

**Madhuri Marda**

---

## 📄 License

This project is intended for educational and experimental purposes.

Please refer to the repository's original license and third-party service terms before redistributing or commercially deploying the project.
