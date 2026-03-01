# SalesShortcut - AI-Powered SDR Agent System
## Comprehensive PPT Presentation Guide

---

## 1. PROJECT OVERVIEW

### What is SalesShortcut?
SalesShortcut is a comprehensive **AI-powered Sales Development Representative (SDR) system** that automates the entire sales process from lead discovery to deal closure. The system **finds, creates, and converts leads** through intelligent AI agents.

### Tagline
> "Transforming manual sales processes into AI-powered automation"

### One-Liner
An autonomous multi-agent sales automation platform that discovers leads, researches prospects, generates personalized proposals, makes phone calls, and manages the entire sales funnel.

---

## 2. INSPIRATION / PROBLEM STATEMENT

### The Problem We Solved
- A developer friend partnered with a salesperson to generate new business
- The salesperson spent **hours cold-calling businesses** trying to find clients who needed websites
- The process was **entirely manual, time-consuming, and inefficient**
- Scaling this approach was nearly impossible

### Our Question
> "What if we could automate the entire sales process using AI?"

### The Solution
SalesShortcut replaces the manual grind with an intelligent multi-agent system that can:
- Find leads automatically
- Research them thoroughly
- Craft personalized proposals
- Make initial contact via phone and email
- Manage the entire sales pipeline

---

## 3. KEY FEATURES

### 🔍 Lead Generation
- **Geographic Targeting** - Find businesses in any specified city
- **Google Maps Integration** - Leverage Places API for accurate business data
- **Intelligent Filtering** - Focus on businesses without websites or with poor digital presence
- **Automated Discovery** - No manual searching required

### 🧠 AI-Powered Research
- **Comprehensive Business Analysis** - Understand target business needs and pain points
- **Competitor Research** - Analyze market position and opportunities
- **Review Analysis** - Extract insights from customer feedback
- **Website Assessment** - Identify digital presence gaps

### 📝 Proposal Generation
- **Personalized Content** - AI-crafted proposals based on research findings
- **PDF Generation** - Professional proposal documents
- **Fact-Checking** - Built-in verification of proposal claims
- **Iterative Refinement** - Multiple review passes for quality

### 📞 Multi-Channel Outreach
- **AI Phone Calls** - Natural voice conversations using Google Cloud Text-to-Speech
- **Email Automation** - SMTP-based delivery with Gmail integration
- **Professional Scripts** - Context-aware communication
- **Follow-up Management** - Automated engagement tracking

### 📋 Lead Management
- **Status Tracking** - Monitor leads through the entire sales funnel
- **Meeting Scheduling** - Calendar integration for appointments
- **Human-in-the-Loop** - User approval for critical actions
- **Data Persistence** - All interactions stored in Firebase Firestore

---

## 4. TECHNOLOGY STACK

### Backend & Framework
| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **FastAPI** | High-performance REST API framework |
| **Uvicorn** | ASGI server for async support |
| **Pydantic** | Data validation and settings management |
| **Starlette** | Lightweight ASGI framework for WebSockets |

### AI & Agent Framework
| Technology | Purpose |
|------------|---------|
| **Google Agent Development Kit (ADK) 1.0.0** | Multi-agent orchestration framework |
| **Gemini 2.0 Flash Lite** | Primary LLM for agent intelligence |
| **Vertex AI** | Advanced AI model hosting and inference |
| **A2A SDK 0.2.5** | Agent-to-Agent communication protocol |
| **Google Cloud AI Platform** | ML infrastructure and model serving |

### Google Cloud Services
| Service | Purpose |
|---------|---------|
| **Google Cloud Run** | Serverless container deployment |
| **Google Maps Places API** | Business discovery and location data |
| **Google Maps Geocoding API** | Address resolution and coordinates |
| **Google Search API** | Web research and information gathering |
| **Gmail API** | Email sending, reading, and response tracking |
| **Google Calendar API** | Meeting scheduling and calendar integration |
| **Google Cloud Pub/Sub** | Real-time message handling for email responses |
| **Google Cloud Build** | CI/CD pipeline automation |

### Database & Storage (Firebase)
| Service | Purpose |
|---------|---------|
| **Firebase Firestore** | NoSQL database for lead storage and real-time sync |
| **Firebase Realtime Database** | Live data synchronization across clients |
| **Firebase Cloud Storage** | File storage for proposals and documents |
| **Firebase Hosting** | Static asset hosting and CDN |

### Authentication & Security
| Technology | Purpose |
|------------|---------|
| **Clerk** | User authentication and session management |
| **Clerk SDK** | Secure login/signup flows |
| **OAuth 2.0** | Google service authentication |
| **Google Auth Libraries** | Service account and API authentication |

### Communication & Outreach
| Technology | Purpose |
|------------|---------|
| **Twilio** | Phone call infrastructure and SMS |
| **SMTP/Gmail** | Email delivery |
| **Google Cloud Text-to-Speech** | Voice synthesis for automated calls |
| **WebSocket** | Real-time bidirectional communication |

### Frontend & UI
| Technology | Purpose |
|------------|---------|
| **HTML5** | Page structure and semantics |
| **CSS3** | Styling with custom properties and animations |
| **JavaScript (ES6+)** | Client-side interactivity |
| **Jinja2** | Server-side templating engine |
| **WebSocket API** | Real-time dashboard updates |
| **Inter Font** | Modern typography via Google Fonts |
| **Clerk Components** | Pre-built authentication UI |

### Document Generation
| Technology | Purpose |
|------------|---------|
| **ReportLab** | PDF proposal generation |
| **Jinja2** | Email and document templating |
| **Markdown** | Content formatting |
| **BeautifulSoup4** | HTML parsing for web research |

### DevOps & Infrastructure
| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization |
| **Google Cloud Build** | CI/CD automation |
| **Cloud Run** | Serverless deployment |
| **nixpacks** | Build system for deployment |

### Development & Testing
| Technology | Purpose |
|------------|---------|
| **pytest** | Unit and integration testing |
| **pytest-asyncio** | Async test support |
| **httpx** | Async HTTP client for testing |
| **black** | Code formatting |
| **flake8** | Linting |
| **mypy** | Static type checking |

