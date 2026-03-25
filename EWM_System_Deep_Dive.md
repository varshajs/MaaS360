# EWM/ELM System Deep Dive: Understanding Work Items

A comprehensive guide to understanding how IBM Engineering Workflow Management (EWM) and Engineering Lifecycle Management (ELM) work, with detailed focus on work items and their mechanics.

---

## Table of Contents
1. [What is ELM? The Big Picture](#what-is-elm-the-big-picture)
2. [What is EWM? The Workflow Engine](#what-is-ewm-the-workflow-engine)
3. [Understanding Work Items in Depth](#understanding-work-items-in-depth)
4. [Work Item Lifecycle](#work-item-lifecycle)
5. [Work Item Anatomy](#work-item-anatomy)
6. [How Work Items Flow Through the System](#how-work-items-flow-through-the-system)
7. [Work Item Relationships in Detail](#work-item-relationships-in-detail)
8. [Real-World Scenarios](#real-world-scenarios)
9. [Technical Architecture](#technical-architecture)
10. [Key Takeaways](#key-takeaways)

---

## What is ELM? The Big Picture

### The Problem ELM Solves

Imagine you're building a complex product like a car. You need:
- **Requirements**: What features should the car have?
- **Design**: How will we build it?
- **Development**: Actually building the parts
- **Testing**: Making sure everything works
- **Quality**: Tracking defects and improvements
- **Traceability**: Knowing which requirement led to which design, which code, which test

**The Challenge**: In large organizations, these activities happen in different tools, by different teams, with no connection between them.

**ELM's Solution**: A unified platform where all engineering activities are connected and traceable.

### ELM: The Integrated Engineering Platform

Think of ELM as a **smart city** where everything is connected:
- Requirements are like **building permits** (what you're allowed to build)
- Work items are like **construction projects** (what you're actually building)
- Tests are like **inspections** (making sure it's built correctly)
- Quality metrics are like **city reports** (how well the city is functioning)

**Key Benefit**: Click on any item and see the complete chain from idea to delivery.

### ELM Components

| Component | Full Name | Purpose | Analogy |
|-----------|-----------|---------|---------|
| **DOORS Next** | Dynamic Object-Oriented Requirements System | Formal requirements management | Building blueprints |
| **EWM** | Engineering Workflow Management | Work tracking, source control, builds | Construction management |
| **ETM** | Engineering Test Management | Test planning and execution | Quality inspections |
| **RQM** | Rational Quality Manager | Quality metrics and reporting | City quality reports |
| **ERM** | Engineering Requirements Management | Requirements definition | Zoning regulations |

### How ELM Components Work Together

**Real-World Example: Building a Login Feature**

```
1. BUSINESS NEED
   "We need secure user authentication"
   
2. DOORS Next (Requirements)
   REQ-001: "System shall authenticate users via email/password"
   REQ-002: "System shall lock account after 5 failed attempts"
   REQ-003: "System shall support password reset"
   
3. EWM (Work Items)
   Epic #100: "User Authentication System"
   ├─ Feature #110: "Login Functionality"
   │  ├─ Story #111: "Email/password login" (implements REQ-001)
   │  ├─ Story #112: "Account lockout" (implements REQ-002)
   │  └─ Story #113: "Password reset" (implements REQ-003)
   
4. EWM (Code)
   Developer commits code linked to Story #111
   Code review, merge to main branch
   
5. ETM (Testing)
   Test Case TC-001: "Valid login succeeds" (validates REQ-001)
   Test Case TC-002: "5 failures lock account" (validates REQ-002)
   Test Case TC-003: "Password reset works" (validates REQ-003)
   
6. RQM (Quality)
   Test Results: 100% pass rate
   Code Coverage: 95%
   Defects: 0 critical, 2 minor
   
7. TRACEABILITY
   Click REQ-001 → See Story #111 → See Code Commit → See Test TC-001 → See Results
```

**The Power**: If a requirement changes, you instantly know which code, tests, and work items are affected.

---

## What is EWM? The Workflow Engine

### EWM's Core Purpose

EWM is the **execution engine** of ELM. While other tools define what to build (requirements) and how to verify it (tests), EWM manages the actual work of building it.

**Think of EWM as**: The project manager + version control + build system all in one.

### What EWM Manages

#### 1. Work Items (The "What")
- Epics, Features, Stories, Tasks, Defects
- Status, priority, assignments
- Relationships and dependencies

#### 2. Source Code (The "How")
- Version control (like Git)
- Branching and merging
- Code reviews
- Change tracking

#### 3. Builds (The "Delivery")
- Automated builds
- Continuous integration
- Deployment tracking
- Build results

#### 4. Process (The "Rules")
- Workflows (how work moves through states)
- Approvals (who can approve what)
- Permissions (who can do what)
- Notifications (who gets alerted when)

### EWM Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    EWM SERVER                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Work Item   │  │    Source    │  │    Build     │ │
│  │  Management  │  │    Control   │  │    Engine    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│         │                 │                  │         │
│         └─────────────────┴──────────────────┘         │
│                          │                             │
│                  ┌───────┴────────┐                    │
│                  │   Database     │                    │
│                  │  (Work Items,  │                    │
│                  │   Code, Builds)│                    │
│                  └────────────────┘                    │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
   │  Web    │      │  Eclipse│      │  VS Code│
   │ Client  │      │  Client │      │  Plugin │
   └─────────┘      └─────────┘      └─────────┘
```

---

## Understanding Work Items in Depth

### What is a Work Item? (The Complete Picture)

A work item is **not just a task**. It's a sophisticated data structure that:

1. **Represents work** to be done
2. **Tracks progress** through its lifecycle
3. **Connects** to related work
4. **Enforces** process rules
5. **Stores** all relevant information
6. **Provides** audit trail
7. **Enables** reporting and metrics

### The Work Item as a Living Document

Think of a work item as a **living document** that evolves:

**Birth** (Creation):
```
Story #12345 created
- Title: "Password reset"
- Status: New
- Description: Basic idea
- Owner: None
- Estimate: Unknown
```

**Childhood** (Refinement):
```
Story #12345 refined
- Description: Detailed with acceptance criteria
- Owner: Still none
- Estimate: 5 story points
- Status: Open (ready for work)
```

**Adolescence** (Development):
```
Story #12345 in progress
- Owner: John Developer
- Status: In Progress
- Tasks: 4 created
- Code: 3 commits linked
- Time spent: 8 hours
```

**Adulthood** (Completion):
```
Story #12345 complete
- Status: Closed
- All tasks: Done
- Tests: Passed
- Demonstrated: Sprint review
- Actual effort: 12 hours
```

**Legacy** (Historical Record):
```
Story #12345 archived
- Complete history preserved
- Metrics contributed to velocity
- Lessons learned documented
- Referenced by future work
```

### Work Item Data Model

```json
{
  "workItem": {
    "identity": {
      "id": 12345,
      "uuid": "abc-123-def-456",
      "type": "story",
      "typeId": "com.ibm.team.apt.workItemType.story"
    },
    "core": {
      "title": "Implement password reset via email",
      "description": "As a user, I want to reset my password...",
      "status": {
        "id": "inprogress",
        "name": "In Progress",
        "group": "open"
      },
      "priority": {
        "id": "priority.high",
        "name": "High"
      }
    },
    "ownership": {
      "owner": {
        "userId": "john.developer",
        "name": "John Developer",
        "email": "john.developer@company.com"
      },
      "creator": {
        "userId": "sarah.po",
        "name": "Sarah Product Owner"
      }
    },
    "planning": {
      "plannedFor": {
        "id": "sprint45",
        "name": "Sprint 45",
        "startDate": "2026-01-20",
        "endDate": "2026-02-02"
      },
      "filedAgainst": {
        "id": "auth-service",
        "name": "Authentication Service"
      },
      "teamArea": {
        "id": "backend-team",
        "name": "Backend Team"
      },
      "projectArea": {
        "id": "customer-portal",
        "name": "Customer Portal"
      }
    },
    "estimation": {
      "storyPoints": 5,
      "timeSpent": 28800,
      "timeRemaining": 14400,
      "complexity": "medium"
    },
    "relationships": {
      "parent": {
        "id": 12340,
        "type": "feature",
        "title": "User Authentication"
      },
      "children": [
        {"id": 12346, "type": "task", "title": "Create API endpoint"},
        {"id": 12347, "type": "task", "title": "Implement email service"},
        {"id": 12348, "type": "task", "title": "Add database fields"},
        {"id": 12349, "type": "task", "title": "Write unit tests"}
      ],
      "dependsOn": [
        {"id": 12320, "type": "story", "title": "Email service integration"}
      ],
      "tracksRequirement": [
        {"id": "REQ-AUTH-003", "title": "Password reset capability"}
      ]
    },
    "content": {
      "acceptanceCriteria": [
        "User receives reset email within 2 minutes",
        "Reset link expires after 24 hours",
        "User can set new password",
        "User is automatically logged in",
        "Old password no longer works"
      ],
      "comments": [
        {
          "id": 1,
          "author": "john.developer",
          "timestamp": "2026-01-20T10:30:00Z",
          "text": "Starting work on API endpoint"
        },
        {
          "id": 2,
          "author": "sarah.po",
          "timestamp": "2026-01-21T14:15:00Z",
          "text": "Please ensure password complexity requirements"
        }
      ],
      "attachments": [
        {"name": "password-reset-flow.png", "size": 45678},
        {"name": "api-specification.pdf", "size": 123456}
      ]
    },
    "metadata": {
      "created": "2026-01-15T10:30:00Z",
      "modified": "2026-01-22T16:30:00Z",
      "resolved": null,
      "closed": null,
      "version": 15
    },
    "customFields": {
      "businessValue": 8,
      "riskLevel": "low",
      "customerImpact": "high"
    }
  }
}
```

---

## Work Item Lifecycle

### Complete Lifecycle Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    WORK ITEM LIFECYCLE                      │
└─────────────────────────────────────────────────────────────┘

    [IDEA/NEED]
         │
         ▼
    ┌─────────┐
    │   NEW   │ ◄─── Created, awaiting review
    └────┬────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐  ┌──────────┐
│  OPEN  │  │ REJECTED │ ◄─── Not needed
└───┬────┘  └──────────┘
    │
    │ Sprint Planning
    ▼
┌──────────────┐
│ IN PROGRESS  │ ◄─── Active development
└──────┬───────┘
       │
       │ Work complete
       ▼
┌──────────┐
│ RESOLVED │ ◄─── Ready for verification
└────┬─────┘
     │
┌────┴────┐
│         │
▼         ▼
┌────────┐  ┌──────────────┐
│ CLOSED │  │ IN PROGRESS  │ ◄─── Issues found, back to dev
└────────┘  └──────────────┘
   │
   ▼
[COMPLETE]
```

### Detailed State Descriptions

#### NEW State
**Meaning**: Work item just created, not yet reviewed or approved

**Who can create**: Anyone with permissions (typically Product Owners, Team Leads)

**What happens here**:
- Initial triage
- Priority assessment
- Feasibility check
- Assignment to backlog

**Typical duration**: Hours to days

**Example**:
```
Customer Support creates Defect #12500
- Title: "App crashes on iOS 15"
- Priority: Unknown
- Owner: None
- Status: NEW

Product Owner reviews:
- Confirms it's a real issue
- Sets Priority: High
- Assigns to: Mobile Team backlog
- Status: NEW → OPEN
```

#### OPEN State
**Meaning**: Approved and ready to be worked on, waiting in backlog

**What happens here**:
- Backlog refinement
- Adding details (acceptance criteria, estimates)
- Breaking down into smaller pieces
- Identifying dependencies

**Typical duration**: Days to weeks

**Example**:
```
Story #12345 in OPEN state
- Has acceptance criteria
- Estimated at 5 points
- Dependencies identified
- Ready for sprint planning
```

#### IN PROGRESS State
**Meaning**: Someone is actively working on this

**What happens here**:
- Daily development work
- Code commits
- Status updates
- Time tracking
- Collaboration and discussion

**Typical duration**: Hours to days (for stories), days to weeks (for features)

**Example**:
```
Story #12345 IN PROGRESS
- Owner: John Developer
- Tasks: 2 of 4 complete
- Code commits: 3
- Time spent: 8 hours
- Blockers: None
```

#### RESOLVED State
**Meaning**: Work complete, awaiting verification

**What happens here**:
- QA testing
- Product Owner review
- Stakeholder demo
- Final verification

**Typical duration**: Hours to days

**Example**:
```
Story #12345 RESOLVED
- All tasks complete
- Code reviewed and merged
- Ready for QA testing
- Awaiting verification
```

#### CLOSED State
**Meaning**: Verified complete, no further work needed

**What happens here**:
- Final acceptance
- Metrics recorded
- Lessons learned
- Historical record

**Typical duration**: Permanent

**Example**:
```
Story #12345 CLOSED
- QA verified: All tests pass
- PO accepted: Demonstrated in sprint review
- Metrics: 5 points, 12 hours actual
- Sprint: Sprint 45 (complete)
```

#### REJECTED State
**Meaning**: Will not be done

**Reasons**:
- Duplicate of another item
- No longer needed
- Not feasible
- Out of scope

**Example**:
```
Story #12999 REJECTED
- Reason: Duplicate of #12345
- Comment: "Same functionality already implemented"
- No work performed
```

---

## Work Item Anatomy

### Visual Breakdown

Let me show you a complete work item with all its parts labeled:

```
╔═══════════════════════════════════════════════════════════╗
║ WORK ITEM #12345                                          ║
╠═══════════════════════════════════════════════════════════╣
║ HEADER BAR                                                ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ 📋 Story  │  🔴 High  │  ⏳ In Progress  │  👤 John  │ ║
║ └───────────────────────────────────────────────────────┘ ║
╠═══════════════════════════════════════════════════════════╣
║ TITLE                                                     ║
║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ║
║ ┃ Implement password reset via email                   ┃ ║
║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ║
╠═══════════════════════════════════════════════════════════╣
║ TABS                                                      ║
║ [Overview] [Links] [Approvals] [History] [Attachments]   ║
╠═══════════════════════════════════════════════════════════╣
║ OVERVIEW TAB                                              ║
║                                                           ║
║ Description                                               ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ As a user, I want to reset my password via email     │ ║
║ │ so that I can regain access if I forget it.          │ ║
║ │                                                       │ ║
║ │ **User Flow:**                                        │ ║
║ │ 1. Click "Forgot Password"                           │ ║
║ │ 2. Enter email address                               │ ║
║ │ 3. Receive reset link                                │ ║
║ │ 4. Click link and set new password                   │ ║
║ └───────────────────────────────────────────────────────┘ ║
║                                                           ║
║ Acceptance Criteria                                       ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ ☑ Email sent within 2 minutes                        │ ║
║ │ ☑ Link expires after 24 hours                        │ ║
║ │ ☑ New password meets complexity rules                │ ║
║ │ ☑ Auto-login after reset                             │ ║
║ │ ☑ Old password invalidated                           │ ║
║ └───────────────────────────────────────────────────────┘ ║
║                                                           ║
║ Details                                                   ║
║ ┌─────────────────┬─────────────────────────────────────┐ ║
║ │ Owner           │ john.developer@company.com          │ ║
║ │ Planned For     │ Sprint 45 (Jan 20 - Feb 2)        │ ║
║ │ Filed Against   │ Authentication Service              │ ║
║ │ Team Area       │ Backend Team                        │ ║
║ │ Story Points    │ 5                                   │ ║
║ │ Time Spent      │ 8h                                  │ ║
║ │ Time Remaining  │ 4h                                  │ ║
║ │ Created         │ Jan 15, 2026 by sarah.po           │ ║
║ │ Modified        │ Jan 22, 2026 by john.developer     │ ║
║ └─────────────────┴─────────────────────────────────────┘ ║
╠═══════════════════════════════════════════════════════════╣
║ LINKS TAB                                                 ║
║                                                           ║
║ Parent                                                    ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ ⬆️ Feature #12340: User Authentication               │ ║
║ └───────────────────────────────────────────────────────┘ ║
║                                                           ║
║ Children                                                  ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ ⬇️ Task #12346: Create API endpoint [Closed]         │ ║
║ │ ⬇️ Task #12347: Implement email service [Closed]     │ ║
║ │ ⬇️ Task #12348: Add database fields [In Progress]    │ ║
║ │ ⬇️ Task #12349: Write unit tests [Open]              │ ║
║ └───────────────────────────────────────────────────────┘ ║
║                                                           ║
║ Dependencies                                              ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ ⚠️ Depends On: Story #12320 [Closed]                 │ ║
║ │    "Email service integration"                        │ ║
║ └───────────────────────────────────────────────────────┘ ║
║                                                           ║
║ Requirements                                              ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ 📋 Tracks: REQ-AUTH-003                               │ ║
║ │    "System shall support password reset"             │ ║
║ └───────────────────────────────────────────────────────┘ ║
╠═══════════════════════════════════════════════════════════╣
║ COMMENTS                                                  ║
║ ┌───────────────────────────────────────────────────────┐ ║
║ │ 💬 john.developer - Jan 20, 10:30 AM                 │ ║
║ │    "Starting work on API endpoint"                    │ ║
║ │                                                       │ ║
║ │ 💬 sarah.po - Jan 21, 2:15 PM                        │ ║
║ │    "Please ensure password complexity requirements"   │ ║
║ │                                                       │ ║
║ │ 💬 john.developer - Jan 22, 9:00 AM                  │ ║
║ │    "API complete, starting email integration"         │ ║
║ └───────────────────────────────────────────────────────┘ ║
╚═══════════════════════════════════════════════════════════╝
```

### Field-by-Field Explanation

#### Identity Fields

**ID**: `#12345`
- Unique identifier
- Never changes
- Used for references
- Sequential or UUID-based

**Type**: `Story`
- Determines available fields
- Defines workflow
- Sets permissions
- Influences reporting

**Title**: `"Implement password reset via email"`
- Short, descriptive
- Appears in lists
- Searchable
- 50-100 characters ideal

#### Status & Priority

**Status**: `In Progress`
- Current lifecycle state
- Drives workflow
- Determines who can act
- Affects metrics

**Priority**: `High`
- Relative importance
- Affects scheduling
- Influences resource allocation
- Set by Product Owner

#### Ownership

**Owner**: `john.developer@company.com`
- Accountable person
- Receives notifications
- Updates status
- One owner at a time

**Creator**: `sarah.po`
- Who created it
- Historical record
- Never changes

#### Planning

**Planned For**: `Sprint 45`
- When it will be done
- Affects capacity planning
- Drives commitment
- Can be changed

**Filed Against**: `Authentication Service`
- Which component/module
- Routes to correct team
- Enables component reporting
- Hierarchical structure

**Team Area**: `Backend Team`
- Which team owns it
- Affects permissions
- Drives notifications
- Team-level reporting

**Story Points**: `5`
- Relative effort estimate
- Used for velocity
- Planning tool
- Not hours!

#### Time Tracking

**Time Spent**: `8 hours`
- Actual work performed
- Cumulative
- Used for metrics
- Optional but valuable

**Time Remaining**: `4 hours`
- Estimated work left
- Updated regularly
- Burndown calculation
- Helps identify issues early

---

## How Work Items Flow Through the System

### The Daily Flow

Let's follow a typical day in the life of a work item:

**8:00 AM - Morning**
```
Developer John logs into EWM
- Sees his assigned work items
- Story #12345 is "In Progress"
- 2 tasks remaining
```

**9:00 AM - Daily Standup**
```
John updates team:
"Yesterday: Completed API endpoint
 Today: Working on email integration
 Blockers: None"
```

**9:15 AM - Start Work**
```
John opens Task #12347 "Implement email service"
- Status: Open → In Progress
- Starts timer
- Opens IDE
```

**9:30 AM - Code Commit**
```
John commits code:
git commit -m "Add email service integration #12347"

EWM automatically:
- Links commit to Task #12347
- Updates work item with commit reference
- Notifies team of progress
```

**12:00 PM - Lunch Update**
```
John updates Task #12347:
- Time Spent: 3 hours
- Time Remaining: 2 hours
- Comment: "Email integration 60% complete"
```

**3:00 PM - Task Complete**
```
John finishes Task #12347:
- Status: In Progress → Closed
- Time Spent: 5 hours (total)
- Comment: "Email integration complete, tested locally"
- Commits final code
```

**3:30 PM - Story Update**
```
John checks Story #12345:
- 3 of 4 tasks complete
- Only "Write unit tests" remaining
- Updates Story comment: "Almost done, just tests left"
```

**4:00 PM - Blocker Found**
```
John starts Task #12349 "Write unit tests"
- Discovers test framework issue
- Creates Impediment #12600
- Links to Story #12345
- Notifies Scrum Master
```

**5:00 PM - End of Day**
```
John updates EWM:
- Task #12349: Still In Progress
- Time Spent: 1 hour
- Time Remaining: 3 hours (increased due to blocker)
- Comment: "Blocked by test framework issue #12600"
```

### The Sprint Flow

**Week 1: Sprint Planning**
```
Monday:
- Sprint 45 starts
- Team commits to 40 story points
- Story #12345 included (5 points)
- John volunteers to own it

Tuesday-Friday:
- John works on tasks
- Daily updates
- Progress tracked
```

**Week 2: Development & Testing**
```
Monday-Wednesday:
- John completes development
- Story #12345: In Progress → Resolved
- QA picks up for testing

Thursday:
- QA finds issue
- Creates Defect #12700
- Story #12345: Resolved → In Progress
- John fixes defect

Friday:
- John fixes issue
- Story #12345: In Progress → Resolved (again)
- QA retests, passes
- Story ready for review
```

**Sprint Review**
```
Last day of sprint:
- Team demonstrates Story #12345
- Stakeholders approve
- Product Owner accepts
- Story #12345: Resolved → Closed
- Sprint 45 complete!
```

---

## Work Item Relationships in Detail

### Why Relationships Matter

Relationships connect work items to create a **web of dependencies** that:
1. Shows how work breaks down (parent-child)
2. Tracks what blocks what (dependencies)
3. Links requirements to implementation (traceability)
4. Identifies risks (affected by defects)

### Relationship Types Explained

#### 1. Parent-Child (Hierarchy)

**Purpose**: Break large work into smaller pieces

**Example**:
```
Epic #100 "User Authentication System"
├─ Feature #110 "Login Functionality"
│  ├─ Story #111 "Email/password login"
│  │  ├─ Task #1111 "Create login API"
│  │  ├─ Task #1112 "Add UI form"
│  │  └─ Task #1113 "Write tests"
│  ├─ Story #112 "Social media login"
│  └─ Story #113 "Two-factor authentication"
├─ Feature #120 "Password Management"
│  ├─ Story #121 "Password reset"
│  └─ Story #122 "Password strength meter"
└─ Feature #130 "Account Security"
   ├─ Story #131 "Account lockout"
   └─ Story #132 "Login history"
```

**Rules**:
- Child cannot be closed if parent is closed
- Parent progress rolls up from children
- Deleting parent can delete children (configurable)

#### 2. Depends On / Blocks

**Purpose**: Show sequential dependencies

**Example**:
```
Story #121 "Password reset"
  Depends On: Story #120 "Email service integration"
  
Why? Can't reset password without email service!

This means:
- Story #120 must complete first
- Story #121 is blocked until #120 is done
- Critical path identified
```

**Visual**:
```
#120 Email Service ──► #121 Password Reset ──► #122 Password Strength
     (must finish)        (can start)            (can start)
```

#### 3. Tracks / Implements / Affects Requirement

**Purpose**: Link work to formal requirements

**Example**:
```
Requirement REQ-AUTH-003:
"System shall support password reset via email"

Work Items:
- Story #121 "Password reset" (Implements REQ-AUTH-003)
- Task #1211 "Create reset API" (Implements REQ-AUTH-003)
- Test Case TC-003 "Test password reset" (Validates REQ-AUTH-003)

Traceability Chain:
REQ-AUTH-003 → Story #121 → Task #1211 → Code Commit abc123 → Test TC-003
```

**Benefits**:
- Know which requirements are implemented
- Know which code implements which requirement
- Impact analysis when requirements change

#### 4. Affected By Defect

**Purpose**: Track quality issues impacting work

**Example**:
```
Feature #110 "Login Functionality"
  Affected By: Defect #500 "Login fails on iOS"
  Affected By: Defect #501 "Slow login on Android"

This means:
- Feature is complete but has known issues
- Defects must be fixed before feature is truly done
- Quality metrics affected
```

#### 5. Related To

**Purpose**: General association between work items

**Example**:
```
Story #121 "Password reset"
  Related To: Story #131 "Account lockout"
  
Why? Both deal with account security, might share code
```

### Relationship Best Practices

#### DO:
✅ Link stories to parent features
✅ Link tasks to parent stories
✅ Link defects to affected work
✅ Link work to requirements
✅ Document why relationships exist

#### DON'T:
❌ Create circular dependencies (A depends on B, B depends on A)
❌ Over-link everything (creates noise)
❌ Forget to update when relationships change
❌ Link unrelated items just because

---

## Real-World Scenarios

### Scenario 1: New Feature Request

**Situation**: Customer requests "Export data to Excel"

**Flow**:
```
1. Customer Support creates Story #2000
   - Title: "Export data to Excel"
   - Description: Customer feedback
   - Status: NEW

2. Product Owner reviews
   - Realizes it's bigger than a story
   - Creates Feature #200 "Data Export"
   - Converts Story #2000 to child story
   - Status: NEW → OPEN

3. Team refines Feature #200
   - Breaks into stories:
     * Story #2001 "Export to Excel"
     * Story #2002 "Export to PDF"
     * Story #2003 "Export to CSV"
   - Estimates: 13 points total
   - Planned For: Sprint 50

4. Sprint 50 Planning
   - Team commits to Stories #2001 and #2003
   - Story #2002 deferred to Sprint 51
   - Developers assigned

5. Development
   - Developer creates tasks
   - Implements functionality
   - Commits code
   - Updates status

6. Testing
   - QA tests exports
   - Finds issue with large datasets
   - Creates Defect #2100
   - Links to Story #2001

7. Fix & Retest
   - Developer fixes defect
   - QA retests
   - All tests pass

8. Completion
   - Stories #2001 and #2003 closed
   - Feature #200 partially complete
   - Story #2002 remains for next sprint
```

### Scenario 2: Critical Production Defect

**Situation**: Production system down, users can't login

**Flow**:
```
1. 2:00 AM - Alert triggered
   - Monitoring system detects issue
   - On-call engineer notified

2. 2:15 AM - Initial triage
   - Engineer creates Defect #3000
   - Title: "Login system down"
   - Priority: CRITICAL
   - Severity: CRITICAL
   - Status: NEW → OPEN immediately

3. 2:30 AM - Investigation
   - Engineer adds comments with findings
   - Links to related logs
   - Identifies root cause: database connection pool exhausted

4. 3:00 AM - Fix deployed
   - Engineer implements hotfix
   - Commits code linked to Defect #3000
   - Deploys to production
   - System restored

5. 3:30 AM - Verification
   - QA verifies fix in production
   - Monitoring confirms system healthy
   - Defect #3000: OPEN → RESOLVED

6. Next Day - Post-mortem
   - Team reviews incident
   - Creates Story #3001 "Increase connection pool"
   - Creates Story #3002 "Add connection pool monitoring"
   - Links both to Defect #3000
   - Defect #3000: RESOLVED → CLOSED

7. Follow-up
   - Stories #3001 and #3002 planned for next sprint
   - Prevents future occurrences
```

### Scenario 3: Epic Planning & Execution

**Situation**: Company wants to add mobile app

**Flow**:
```
1. Quarter Planning
   - Executive team approves initiative
   - Product creates Portfolio Epic #1000
   - Title: "Mobile Application Platform"
   - Budget: $2M
   - Timeline: 12 months

2. Program Planning
   - Breaks into Program Epics:
     * Epic #1100 "iOS App" (6 months)
     * Epic #1200 "Android App" (6 months)
     * Epic #1300 "Backend API" (3 months)
   - Epic #1300 must complete first (dependency)

3. PI Planning (Quarter 1)
   - Epic #1300 breaks into Features:
     * Feature #1310 "User Authentication API"
     * Feature #1320 "Data Sync API"
     * Feature #1330 "Push Notification API"
   - All planned for PI-1 (Q1)

4. Sprint Planning (Sprint 1)
   - Feature #1310 breaks into Stories:
     * Story #13101 "Login endpoint"
     * Story #13102 "Registration endpoint"
     * Story #13103 "Token management"
   - Stories planned across Sprints 1-3

5. Development (Sprints 1-12)
   - Teams work on stories
   - Complete features
   - Integrate components
   - Test end-to-end

6. Release (End of Q4)
   - All epics complete
   - Mobile apps launched
   - Portfolio Epic #1000 closed
   - Success metrics tracked
```

---

## Technical Architecture

### How EWM Stores Work Items

**Database Structure**:
```
┌─────────────────────────────────────────┐
│         WORK_ITEMS Table                │
├─────────────────────────────────────────┤
│ id (primary key)                        │
│ uuid (unique identifier)                │
│ type_id (foreign key to TYPES)         │
│ title (varchar)                         │
│ description (text)                      │
│ status_id (foreign key to STATUSES)    │
│ priority_id (foreign key to PRIORITIES)│
│ owner_id (foreign key to USERS)        │
│ creator_id (foreign key to USERS)      │
│ created_date (timestamp)                │
│ modified_date (timestamp)               │
│ ... (many more fields)                  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│      WORK_ITEM_LINKS Table              │
├─────────────────────────────────────────┤
│ id (primary key)                        │
│ source_id (foreign key to WORK_ITEMS)  │
│ target_id (foreign key to WORK_ITEMS)  │
│ link_type (parent, depends_on, etc.)   │
│ created_date (timestamp)                │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│      WORK_ITEM_HISTORY Table            │
├─────────────────────────────────────────┤
│ id (primary key)                        │
│ work_item_id (foreign key)              │
│ field_name (varchar)                    │
│ old_value (text)                        │
│ new_value (text)                        │
│ changed_by (foreign key to USERS)      │
│ changed_date (timestamp)                │
└─────────────────────────────────────────┘
```

### REST API Structure

**Get Work Item**:
```
GET /ccm/oslc/workitems/12345
Accept: application/json

Response:
{
  "dcterms:identifier": "12345",
  "dcterms:title": "Implement password reset",
  "rtc_cm:state": "inprogress",
  ...
}
```

**Update Work Item**:
```
PUT /ccm/oslc/workitems/12345
Content-Type: application/json

{
  "rtc_cm:state": "resolved",
  "rtc_cm:timeSpent": 28800
}
```

**Query Work Items**:
```
GET /ccm/oslc/queries/workitems?
  oslc.where=rtc_cm:state="inprogress" and 
  rtc_cm:owner="john.developer"
```

---

## Key Takeaways

### Understanding ELM/EWM

1. **ELM is the ecosystem**, EWM is the workflow engine
2. **Everything is connected**: Requirements → Work → Code → Tests → Results
3. **Traceability is key**: Know the complete chain from idea to delivery
4. **Integration matters**: Tools work better together than separately

### Understanding Work Items

1. **Work items are living documents** that evolve through their lifecycle
2. **Different types serve different purposes** - use the right type for the right level
3. **Relationships create context** - link related work for better understanding
4. **Status drives workflow** - understand the lifecycle to work effectively
5. **Details matter** - good descriptions and acceptance criteria prevent rework

### Best Practices

1. **Keep work items updated** - stale data helps no one
2. **Link related items** - relationships provide valuable context
3. **Use appropriate types** - don't make everything a story
4. **Write clear descriptions** - future you will thank present you
5. **Track time honestly** - metrics help improve estimation
6. **Comment frequently** - document decisions and progress
7. **Close completed work** - keep backlog clean

### Common Pitfalls to Avoid

1. ❌ Creating work items that are too large
2. ❌ Not linking related work
3. ❌ Forgetting to update status
4. ❌ Vague descriptions without acceptance criteria
5. ❌ Not tracking dependencies
6. ❌ Leaving work items in limbo
7. ❌ Not documenting decisions in comments

---

## Quick Reference

### Work Item Lifecycle Cheat Sheet

| State | Meaning | Who Acts | Next State |
|-------|---------|----------|------------|
| NEW | Just created | Product Owner | OPEN or REJECTED |
| OPEN | Ready for work | Team | IN PROGRESS |
| IN PROGRESS | Being worked on | Developer | RESOLVED |
| RESOLVED | Work complete | QA/PO | CLOSED or IN PROGRESS |
| CLOSED | Verified complete | - | - |
| REJECTED | Won't do | - | - |

### Relationship Types Cheat Sheet

| Relationship | Purpose | Example |
|--------------|---------|---------|
| Parent-Child | Hierarchy | Feature → Story → Task |
| Depends On | Sequential | Story A must finish before Story B |
| Blocks | Prevents progress | Defect blocks Feature |
| Tracks Requirement | Traceability | Story implements Requirement |
| Affected By Defect | Quality | Feature has known Defect |
| Related To | Association | Similar stories |

### When to Use Which Type

| Situation | Use This Type |
|-----------|---------------|
| Strategic initiative (12+ months) | Portfolio Epic |
| Cross-ART initiative (6-12 months) | Solution Epic |
| Program initiative (3-6 months) | Program Epic |
| Deliverable feature (1-3 months) | Feature |
| User-facing functionality (1-2 weeks) | Story |
| Technical implementation (hours-days) | Task |
| Something broken | Defect |
| Potential problem | Risk |
| Current blocker | Impediment |

---

**Document Version**: 1.0  
**Last Updated**: 2026-03-06  
**Companion Documents**: 
- EWM_Agent_Architecture_Guide.md
- EWM_Domain_Glossary.md