# EWM & Agile Domain Glossary

A comprehensive guide to understanding all the terminology used in Engineering Workflow Management (EWM) and Agile/SAFe methodologies.

---

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Work Item Types](#work-item-types)
3. [SAFe Framework Terms](#safe-framework-terms)
4. [Agile Methodology Terms](#agile-methodology-terms)
5. [Work Item Fields & Attributes](#work-item-fields--attributes)
6. [Relationships & Dependencies](#relationships--dependencies)
7. [Process & Workflow Terms](#process--workflow-terms)
8. [Real-World Examples](#real-world-examples)

---

## Core Concepts

### Work Item
**Definition**: A unit of work that needs to be tracked, managed, and completed in a software development project.

**Think of it as**: A digital task card that contains all information about something that needs to be done.

**Contains**:
- Title and description
- Status (New, In Progress, Done, etc.)
- Owner/Assignee
- Priority
- Dates (created, due, completed)
- Relationships to other work items
- Comments and discussions
- Attachments

**Example**: "Implement user login feature" or "Fix crash on iOS app startup"

---

### EWM (Engineering Workflow Management)
**Definition**: IBM's tool for managing the entire software development lifecycle using agile methodologies.

**Previously known as**: RTC (Rational Team Concert)

**What it does**:
- Tracks work items (stories, tasks, defects)
- Manages sprints and releases
- Provides dashboards and reports
- Integrates with source control
- Supports SAFe framework

**Think of it as**: Jira or Azure DevOps, but IBM's version with deep SAFe integration.

---

### ELM (Engineering Lifecycle Management)
**Definition**: IBM's suite of tools for managing the complete engineering lifecycle.

**Components**:
- **EWM**: Workflow and work item management
- **ETM**: Test management
- **DOORS Next**: Requirements management
- **ERM**: Requirements management
- **RQM**: Quality management

**Think of it as**: An integrated ecosystem where all engineering activities are connected.

---

### Planning Level
**Definition**: The hierarchical level at which work is planned and executed in SAFe.

**Levels** (from highest to lowest):
1. **Portfolio Level**: Strategic, multi-year initiatives
2. **Program Level**: Quarterly planning (PI - Program Increment)
3. **Team Level**: Sprint planning (2-week iterations)
4. **Execution Level**: Daily work

**Why it matters**: Different levels need different detail. Executives don't need to know about individual code commits; developers don't need to know about portfolio strategy.

---

## Work Item Types

### Epic
**Definition**: A large body of work that delivers significant business value and spans multiple sprints or Program Increments (PIs).

**Size**: Typically 3-6 months of work

**Contains**: Multiple Features or Capabilities

**Key Characteristics**:
- Strategic importance
- Requires hypothesis statement
- Has success criteria
- Needs approval before implementation

**Example**: "Implement AI-powered recommendation engine for e-commerce platform"

**Real-world analogy**: Building a new wing of a house (not just painting a room)

---

### Portfolio Epic
**Definition**: The largest work item type representing strategic initiatives that span multiple programs and solutions.

**Size**: 6-12+ months, enterprise-wide impact

**Audience**: Executives, Portfolio Managers, Business Owners

**Key Characteristics**:
- Strategic business value
- Significant investment required
- Affects multiple ARTs (Agile Release Trains)
- Requires executive approval

**Example**: "Digital transformation initiative to migrate all services to cloud"

**Real-world analogy**: Company-wide transformation (like Amazon becoming a cloud provider)

---

### Solution Epic
**Definition**: Large initiatives that require coordination across multiple Agile Release Trains (ARTs) to deliver a complete solution.

**Size**: 6-12 months, solution-wide impact

**Audience**: Solution Management, Solution Architects

**Key Characteristics**:
- Requires multiple ARTs to deliver
- Solution-level coordination
- Complex dependencies
- Architectural significance

**Example**: "Build unified customer data platform integrating CRM, billing, and support systems"

**Real-world analogy**: Building a complete smart home system (requires electrical, plumbing, networking teams)

---

### Program Epic / ART Epic
**Definition**: Epics that are scoped to a single Agile Release Train (ART) or program.

**Size**: 3-6 months, program-level impact

**Audience**: Product Management, Program Managers

**Key Characteristics**:
- Single ART delivery
- Program-level coordination
- Multiple features
- PI-level planning

**Example**: "Redesign mobile app user experience for iOS and Android"

**Real-world analogy**: Renovating your kitchen (significant but contained to one area)

---

### Feature
**Definition**: A service or functionality that delivers business value and can be completed within a Program Increment (PI).

**Size**: 1-3 months (typically fits in one PI)

**Contains**: Multiple User Stories

**Key Characteristics**:
- Delivers tangible value
- Has acceptance criteria
- Can be demonstrated to stakeholders
- Fits in a PI (10-12 weeks)

**Example**: "User profile management with photo upload and bio editing"

**Real-world analogy**: Installing a new kitchen appliance (dishwasher, oven)

---

### Capability
**Definition**: Similar to a Feature but at the solution level, requiring coordination across multiple ARTs.

**Size**: 1-3 months, cross-ART coordination

**Difference from Feature**: Capabilities span multiple ARTs; Features are within a single ART

**Example**: "Single sign-on across all company applications"

**Real-world analogy**: Installing a whole-house water filtration system (affects multiple rooms/systems)

---

### User Story (Story)
**Definition**: A small, user-focused requirement that can be completed within a single sprint (1-2 weeks).

**Size**: 1-5 days of work

**Format**: "As a [user type], I want [goal] so that [benefit]"

**Contains**: Tasks (technical implementation steps)

**Key Characteristics**:
- User-centric
- Testable
- Independent (can be developed separately)
- Negotiable (details can be discussed)
- Small (fits in a sprint)

**Example**: "As a customer, I want to reset my password via email so that I can regain access to my account"

**Real-world analogy**: A single recipe in a cookbook (specific, actionable, complete)

---

### Task
**Definition**: A technical implementation step required to complete a User Story.

**Size**: 2-8 hours of work

**Key Characteristics**:
- Technical focus (not user-facing)
- Assigned to specific developer
- Tracked in hours
- Part of a story

**Examples**:
- "Create database migration for password reset tokens"
- "Implement email service integration"
- "Write unit tests for password validation"
- "Update API documentation"

**Real-world analogy**: Individual steps in a recipe (chop onions, heat oil, add spices)

---

### Defect (Bug)
**Definition**: An error, flaw, or unintended behavior in the software that needs to be fixed.

**Key Characteristics**:
- Describes what's broken
- Includes steps to reproduce
- Has severity/priority
- May block other work

**Severity Levels**:
- **Critical**: System crash, data loss, security breach
- **High**: Major feature broken, workaround exists
- **Medium**: Minor feature issue, cosmetic problems
- **Low**: Typos, minor UI issues

**Example**: "App crashes when user uploads image larger than 10MB"

**Real-world analogy**: A broken appliance that needs repair

---

### Risk
**Definition**: A potential problem or uncertainty that could negatively impact the project.

**Key Characteristics**:
- Probability (likelihood of occurring)
- Impact (severity if it occurs)
- Mitigation plan (how to prevent)
- Contingency plan (what to do if it happens)

**Example**: "Third-party API provider may not meet performance SLA during peak traffic"

**Real-world analogy**: Weather forecast for outdoor event (might rain, have backup plan)

---

### Impediment
**Definition**: An obstacle or blocker that prevents the team from making progress.

**Key Characteristics**:
- Actively blocking work
- Needs immediate attention
- Requires resolution
- Tracked by Scrum Master

**Examples**:
- "Development environment is down"
- "Waiting for legal approval on terms of service"
- "Key team member on unexpected leave"

**Real-world analogy**: Road construction blocking your commute route

---

### Retrospective
**Definition**: A work item type for capturing team reflections and improvement actions after a sprint or PI.

**Key Characteristics**:
- What went well
- What didn't go well
- Action items for improvement
- Team-focused

**Example**: "Sprint 23 Retrospective - Improve code review turnaround time"

**Real-world analogy**: Post-game analysis in sports (what worked, what to improve)

---

## SAFe Framework Terms

### SAFe (Scaled Agile Framework)
**Definition**: A framework for scaling agile practices across large organizations with multiple teams.

**Key Principles**:
- Align strategy to execution
- Built-in quality
- Transparency
- Program execution
- Leadership

**Think of it as**: A playbook for running agile at enterprise scale (100s or 1000s of people)

---

### ART (Agile Release Train)
**Definition**: A long-lived team of agile teams (50-125 people) that plans, commits, and executes together.

**Key Characteristics**:
- 5-12 agile teams
- Shared mission and backlog
- Synchronized planning and delivery
- Delivers every PI (10-12 weeks)

**Example**: "Mobile Apps ART" with iOS team, Android team, Backend API team, QA team

**Real-world analogy**: A train with multiple cars, all moving together toward the same destination

---

### PI (Program Increment)
**Definition**: A fixed timebox (typically 10-12 weeks) during which an ART delivers incremental value.

**Structure**:
- 8-12 weeks of development (4-6 sprints)
- PI Planning event (2 days at start)
- System Demo (every 2 weeks)
- Inspect & Adapt workshop (at end)
- Innovation & Planning sprint (final sprint)

**Example**: "Q1 2026 PI - January 6 to March 27"

**Real-world analogy**: A semester in school (fixed duration, planned outcomes, final exam)

---

### PI Planning
**Definition**: A 2-day event where all ART teams plan the upcoming Program Increment together.

**What happens**:
- Business context presentation
- Team breakouts for planning
- Draft plans and dependencies identified
- Management review and adjustments
- Final plan commitment

**Output**: PI Objectives, committed features, identified risks

**Real-world analogy**: Annual company kickoff meeting where everyone aligns on quarterly goals

---

### Epic Hypothesis Statement
**Definition**: A structured statement that articulates the expected value and outcomes of an Epic.

**Format**:
```
For [customers]
who [do something]
the [solution]
is a [something - the "how"]
that [provides this value]
Unlike [competitor/current solution]
our solution [does something better - the "why"]
```

**Example**:
```
For online shoppers
who struggle to find relevant products
the AI recommendation engine
is a personalized shopping assistant
that suggests products based on browsing history and preferences
Unlike generic product listings
our solution increases purchase conversion by 25%
```

**Why it matters**: Makes the value proposition testable and measurable

---

### Enabler
**Definition**: Work that supports future business functionality but doesn't directly deliver user value.

**Types**:
- **Architectural Enablers**: Infrastructure, platforms, frameworks
- **Research Enablers**: Spikes, prototypes, proof of concepts
- **Compliance Enablers**: Security, regulatory requirements

**Example**: "Upgrade database to support 10x traffic" (enables future features but isn't a feature itself)

**Real-world analogy**: Laying foundation before building a house

---

### WSJF (Weighted Shortest Job First)
**Definition**: A prioritization method that considers both value and effort.

**Formula**: WSJF = Cost of Delay / Job Duration

**Cost of Delay includes**:
- User/Business Value
- Time Criticality
- Risk Reduction/Opportunity Enablement

**Why it matters**: Helps prioritize work to maximize economic value

**Example**: High-value, quick-to-deliver features get priority over low-value, long-duration work

---

## Agile Methodology Terms

### Sprint
**Definition**: A fixed timebox (typically 1-2 weeks) during which a team completes a set of work items.

**Structure**:
- Sprint Planning (start)
- Daily Standups (every day)
- Sprint Review/Demo (end)
- Sprint Retrospective (end)

**Example**: "Sprint 45: March 1-14, 2026"

**Real-world analogy**: A two-week cooking challenge with specific dishes to complete

---

### Backlog
**Definition**: A prioritized list of work items waiting to be implemented.

**Types**:
- **Product Backlog**: All features/stories for the product
- **Sprint Backlog**: Stories committed for current sprint
- **Program Backlog**: Features for the ART
- **Portfolio Backlog**: Epics for the portfolio

**Key Characteristics**:
- Prioritized (most important at top)
- Refined (detailed enough to work on)
- Estimated (sized for planning)

**Real-world analogy**: A to-do list, but constantly re-prioritized

---

### Acceptance Criteria
**Definition**: Specific conditions that must be met for a work item to be considered complete.

**Format**: Often written as Given-When-Then scenarios

**Example for "Password Reset" story**:
- User receives reset email within 2 minutes
- Reset link expires after 24 hours
- User can set new password meeting complexity requirements
- User is automatically logged in after successful reset

**Why it matters**: Defines "done" objectively, prevents misunderstandings

---

### Success Criteria
**Definition**: Measurable outcomes that indicate an Epic has delivered its intended value.

**Difference from Acceptance Criteria**: Success criteria measure business impact; acceptance criteria verify functionality

**Example for "AI Recommendation Engine" epic**:
- 25% increase in purchase conversion rate
- 40% increase in average order value
- 90% user satisfaction score
- 50ms average response time

**Real-world analogy**: Business KPIs vs. feature checklist

---

### Definition of Done (DoD)
**Definition**: A shared understanding of what "complete" means for any work item.

**Typical DoD includes**:
- Code written and reviewed
- Unit tests passing (>80% coverage)
- Integration tests passing
- Documentation updated
- Deployed to staging environment
- Product Owner acceptance

**Why it matters**: Prevents "90% done" syndrome, ensures quality

---

### Velocity
**Definition**: The amount of work a team completes in a sprint, measured in story points.

**Example**: "Team velocity is 40 points per sprint"

**Uses**:
- Predict future capacity
- Plan sprint commitments
- Track team performance trends

**Real-world analogy**: Miles per hour for a car (measures speed/capacity)

---

### Story Points
**Definition**: A relative measure of effort/complexity for completing a story.

**Common Scale**: Fibonacci sequence (1, 2, 3, 5, 8, 13, 21)

**Considers**:
- Complexity
- Effort
- Uncertainty/Risk

**Example**:
- 1 point: Simple text change
- 3 points: Add new form field
- 8 points: Integrate third-party API
- 13 points: Redesign database schema

**Why not hours?**: Points account for complexity and uncertainty, not just time

---

### Scrum Master
**Definition**: The person responsible for facilitating the agile process and removing impediments.

**Responsibilities**:
- Facilitate ceremonies (standups, planning, retros)
- Remove blockers
- Coach team on agile practices
- Shield team from distractions
- Track metrics

**Not a manager**: Servant leader, not command-and-control

**Real-world analogy**: Sports coach (guides, facilitates, doesn't play)

---

### Product Owner
**Definition**: The person responsible for maximizing product value and managing the backlog.

**Responsibilities**:
- Define product vision
- Prioritize backlog
- Write/refine user stories
- Accept completed work
- Stakeholder communication

**Key skill**: Balancing business needs with technical constraints

**Real-world analogy**: Restaurant owner (decides menu, not how to cook)

---

## Work Item Fields & Attributes

### Status / State
**Definition**: The current lifecycle stage of a work item.

**Common States**:
- **New**: Just created, not yet reviewed
- **Open**: Approved and ready to work on
- **In Progress**: Actively being worked on
- **Resolved**: Work complete, awaiting verification
- **Closed**: Verified and complete
- **Rejected**: Not going to be done

**State Groups**:
- **Open**: New, Open, In Progress
- **Done**: Resolved, Closed
- **Close**: Rejected, Duplicate

---

### Priority
**Definition**: The importance/urgency of a work item.

**Common Levels**:
- **Critical/P1**: Must be done immediately
- **High/P2**: Important, do soon
- **Medium/P3**: Normal priority
- **Low/P4**: Nice to have

**Factors**:
- Business impact
- Customer impact
- Dependencies
- Time sensitivity

---

### Severity (for Defects)
**Definition**: The impact of a defect on the system.

**Levels**:
- **Critical**: System unusable, data loss
- **High**: Major feature broken
- **Medium**: Minor feature issue
- **Low**: Cosmetic issue

**Note**: Severity ≠ Priority (critical bug in unused feature = high severity, low priority)

---

### Owner / Assignee
**Definition**: The person responsible for completing the work item.

**Best Practices**:
- One owner per work item
- Owner can change as work progresses
- Owner is accountable for completion

---

### Filed Against
**Definition**: The component, module, or area of the product this work item relates to.

**Examples**:
- "Mobile App / iOS"
- "Backend / Authentication Service"
- "Web UI / Shopping Cart"

**Why it matters**: Helps route work to correct team, track issues by component

---

### Planned For
**Definition**: The sprint, release, or PI when this work is scheduled.

**Examples**:
- "Sprint 45"
- "Release 3.2"
- "Q1 2026 PI"

**Why it matters**: Enables roadmap planning and commitment tracking

---

### Team Area
**Definition**: The team responsible for this work item.

**Examples**:
- "Mobile Development Team"
- "Backend Services Team"
- "QA Team"

---

### Project Area
**Definition**: The project or product this work item belongs to.

**Examples**:
- "E-commerce Platform"
- "Mobile Banking App"
- "Customer Portal"

---

## Relationships & Dependencies

### Parent-Child Relationship
**Definition**: Hierarchical relationship where one work item contains others.

**Examples**:
- Epic → Features → Stories → Tasks
- Feature → Stories
- Story → Tasks

**Why it matters**: Enables rollup reporting, tracks progress at different levels

---

### Depends On
**Definition**: This work item cannot start until another work item is complete.

**Example**: "Implement payment processing" depends on "Set up payment gateway account"

**Impact**: Creates critical path, affects scheduling

---

### Blocks / Blocked By
**Definition**: This work item prevents another from progressing.

**Example**: "Database migration" blocks "Deploy new feature"

**Why it matters**: Identifies bottlenecks, prioritizes critical work

---

### Tracks Requirement
**Definition**: Links work item to a formal requirement document.

**Why it matters**: Ensures traceability from requirements to implementation

---

### Implements Requirement
**Definition**: This work item implements a specific requirement.

**Why it matters**: Tracks requirement coverage

---

### Affects Requirement
**Definition**: This work item impacts or changes a requirement.

**Why it matters**: Tracks requirement changes

---

### Affected By Defect
**Definition**: This work item is impacted by a defect.

**Example**: Feature "User Profile" is affected by defect "Profile photo upload fails"

**Why it matters**: Tracks quality issues, prioritizes defect fixes

---

### Related To
**Definition**: General relationship between work items.

**Use cases**:
- Similar issues
- Related features
- Duplicate detection

---

## Process & Workflow Terms

### Workflow
**Definition**: The sequence of states a work item moves through from creation to completion.

**Example Workflow**:
```
New → Open → In Progress → Resolved → Closed
         ↓
      Rejected
```

**Transitions**: Actions that move work item between states (e.g., "Start Progress", "Resolve", "Close")

---

### Approval
**Definition**: A formal review and sign-off required before work can proceed.

**Common Approvals**:
- Epic approval (before implementation)
- Architecture review
- Security review
- Release approval

**Approvers**: Specific roles with authority to approve (Product Owner, Architect, etc.)

---

### Iteration
**Definition**: Another term for Sprint - a fixed timebox for development.

**Why two terms?**: "Iteration" is more general; "Sprint" is Scrum-specific

---

### Release
**Definition**: A version of the software delivered to customers.

**Types**:
- **Major Release**: Significant new features (v2.0)
- **Minor Release**: Small features, improvements (v2.1)
- **Patch Release**: Bug fixes only (v2.1.1)

---

### Milestone
**Definition**: A significant point in the project timeline.

**Examples**:
- "Beta Release"
- "Feature Complete"
- "General Availability"

---

### Burndown Chart
**Definition**: A graph showing remaining work over time.

**X-axis**: Time (days in sprint)
**Y-axis**: Remaining work (story points or hours)

**Ideal**: Line slopes down to zero by end of sprint

**Why it matters**: Visual indicator of sprint progress and risk

---

## Real-World Examples

### Example 1: E-commerce Platform

**Portfolio Epic**: "Transform shopping experience with AI personalization"
- **Solution Epic**: "Build AI recommendation engine"
  - **Program Epic**: "Implement product recommendation system"
    - **Feature**: "Personalized homepage recommendations"
      - **Story**: "As a returning customer, I want to see recommended products on homepage"
        - **Task**: "Create recommendation API endpoint"
        - **Task**: "Implement collaborative filtering algorithm"
        - **Task**: "Design homepage recommendation widget"
      - **Story**: "As a customer, I want recommendations based on my browsing history"
        - **Task**: "Track user browsing events"
        - **Task**: "Store browsing history in database"
        - **Task**: "Update recommendation algorithm"
    - **Feature**: "Email recommendations"
      - **Story**: "As a customer, I want weekly email with recommended products"
      - **Story**: "As a customer, I want to unsubscribe from recommendation emails"

**Defect**: "Recommendation widget shows products already purchased"
**Risk**: "Third-party ML service may not scale to Black Friday traffic"
**Impediment**: "ML team waiting for production data access approval"

---

### Example 2: Mobile Banking App

**Epic**: "Enable mobile check deposit"
- **Feature**: "Photo capture and processing"
  - **Story**: "As a user, I want to photograph front of check"
  - **Story**: "As a user, I want to photograph back of check"
  - **Story**: "As a user, I want to see image quality feedback"
- **Feature**: "Deposit submission and tracking"
  - **Story**: "As a user, I want to submit check for deposit"
  - **Story**: "As a user, I want to track deposit status"
  - **Story**: "As a user, I want notification when deposit clears"

**Acceptance Criteria** (for "photograph check" story):
- Camera opens within 2 seconds
- Image quality validation provides real-time feedback
- User can retake photo if quality insufficient
- Photo is encrypted before storage

**Success Criteria** (for Epic):
- 50% of check deposits via mobile within 6 months
- 95% successful deposit rate
- Average processing time under 24 hours
- 4.5+ star rating in app stores

---

### Example 3: Work Item Lifecycle

**Day 1**: Product Owner creates **Story** "Password reset via email"
- Status: **New**
- Priority: **High**
- Planned For: **Sprint 45**

**Day 2**: Team reviews in backlog refinement
- Status: **Open**
- Story points: **5**
- Acceptance criteria added

**Day 3**: Sprint planning, developer picks up story
- Status: **In Progress**
- Owner: **John Developer**
- Creates **Tasks**:
  - "Create password reset API endpoint"
  - "Implement email service"
  - "Add reset token to database"
  - "Write unit tests"

**Day 5**: QA finds issue
- Creates **Defect**: "Reset link doesn't expire"
- Links to story: **Affects** relationship
- Developer fixes defect

**Day 7**: Work complete
- Status: **Resolved**
- All tasks: **Closed**
- Defect: **Closed**

**Day 8**: Product Owner verifies
- Status: **Closed**
- Story demonstrated in sprint review

---

## Quick Reference

### Work Item Size Guide

| Type | Duration | Team Size | Example |
|------|----------|-----------|---------|
| Portfolio Epic | 12+ months | Multiple ARTs | Digital transformation |
| Solution Epic | 6-12 months | Multiple ARTs | Unified data platform |
| Program Epic | 3-6 months | Single ART | Mobile app redesign |
| Feature | 1-3 months | Single team | User profile management |
| Story | 1-5 days | 1-2 developers | Password reset |
| Task | 2-8 hours | 1 developer | Create API endpoint |

### Priority vs Severity Matrix (for Defects)

|  | Low Severity | Medium Severity | High Severity | Critical Severity |
|---|---|---|---|---|
| **High Priority** | Typo on homepage | Search sometimes slow | Login fails 10% of time | Payment processing down |
| **Medium Priority** | Typo in help docs | Filter doesn't work | Profile page crashes | Data export broken |
| **Low Priority** | Typo in footer | Old browser warning | Admin tool glitch | Legacy feature broken |

### Common Abbreviations

- **ART**: Agile Release Train
- **DoD**: Definition of Done
- **DoR**: Definition of Ready
- **PI**: Program Increment
- **PO**: Product Owner
- **SAFe**: Scaled Agile Framework
- **SM**: Scrum Master
- **WSJF**: Weighted Shortest Job First
- **WIP**: Work In Progress
- **MVP**: Minimum Viable Product
- **MBI**: Minimum Business Increment

---

## Tips for New Team Members

### Understanding Work Item Hierarchy
Think of it like a book:
- **Portfolio Epic** = Series (Harry Potter)
- **Solution Epic** = Book (Philosopher's Stone)
- **Program Epic** = Part (The Boy Who Lived)
- **Feature** = Chapter (The Letters from No One)
- **Story** = Scene (Harry receives his Hogwarts letter)
- **Task** = Paragraph (Describe the owl delivery)

### When to Create What

**Create an Epic when**:
- Work spans multiple months
- Requires significant investment
- Needs executive approval
- Affects multiple teams

**Create a Feature when**:
- Work fits in a PI (10-12 weeks)
- Delivers complete functionality
- Can be demonstrated to stakeholders
- Requires multiple stories

**Create a Story when**:
- Work fits in a sprint (1-2 weeks)
- Delivers user value
- Can be tested independently
- Is small enough to estimate accurately

**Create a Task when**:
- Breaking down technical implementation
- Tracking individual developer work
- Need hour-level tracking

### Common Mistakes to Avoid

1. **Stories too large**: If story takes more than a sprint, break it down
2. **Missing acceptance criteria**: Always define "done" upfront
3. **Vague descriptions**: Be specific about what needs to be done
4. **Ignoring dependencies**: Always link related work items
5. **Wrong work item type**: Use Epic for strategic work, Story for tactical
6. **Not updating status**: Keep work items current
7. **Missing relationships**: Link defects to affected features

---

**Document Version**: 1.0  
**Last Updated**: 2026-03-06  
**Companion Document**: EWM_Agent_Architecture_Guide.md