---

## 5. ARCHITECTURE

### Microservices Overview
SalesShortcut consists of **5 specialized microservices**:

| Service | Port | Description |
|---------|------|-------------|
| **Lead Finder** | 8081 | Discovers potential business leads using Google Maps |
| **SDR Agent** | 8084 | Main orchestrator for research, proposals, and outreach |
| **Lead Manager** | 8082 | Manages lead data, tracks conversion, scheduling |
| **UI Client** | 8000 | Web dashboard for monitoring and control |
| **Gmail PubSub Listener** | 8083 | Handles incoming email responses via Cloud Pub/Sub |

### Agent Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                        LEAD FINDER SERVICE                       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ Google Maps     │  │ Cluster Search  │  │ Potential Lead  │  │
│  │ Agent           │  │ Agent           │  │ Finder Agent    │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│                    ┌─────────────────┐                          │
│                    │  Merger Agent   │                          │
│                    └─────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                          SDR SERVICE                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ Research Lead   │  │ Proposal        │  │ Draft Writer    │  │
│  │ Agent           │  │ Generator       │  │ Agent           │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ Fact Checker    │  │ Outreach Caller │  │ Lead Clerk      │  │
│  │ Agent           │  │ Agent           │  │ Agent           │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │                   Outreach Email Agent                      ││
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ ││
│  │  │ Email Sender │ │ Offer File   │ │ Website Creator     │ ││
│  │  │ Agent        │ │ Creator      │ │ Agent               │ ││
│  │  └──────────────┘ └──────────────┘ └──────────────────────┘ ││
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐ ││
│  │  │ Spec Creator │ │ Engagement   │ │ Conversation        │ ││
│  │  │ Agent        │ │ Saver Agent  │ │ Classifier          │ ││
│  │  └──────────────┘ └──────────────┘ └──────────────────────┘ ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      LEAD MANAGER SERVICE                        │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ Calendar        │  │ Email Analyzer  │  │ Email Checker   │  │
│  │ Organizer       │  │ Agent           │  │ Agent           │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│  ┌─────────────────┐                                            │
│  │ Post Action     │                                            │
│  │ Agent           │                                            │
│  └─────────────────┘                                            │
└─────────────────────────────────────────────────────────────────┘
```

### Agent Statistics
| Agent Type | Count |
|------------|-------|
| **LLM Agents** | 21 |
| **Sequential Agents** | 7 |
| **Parallel Agents** | 1 |
| **Custom Agents** | 2 |
| **Loop Agents** | 1 |
| **A2A Clients** | 2 |
| **Total Agents** | **34** |

---

## 5.1. ARCHITECTURE STORY: THE JOURNEY OF A LEAD

### The Complete Agent Flow - A Narrative

Imagine you're a small web development agency. You want to find businesses in "Austin, Texas" that need websites. Here's exactly how SalesShortcut's 34 agents work together to make sales happen automatically:

---

### ACT 1: THE HUNT (Lead Finder Service)

**Scene 1: The User's Command**
```
User enters: "Austin, Texas" in the dashboard
```

The journey begins when a user enters a city name in the UI Client dashboard. This single action triggers a cascade of intelligent agent activity.

**Scene 2: Google Maps Agent Takes the Stage**

The **Google Maps Agent** wakes up first. It's an LLM Agent equipped with the `maps_search.py` tool. 

```
Google Maps Agent thinks:
"I need to find businesses in Austin, Texas. Let me search for 
restaurants, salons, gyms, auto shops - any local business that 
might need a website."
```

The agent makes multiple API calls to Google Maps Places API:
- Searches for "restaurants in Austin, Texas"
- Searches for "hair salons in Austin, Texas"  
- Searches for "fitness centers in Austin, Texas"
- And many more business categories...

For each business found, it extracts:
- Business name
- Address
- Phone number
- Website (or lack thereof!) ← **This is key**
- Rating and reviews
- Business hours
- Google Place ID

**Scene 3: Cluster Search Agent Organizes the Chaos**

With potentially hundreds of businesses discovered, the **Cluster Search Agent** steps in. Using the `cluster_search.py` tool, it:

```
Cluster Search Agent thinks:
"I have 200 businesses. Let me group them by:
- Geographic proximity (neighborhoods)
- Business type (food, beauty, fitness)
- Potential value (high-rated but no website = high priority)"
```

This creates intelligent clusters for efficient processing.

**Scene 4: Potential Lead Finder Agent Filters Gold from Gravel**

The **Potential Lead Finder Agent** is the gatekeeper. It examines each business:

```
Potential Lead Finder Agent evaluates:

Business: "Joe's Pizza"
- Has website? NO ✅ (This is a lead!)
- Has phone? YES ✅
- Rating: 4.5 ⭐ (Successful business)
- Reviews: 200+ (Established, has customers)
VERDICT: HIGH POTENTIAL LEAD

Business: "Tech Solutions Inc"
- Has website? YES ❌
VERDICT: SKIP (Already has what we sell)
```

Only businesses WITHOUT websites (or with terrible outdated ones) pass through.

**Scene 5: Merger Agent Creates the Master List**

The **Merger Agent** (a Sequential Agent) orchestrates the final assembly:

```
Merger Agent:
"I've received filtered leads from all clusters.
Let me deduplicate, validate, and create the final lead list.
Saving 47 qualified leads to Firebase Firestore..."
```

The `firebase_service.py` tool persists all leads with timestamps, source, and initial scoring.

**🎬 End of Act 1: 47 potential leads discovered and stored**

---

### ACT 2: THE INVESTIGATION (SDR Agent Service)

For each lead, the SDR Agent orchestrates a sophisticated multi-agent investigation.

**Scene 6: Research Lead Agent Deep Dives**

The **Research Lead Agent** receives a lead: "Joe's Pizza - Austin, TX"

```
Research Lead Agent thinks:
"I need to understand this business completely before we reach out.
Let me investigate..."
```

Using Google Search API and web research tools, it researches:
- **Business background**: How long have they been operating?
- **Competitors**: Who else sells pizza nearby? Do THEY have websites?
- **Reviews**: What do customers love/hate about Joe's Pizza?
- **Social media presence**: Are they on Facebook? Instagram?
- **Pain points**: Are customers complaining about not finding them online?

The agent produces a **Research Report**:
```json
{
  "business_name": "Joe's Pizza",
  "years_in_business": "15+ years",
  "monthly_customers_estimate": "2000+",
  "competitors_with_websites": ["Pizza Hut", "Domino's", "Local Slice"],
  "key_pain_points": [
    "Customers can't find menu online",
    "No online ordering (losing to competitors)",
    "Difficult to find location/hours"
  ],
  "opportunity_score": 9.2
}
```

**Scene 7: Proposal Generator Crafts the Pitch**

The **Proposal Generator Agent** receives the research report and gets creative:

```
Proposal Generator Agent thinks:
"Joe's Pizza has been serving Austin for 15 years but is losing 
customers to competitors with online ordering. I'll create a 
proposal that addresses exactly this pain point..."
```

It generates a structured proposal:
- **Problem Statement**: "Your loyal customers want to order online"
- **Solution**: Custom website with online ordering integration
- **Benefits**: Specific to Joe's (increase orders, compete with chains)
- **Pricing**: Tailored package recommendation
- **Timeline**: Realistic delivery estimate

**Scene 8: Draft Writer Agent Polishes the Words**

The **Draft Writer Agent** (an LLM Agent) takes the proposal structure and writes compelling copy:

```
Draft Writer Agent:
"Let me turn these bullet points into a persuasive, 
personalized email and proposal document..."

OUTPUT:
"Dear Joe,

For 15 years, you've been serving the best pizza in Austin. 
Your 4.5-star rating and 200+ reviews prove your customers 
love what you do. But here's the challenge: while you're 
hand-tossing dough, Domino's is taking orders on smartphones.

We'd like to change that..."
```

**Scene 9: Fact Checker Agent Verifies Everything**

Before any outreach, the **Fact Checker Agent** reviews all claims:

```
Fact Checker Agent verifies:
✅ "15 years in business" - Google says opened 2011 (14 years) - ADJUST
✅ "4.5-star rating" - Currently 4.4 stars - ADJUST  
✅ "Domino's has online ordering" - TRUE
✅ "200+ reviews" - Actually 187 reviews - ADJUST
❌ "No Facebook presence" - They DO have Facebook - REMOVE CLAIM
```

The proposal is refined with accurate information only.

**🎬 End of Act 2: Personalized, fact-checked proposal ready**

---

### ACT 3: THE APPROACH (Outreach Agents)

**Scene 10: Outreach Caller Agent Makes First Contact**

The **Outreach Caller Agent** initiates a phone call using Twilio with AI voice:

```
Outreach Caller Agent:
"Initiating call to Joe's Pizza at (512) 555-0123..."
```

Using `phone_call.py` tool with Twilio API:

```
AI Voice: "Hi, this is Sarah from WebCraft Solutions. I'm reaching 
out to local Austin businesses. I noticed Joe's Pizza has been 
serving the community for nearly 15 years - that's amazing! 

I was wondering if Joe or a manager might have 2 minutes to 
discuss how a simple website could help you compete with the 
big pizza chains online? We've helped several local restaurants 
increase their orders by 30%..."
```

The conversation is recorded and analyzed:

```
Call Result:
- Duration: 3 minutes 24 seconds
- Spoke with: Manager (Maria)
- Interest Level: HIGH
- Response: "Send me more information via email"
- Email provided: joe@joespizzaaustin.com
```

**Scene 11: Lead Clerk Agent Logs Everything**

The **Lead Clerk Agent** immediately updates the system:

```
Lead Clerk Agent:
"Updating lead status in Firebase Firestore...
- Status: CONTACTED → INTERESTED
- Contact person: Maria (Manager)
- Email: joe@joespizzaaustin.com
- Next action: SEND_PROPOSAL
- Follow-up date: Tomorrow"
```

**🎬 End of Act 3: Phone contact made, interest confirmed**

---

### ACT 4: THE PROPOSAL (Outreach Email Agent - A Sub-System)

The **Outreach Email Agent** is actually a complex system with its own sub-agents:

**Scene 12: Specification Creator Agent Designs the Website**

```
Specification Creator Agent:
"Based on the research, Joe's Pizza needs:
- Homepage with hero image of their pizza
- Menu page with prices
- Online ordering integration (UberEats/DoorDash)
- Location page with Google Maps
- Contact form
- Mobile-responsive design"
```

**Scene 13: Website Creator Agent Builds a Preview**

```
Website Creator Agent:
"Creating a mockup preview of Joe's Pizza website...
Using their actual photos from Google Business...
Generating responsive HTML/CSS preview..."
```

This creates an actual visual preview the prospect can see!

**Scene 14: Offer File Creator Agent Generates PDF**

Using `create_pdf_offer.py` with ReportLab, a professional PDF proposal is generated:

```
Offer File Creator Agent:
"Creating professional PDF proposal...
- Cover page with Joe's Pizza branding
- Problem/Solution breakdown
- Website preview screenshots
- Pricing table
- Terms and timeline
- Call to action"
```

Output: `JoesPizza_Proposal.pdf`

**Scene 15: Email Sender Agent Delivers**

The **Email Sender Agent** uses `gmail_service_account_tool.py` with Gmail API:

```
Email Sender Agent:
"Composing and sending email to joe@joespizzaaustin.com...

Subject: Joe's Pizza Website Proposal - As Discussed with Maria

Dear Joe and Maria,

Thank you for taking my call earlier today! As promised, 
I've attached our proposal for creating a professional 
website for Joe's Pizza...

[Attached: JoesPizza_Proposal.pdf]
[Attached: Website_Preview.html]

Looking forward to your thoughts!
Sarah"
```

**Scene 16: Engagement Saver Agent Tracks It**

```
Engagement Saver Agent:
"Logging email engagement to Firebase...
- Email sent: ✅
- Proposal attached: ✅
- Preview attached: ✅
- Tracking pixel: Inserted
- Follow-up scheduled: 3 days"
```

**🎬 End of Act 4: Professional proposal delivered**

---

### ACT 5: THE FOLLOW-UP (Lead Manager Service)

**Scene 17: Email Analyzer Agent Monitors Responses**

The **Email Analyzer Agent** receives notifications from Gmail Pub/Sub:

```
Email Analyzer Agent:
"New email received from joe@joespizzaaustin.com!
Subject: Re: Joe's Pizza Website Proposal

Analyzing content..."
```

**Scene 18: Conversation Classifier Agent Understands Intent**

```
Conversation Classifier Agent:
"Email content analysis:

'Thanks for sending this over. The mockup looks great! 
My wife and I would like to discuss pricing. 
Are you available Thursday afternoon?'

CLASSIFICATION: POSITIVE_RESPONSE
INTENT: MEETING_REQUEST
SENTIMENT: Enthusiastic
ACTION_REQUIRED: SCHEDULE_MEETING"
```

**Scene 19: Email Checker Agent Validates**

```
Email Checker Agent:
"Validating response...
- Sender verified: joe@joespizzaaustin.com ✅
- Not spam: ✅
- Relates to our proposal: ✅
- Contains meeting request: ✅"
```

**Scene 20: Calendar Organizer Agent Schedules**

Using `calendar_utils.py` with Google Calendar API:

```
Calendar Organizer Agent:
"Finding available slots for Thursday afternoon...
- Checking team calendar
- Proposing: Thursday 2:00 PM - 3:00 PM

Sending calendar invite to joe@joespizzaaustin.com...

Subject: Joe's Pizza Website Discussion
Time: Thursday, March 4, 2026 at 2:00 PM
Location: Google Meet (link attached)
Attendees: Joe, Maria, Sarah (WebCraft)"
```

**Scene 21: Post Action Agent Updates Pipeline**

```
Post Action Agent:
"Updating lead pipeline in Firebase...
- Status: INTERESTED → MEETING_SCHEDULED
- Meeting: Thursday 2:00 PM
- Next action: PREPARE_FOR_MEETING
- Deal probability: 75%

Notifying UI dashboard via WebSocket..."
```

**Scene 22: Human-in-the-Loop Notification**

The UI Client receives a notification:

```
🔔 HUMAN APPROVAL REQUIRED

Lead: Joe's Pizza
Action: Meeting scheduled for Thursday 2:00 PM
Proposed deal value: $2,500

[APPROVE] [MODIFY] [REJECT]
```

The user (authenticated via Clerk) approves, and the meeting is confirmed!

**🎬 End of Act 5: Meeting scheduled, deal 75% likely**

---

### ACT 6: THE CLOSE (Post-Meeting Flow)

**Scene 23: After the Meeting**

The user marks the meeting as "Successful - Deal Closed" in the dashboard.

**Scene 24: Post Action Agent Celebrates**

```
Post Action Agent:
"🎉 DEAL CLOSED!
- Lead: Joe's Pizza
- Final value: $2,500
- Status: CLOSED_WON
- Time from discovery to close: 5 days

Updating Firebase analytics...
Triggering success notification...
Preparing invoice template..."
```

---

### THE COMPLETE AGENT MAP

```
USER INPUT: "Austin, Texas"
      │
      ▼
┌─────────────────────────────────────────────────────────────────┐
│  🔍 LEAD FINDER SERVICE (Port 8081)                             │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 1. GOOGLE MAPS   │───▶│ 2. CLUSTER       │                  │
│  │    AGENT         │    │    SEARCH AGENT  │                  │
│  │    (LLM Agent)   │    │    (LLM Agent)   │                  │
│  │                  │    │                  │                  │
│  │ Tool: maps_search│    │ Tool: cluster_   │                  │
│  │       .py        │    │       search.py  │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 3. POTENTIAL     │◀───│ 4. MERGER        │                  │
│  │    LEAD FINDER   │    │    AGENT         │                  │
│  │    (LLM Agent)   │    │    (Sequential)  │                  │
│  │                  │───▶│                  │                  │
│  │ Filters leads    │    │ Tool: firebase_  │                  │
│  │ without websites │    │       service.py │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
└───────────────────────────────────┼─────────────────────────────┘
                                    │ A2A PROTOCOL
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  🧠 SDR AGENT SERVICE (Port 8084)                               │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 5. RESEARCH LEAD │───▶│ 6. PROPOSAL      │                  │
│  │    AGENT         │    │    GENERATOR     │                  │
│  │    (LLM Agent)   │    │    (LLM Agent)   │                  │
│  │                  │    │                  │                  │
│  │ Deep business    │    │ Creates custom   │                  │
│  │ research         │    │ proposal         │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 7. DRAFT WRITER  │───▶│ 8. FACT CHECKER  │                  │
│  │    AGENT         │    │    AGENT         │                  │
│  │    (LLM Agent)   │    │    (LLM Agent)   │                  │
│  │                  │    │                  │                  │
│  │ Writes compelling│    │ Verifies all     │                  │
│  │ copy             │    │ claims           │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 9. OUTREACH      │───▶│ 10. LEAD CLERK   │                  │
│  │    CALLER AGENT  │    │     AGENT        │                  │
│  │    (LLM Agent)   │    │     (LLM Agent)  │                  │
│  │                  │    │                  │                  │
│  │ Tool: phone_call │    │ Updates lead     │                  │
│  │       .py        │    │ status           │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ 📧 OUTREACH EMAIL AGENT (Nested Multi-Agent System)       │ │
│  │                                                           │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │ │
│  │  │ 11. SPEC    │  │ 12. WEBSITE │  │ 13. OFFER   │       │ │
│  │  │  CREATOR    │─▶│  CREATOR    │─▶│  FILE       │       │ │
│  │  │  AGENT      │  │  AGENT      │  │  CREATOR    │       │ │
│  │  └─────────────┘  └─────────────┘  └──────┬──────┘       │ │
│  │                                           │              │ │
│  │                                           ▼              │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │ │
│  │  │ 16. CONVER- │  │ 15. ENGAGE- │◀─│ 14. EMAIL   │       │ │
│  │  │  SATION     │  │  MENT SAVER │  │  SENDER     │       │ │
│  │  │  CLASSIFIER │  │  AGENT      │  │  AGENT      │       │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘       │ │
│  │                                                           │ │
│  │  Tools: create_pdf_offer.py, gmail_service_account_tool  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                    │ A2A PROTOCOL
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  📋 LEAD MANAGER SERVICE (Port 8082)                            │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 17. EMAIL        │───▶│ 18. EMAIL        │                  │
│  │     ANALYZER     │    │     CHECKER      │                  │
│  │     (LLM Agent)  │    │     AGENT        │                  │
│  │                  │    │                  │                  │
│  │ Understands      │    │ Validates        │                  │
│  │ email content    │    │ responses        │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
│                                   ▼                            │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 19. CALENDAR     │───▶│ 20. POST ACTION  │                  │
│  │     ORGANIZER    │    │     AGENT        │                  │
│  │     (LLM Agent)  │    │     (LLM Agent)  │                  │
│  │                  │    │                  │                  │
│  │ Tool: calendar_  │    │ Tool: ui_        │                  │
│  │       utils.py   │    │ notification.py  │                  │
│  └──────────────────┘    └────────┬─────────┘                  │
│                                   │                            │
└───────────────────────────────────┼─────────────────────────────┘
                                    │ WEBSOCKET
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  🖥️ UI CLIENT (Port 8000)                                       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CLERK AUTHENTICATION                                     │   │
│  │ - Secure login/signup                                   │   │
│  │ - Session management                                    │   │
│  │ - User authorization                                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Real-time dashboard showing:                                   │
│  - Lead pipeline with live status updates                       │
│  - Human-in-the-loop approval requests                          │
│  - Agent activity logs                                          │
│  - Analytics and metrics                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  📧 GMAIL PUBSUB LISTENER (Port 8083)                           │
│                                                                 │
│  Uses Google Cloud Pub/Sub to continuously monitor inbox for:  │
│  - Lead responses                                               │
│  - Meeting confirmations                                        │
│  - Questions about proposals                                    │
│                                                                 │
│  Feeds back to → LEAD MANAGER SERVICE                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### PARALLEL PROCESSING: FAN-OUT/GATHER PATTERN

When multiple leads are found, the system doesn't process them one by one. Instead:

```
LEAD FINDER discovers 47 leads
              │
              ▼
    ┌─────────┼─────────┐
    ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐
│Lead 1 │ │Lead 2 │ │Lead 3 │  ... (PARALLEL AGENT fans out)
│       │ │       │ │       │
│Research│ │Research│ │Research│
└───┬───┘ └───┬───┘ └───┬───┘
    │         │         │
    └─────────┼─────────┘
              │
              ▼
      GATHER & PRIORITIZE
    (Highest scores first)
              │
              ▼
      SEQUENTIAL OUTREACH
    (One call at a time)
```

---

### HUMAN-IN-THE-LOOP CHECKPOINTS

At critical decision points, the system pauses for human approval:

```
CHECKPOINT 1: Before first phone call
"Lead: Joe's Pizza | Score: 9.2 | Action: CALL"
[APPROVE CALL] [SKIP] [MODIFY SCRIPT]

CHECKPOINT 2: Before sending proposal
"Proposal for Joe's Pizza ready | Value: $2,500"
[SEND] [EDIT PROPOSAL] [CANCEL]

CHECKPOINT 3: Before scheduling meeting
"Joe's Pizza wants to meet Thursday 2PM"
[CONFIRM] [SUGGEST ALTERNATE TIME] [DECLINE]

CHECKPOINT 4: Before closing deal
"Close deal with Joe's Pizza for $2,500?"
[CLOSE WON] [CLOSE LOST] [KEEP NEGOTIATING]
```

---

### THE FEEDBACK LOOP

The system continuously improves:

```
┌──────────────────────────────────────────────────────────┐
│                    CONTINUOUS LEARNING                    │
│                                                          │
│  Phone call successful? ──────────────┐                  │
│                                       │                  │
│  Email got response? ─────────────────┤                  │
│                                       ▼                  │
│  Meeting scheduled? ───────────▶ ANALYZE PATTERNS        │
│                                       │                  │
│  Deal closed? ────────────────────────┤                  │
│                                       ▼                  │
│                              IMPROVE FUTURE OUTREACH     │
│                              - Better call scripts       │
│                              - More effective emails     │
│                              - Smarter lead scoring      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

### SUMMARY: FROM ZERO TO DEAL IN 34 AGENTS

| Phase | Agents Involved | Time | Output |
|-------|-----------------|------|--------|
| **Discovery** | 4 agents | ~5 min | 47 qualified leads |
| **Research** | 2 agents per lead | ~2 min/lead | Detailed business profiles |
| **Proposal** | 4 agents per lead | ~3 min/lead | Personalized proposals |
| **Phone Call** | 2 agents | ~5 min | Interested prospects |
| **Email** | 6 agents | ~2 min | Delivered proposals |
| **Follow-up** | 4 agents | Ongoing | Scheduled meetings |
| **Close** | 2 agents | Varies | REVENUE! |

**Total: 34 agents working in harmony to turn a city name into closed deals.**

---

## 6. INNOVATION & UNIQUE ASPECTS

### Technical Innovation

#### 1. Multi-Agent Orchestration at Scale
- **34 specialized agents** working in concert
- Sophisticated state management across agents
- Advanced ADK patterns including lifecycle hooks

#### 2. Advanced Agentic Patterns
- **Review/Critique Pattern** - Agents reviewing each other's work
- **Iterative Refinement** - Multiple passes for quality improvement
- **Parallel Fan-Out/Gather** - Simultaneous research operations
- **Human-in-the-Loop** - User approval for critical decisions
- **Agent-as-a-Tool** - Agents invoking other agents

#### 3. A2A Communication Protocol
- Reliable service-to-service communication
- Resilient error handling
- Proper request/response formatting between agent services

#### 4. Google Cloud Native
- Full integration with Google Cloud ecosystem
- Firebase for real-time data and authentication
- Cloud Pub/Sub for event-driven architecture

### Business Innovation

#### 1. End-to-End Automation
- First-of-its-kind complete sales automation
- From discovery to deal closing without manual intervention
- Scalable from individual to enterprise use

#### 2. Personalization at Scale
- Each prospect gets researched individually
- Proposals tailored to specific business needs
- No generic templates - every outreach is unique

#### 3. Multi-Channel Approach
- Phone calls + emails combined
- Follow-up automation
- Engagement tracking across channels

---

## 7. TOOLS IMPLEMENTATION

### Lead Finder Tools
| Tool | Function |
|------|----------|
| `maps_search.py` | Google Maps Places API integration |
| `cluster_search.py` | Geographic clustering of businesses |
| `firebase_service.py` | Lead data persistence to Firestore |

### SDR Agent Tools
| Tool | Function |
|------|----------|
| `phone_call.py` | Twilio voice call execution |
| `create_pdf_offer.py` | Professional proposal PDF generation (ReportLab) |
| `gmail_service_account_tool.py` | Email sending via Gmail API |
| `content_editor_tools.py` | Proposal content refinement |
| `offer_file_tools.py` | Offer document management |

### Lead Manager Tools
| Tool | Function |
|------|----------|
| `calendar_utils.py` | Google Calendar API integration |
| `check_email.py` | Email response monitoring |
| `meeting_request_llm.py` | AI-powered meeting scheduling |
| `ui_notification.py` | Real-time dashboard updates via WebSocket |

### UI Client Tools
| Tool | Function |
|------|----------|
| `auth.py` | Clerk authentication integration |
| `firebase_service.py` | Real-time data sync with Firestore |
| `direct_search.py` | Direct business search interface |
| `email_tracker.py` | Email engagement tracking |
| `sdr_research.py` | SDR research interface |

---

## 8. USER INTERFACE

### Web Dashboard Features
- **Clerk Authentication** - Secure login/signup with Clerk SDK
- **Real-time Pipeline View** - Live updates via WebSocket and Firebase
- **Lead Status Tracking** - Visual funnel progression
- **Human-in-the-Loop Requests** - Approve/reject agent actions
- **City-based Search** - Enter location to start finding leads
- **Architecture Diagram** - Visual system overview
- **Lead History** - Complete interaction timeline

### Key Screens
1. **Landing Page** - City input to start lead finding
2. **Dashboard** - Main control center with live pipeline
3. **Authentication** - Clerk-powered login/signup
4. **Architecture View** - System visualization

---

## 9. WORKFLOW DEMONSTRATION

### Complete Lead Journey

```
Step 1: USER LOGS IN (Clerk Authentication)
         ↓
Step 2: USER ENTERS CITY in dashboard
         ↓
Step 3: LEAD FINDER discovers businesses via Google Maps API
         ↓
Step 4: Filters for businesses without websites
         ↓
Step 5: RESEARCH LEAD AGENT analyzes each business via Google Search
         ↓
Step 6: PROPOSAL GENERATOR creates personalized proposal
         ↓
Step 7: DRAFT WRITER refines the content
         ↓
Step 8: FACT CHECKER verifies claims
         ↓
Step 9: OUTREACH CALLER makes phone call (Twilio)
         ↓
Step 10: If interested → OUTREACH EMAIL sends proposal (Gmail API)
         ↓
Step 11: LEAD MANAGER tracks engagement (Firebase realtime)
         ↓
Step 12: CALENDAR ORGANIZER schedules meeting (Google Calendar)
         ↓
Step 13: Deal Closed! 🎉
```

---

## 10. CHALLENGES & SOLUTIONS

### Challenge 1: Orchestrating 34 Agents
**Problem**: Managing state and communication across three dozen agents
**Solution**: Sophisticated state management using ADK's lifecycle hooks (`before_agent`, `after_agent`, `before_tool`, `after_tool`)

### Challenge 2: True Parallelism
**Problem**: Running simultaneous lead research without race conditions
**Solution**: Fan-out/gather pattern with careful async task management and data aggregation

### Challenge 3: Dynamic Tool Invocation
**Problem**: Agents calling other agents as tools
**Solution**: Proper request formatting and response interpretation with agent-as-a-tool patterns

### Challenge 4: Microservices Communication
**Problem**: Reliable A2A communication across 5 services
**Solution**: Implemented robust A2A protocol with error handling, timeouts, and retry logic

### Challenge 5: Real-time User Experience
**Problem**: Keeping users informed of agent activities
**Solution**: Firebase real-time sync + WebSocket connections for instant updates

---

## 11. ACCOMPLISHMENTS

### Technical Achievements
- ✅ 34 AI agents working in a cohesive system
- ✅ Production-ready multi-agent architecture
- ✅ True parallelism with fan-out/gather patterns
- ✅ Full Google Cloud integration
- ✅ 5 microservices with A2A communication
- ✅ Firebase real-time data synchronization
- ✅ Clerk authentication integration

### Business Impact
- ✅ Replaces manual sales processes entirely
- ✅ Scalable from individuals to teams
- ✅ Personalized outreach at scale
- ✅ Complete audit trail in Firebase

### User Experience
- ✅ Intuitive web dashboard
- ✅ Real-time WebSocket updates
- ✅ Human-in-the-loop control
- ✅ Secure authentication via Clerk
- ✅ Comprehensive lead analytics

---

## 11.1. COMPETITIVE ANALYSIS: SalesShortcut vs Market

### Feature Comparison Table

| Feature | SalesShortcut | Traditional CRMs (Salesforce, HubSpot) | Sales Automation Tools (Outreach, Apollo) | Manual Sales Process |
|---------|---------------|----------------------------------------|-------------------------------------------|---------------------|
| **Lead Discovery** | ✅ Automated via Google Maps API | ❌ Manual import required | ⚠️ Limited to existing databases | ❌ Manual cold searching |
| **AI Agent Orchestration** | ✅ 34 specialized agents | ❌ No AI agents | ⚠️ Single AI assistant | ❌ None |
| **Multi-Agent Architecture** | ✅ Google ADK with A2A protocol | ❌ Monolithic systems | ❌ Single-agent approach | ❌ N/A |
| **Personalized Research** | ✅ Deep AI research per lead | ⚠️ Basic enrichment | ⚠️ Template-based enrichment | ❌ Time-consuming manual |
| **Custom Proposal Generation** | ✅ AI-crafted unique proposals | ❌ Manual creation | ⚠️ Template-based only | ❌ Manual creation |
| **Fact-Checking** | ✅ Built-in AI verification | ❌ None | ❌ None | ❌ Manual verification |
| **AI Phone Calls** | ✅ Natural voice (Twilio + AI) | ❌ No calling | ⚠️ Basic auto-dialers | ✅ Human calls |
| **Email Automation** | ✅ Contextual AI emails | ✅ Template sequences | ✅ Template sequences | ❌ Manual emails |
| **Real-time Sync** | ✅ Firebase + WebSocket | ✅ Cloud sync | ✅ Cloud sync | ❌ None |
| **Human-in-the-Loop** | ✅ Approval checkpoints | ⚠️ Basic workflows | ⚠️ Basic approvals | ✅ Full human control |
| **Meeting Scheduling** | ✅ Google Calendar integration | ✅ Calendar integration | ✅ Calendar integration | ❌ Manual scheduling |
| **Setup Complexity** | ⚠️ Moderate (API keys needed) | ❌ High (weeks to deploy) | ⚠️ Moderate | ✅ Zero setup |
| **Cost** | 💰 Pay-per-use APIs | 💰💰💰 $150-300/user/month | 💰💰 $80-150/user/month | 💰 Time cost only |
| **Scalability** | ✅ Unlimited with Cloud Run | ✅ Enterprise scale | ✅ Good scale | ❌ Limited by humans |
| **Customization** | ✅ Full code control | ⚠️ Limited to features | ⚠️ Limited to features | ✅ Fully custom |

### Unique Differentiators

| What We Have | What Market Lacks |
|--------------|-------------------|
| **34 AI Agents** working in coordination | Most tools use single AI or no AI at all |
| **End-to-End Automation** from discovery to close | Fragmented tools requiring manual handoffs |
| **Google Maps Lead Discovery** | Competitors rely on purchased lead lists |
| **A2A Protocol** for microservices communication | Monolithic architectures with tight coupling |
| **Parallel Fan-Out/Gather** for research | Sequential processing only |
| **AI Fact-Checking Agent** | No verification - errors go unchecked |
| **Dynamic Proposal PDF Generation** | Static templates only |
| **Website Preview Creation** | Just text proposals, no visuals |
| **Firebase Real-time Updates** | Polling-based or delayed updates |
| **Clerk Authentication** | Complex OAuth implementations |
| **Gemini 2.0 Flash Lite** | Older LLM models or no LLM |
| **Google ADK** | Custom agent frameworks or none |

### Market Gap Analysis

| Market Need | Current Solutions | SalesShortcut Solution |
|-------------|-------------------|------------------------|
| **Find leads without buying lists** | ❌ Purchase expensive lead databases ($0.10-$1 per lead) | ✅ Free discovery via Google Maps API |
| **Personalize at scale** | ❌ Generic "Hi {FirstName}" templates | ✅ Deep research + custom proposals per lead |
| **Reduce manual work** | ⚠️ Still requires significant manual input | ✅ 90%+ automated from discovery to meeting |
| **Quality control** | ❌ Send now, fix later approach | ✅ Fact-Checker Agent verifies before send |
| **Multi-channel outreach** | ⚠️ Separate tools for phone vs email | ✅ Unified phone + email in one system |
| **Real-time visibility** | ⚠️ Dashboard refreshes periodically | ✅ Instant WebSocket + Firebase updates |
| **AI that understands context** | ⚠️ Basic keyword matching | ✅ Gemini-powered contextual understanding |
| **Affordable for small teams** | ❌ $150+/user/month minimum | ✅ Pay only for API usage |

### Cost Comparison (Monthly for 1 User)

| Solution | Monthly Cost | Leads/Month | Cost per Lead |
|----------|--------------|-------------|---------------|
| **SalesShortcut** | ~$20-50 (API costs) | Unlimited | ~$0.02-0.05 |
| **Salesforce Sales Cloud** | $300+ | Manual | N/A |
| **HubSpot Sales Hub** | $150+ | Limited | ~$1.50+ |
| **Apollo.io** | $99 | 500 credits | ~$0.20 |
| **Outreach.io** | $130+ | Manual | N/A |
| **ZoomInfo** | $250+ | 1000 credits | ~$0.25 |
| **Manual Process** | $0 (but 40+ hrs time) | ~50 max | Time cost |

### Technology Stack Comparison

| Component | SalesShortcut | Typical SaaS |
|-----------|---------------|--------------|
| **AI Framework** | Google ADK 1.0.0 (latest) | Proprietary or legacy |
| **LLM** | Gemini 2.0 Flash Lite | GPT-3.5 or basic NLP |
| **Agent Pattern** | Multi-agent orchestration | Single-agent or rule-based |
| **Communication** | A2A Protocol (modern) | REST APIs (traditional) |
| **Database** | Firebase Firestore (real-time) | PostgreSQL (polling) |
| **Deployment** | Google Cloud Run (serverless) | Traditional VMs |
| **Auth** | Clerk (modern) | Custom OAuth |

### Summary: Why SalesShortcut Wins

```
┌─────────────────────────────────────────────────────────────────┐
│                    SALESSHORTCUT ADVANTAGES                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  🎯 DISCOVERY                                                   │
│     • Free lead discovery vs $0.10-$1 per lead                  │
│     • Google Maps API vs purchased databases                    │
│                                                                 │
│  🤖 AI POWER                                                    │
│     • 34 agents vs 0-1 agents                                   │
│     • Gemini 2.0 vs older models                                │
│     • Google ADK vs no framework                                │
│                                                                 │
│  💰 COST                                                        │
│     • ~$30/month vs $150-300/month                              │
│     • Pay-per-use vs fixed subscription                         │
│                                                                 │
│  ⚡ SPEED                                                       │
│     • Minutes to process leads vs hours/days                    │
│     • Parallel processing vs sequential                         │
│                                                                 │
│  🎨 PERSONALIZATION                                             │
│     • Unique proposal per lead vs templates                     │
│     • Website preview included vs text only                     │
│                                                                 │
│  ✅ QUALITY                                                     │
│     • Fact-checked content vs unverified                        │
│     • Human-in-the-loop vs fully automated                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. FUTURE ROADMAP

### Immediate Enhancements
- Industry specialization beyond website development
- ML-powered conversion prediction
- Multi-language support
- CRM integration (Salesforce, HubSpot)

### Long-term Vision
- Vertical expansion (legal, healthcare, consulting)
- AI-powered negotiation agents
- Predictive lead scoring
- Enterprise team collaboration features

### Platform Evolution
- Agent marketplace
- No-code agent builder
- Expanded integration ecosystem

---

## 13. TEAM & CREDITS

### Core Technologies Used

**AI & Agent Framework:**
- Google Agent Development Kit (ADK) 1.0.0
- Gemini 2.0 Flash Lite
- Vertex AI
- A2A SDK

**Google Cloud Services:**
- Google Cloud Run
- Google Cloud Pub/Sub
- Google Cloud Build
- Google Maps Places API
- Google Search API
- Gmail API
- Google Calendar API

**Database & Real-time:**
- Firebase Firestore
- Firebase Realtime Database
- Firebase Cloud Storage

**Authentication:**
- Clerk

**Communication:**
- Twilio (Phone calls)
- Gmail API (Emails)

**Frontend:**
- FastAPI + Jinja2
- HTML5/CSS3/JavaScript
- WebSocket

### Built For
Google Cloud / AI Hackathon 2026

---

## 14. KEY TAKEAWAYS FOR PPT

### Slide Suggestions

1. **Title Slide**: SalesShortcut - AI-Powered SDR Agent System
2. **Problem Statement**: Manual sales process pain points
3. **Solution Overview**: What SalesShortcut does
4. **Demo/Workflow**: Show the lead journey
5. **Architecture**: Microservices + Agent diagram
6. **Tech Stack**: Google Cloud + ADK + Firebase + Clerk
7. **Innovation**: 34 agents, A2A, Google Cloud Native
8. **Key Features**: Discovery, Research, Outreach
9. **Challenges & Solutions**: How we overcame obstacles
10. **Demo Screenshots**: UI Dashboard with Clerk auth
11. **Future Vision**: Roadmap
12. **Closing**: Impact & call to action

### Key Stats to Highlight
- **34 AI Agents** orchestrated together
- **5 Microservices** in the architecture
- **16+ Specialized Tools** for various functions
- **End-to-End Automation** from discovery to closing
- **Google Cloud Native** - 10+ Google APIs/services
- **Firebase Real-time** - Live data synchronization
- **Clerk Authentication** - Secure user management

---

## 15. QUICK REFERENCE

### One-Sentence Pitch
> "SalesShortcut uses 34 AI agents powered by Google ADK and Gemini to automate the entire sales process - from finding leads on Google Maps to making phone calls and closing deals."

### Three Key Differentiators
1. **Scale**: 34 agents working in concert with Google ADK
2. **Google Cloud Native**: Full integration with Google ecosystem + Firebase
3. **Full Automation**: No manual intervention required

### Hackathon Focus
- Built entirely with **Google technologies** + Firebase
- Demonstrates **Google ADK mastery**
- Leverages **Google Cloud services**
- **Clerk** for secure authentication
- Real-world **business application**

### Complete Tech Stack Summary
```
┌─────────────────────────────────────────────────────────────┐
│                    SALESSHORTCUT TECH STACK                  │
├─────────────────────────────────────────────────────────────┤
│  AI LAYER                                                    │
│  ├── Google ADK 1.0.0 (Agent orchestration)                 │
│  ├── Gemini 2.0 Flash Lite (LLM)                            │
│  ├── Vertex AI (Model hosting)                              │
│  └── A2A SDK 0.2.5 (Agent communication)                    │
├─────────────────────────────────────────────────────────────┤
│  GOOGLE CLOUD SERVICES                                       │
│  ├── Cloud Run (Serverless deployment)                      │
│  ├── Cloud Pub/Sub (Email notifications)                    │
│  ├── Cloud Build (CI/CD)                                    │
│  ├── Maps Places API (Business discovery)                   │
│  ├── Search API (Web research)                              │
│  ├── Gmail API (Email send/receive)                         │
│  └── Calendar API (Meeting scheduling)                      │
├─────────────────────────────────────────────────────────────┤
│  DATABASE & STORAGE                                          │
│  ├── Firebase Firestore (Lead data)                         │
│  ├── Firebase Realtime DB (Live sync)                       │
│  └── Firebase Cloud Storage (Documents)                     │
├─────────────────────────────────────────────────────────────┤
│  AUTHENTICATION                                              │
│  └── Clerk (User auth & sessions)                           │
├─────────────────────────────────────────────────────────────┤
│  COMMUNICATION                                               │
│  ├── Twilio (Phone calls)                                   │
│  └── Gmail API (Email)                                      │
├─────────────────────────────────────────────────────────────┤
│  BACKEND                                                     │
│  ├── Python 3.9+                                            │
│  ├── FastAPI (REST API)                                     │
│  ├── Uvicorn (ASGI server)                                  │
│  └── Pydantic (Validation)                                  │
├─────────────────────────────────────────────────────────────┤
│  FRONTEND                                                    │
│  ├── HTML5/CSS3/JavaScript                                  │
│  ├── Jinja2 (Templating)                                    │
│  ├── WebSocket (Real-time)                                  │
│  └── Clerk Components (Auth UI)                             │
├─────────────────────────────────────────────────────────────┤
│  DEVOPS                                                      │
│  ├── Docker (Containers)                                    │
│  ├── Google Cloud Build (CI/CD)                             │
│  └── Cloud Run (Deployment)                                 │
└─────────────────────────────────────────────────────────────┘
```

---

*Built with passion during the hackathon - transforming manual sales processes into AI-powered automation with Google Cloud, Firebase, and Clerk!*
