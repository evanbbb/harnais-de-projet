# Questioning Methodology

Adapted from GSD's "Dream extraction, not requirements gathering" approach. Used by the `project-questioner` agent.

## Philosophy

Most projects fail not because of bad code, but because the wrong thing was built. Traditional requirements gathering produces dry, formal documents that miss the user's actual vision. Dream extraction uncovers what the user truly wants by following energy and making the abstract concrete.

## Four Question Types

### 1. Motivation Questions (Why)

Uncover the driving force behind the project.

- "What problem does this solve for you?"
- "What happens if this doesn't get built?"
- "What prompted you to start this now?"
- "Who benefits most from this?"

**Purpose**: Understand the real need, not just the stated request.

### 2. Concreteness Questions (What Specifically)

Turn abstract ideas into specific, buildable features.

- "When you say 'dashboard', what do you see on it?"
- "Walk me through what a user does on their first visit."
- "What's the simplest version that would make you happy?"
- "Can you give me an example of what that would look like?"

**Purpose**: Replace vague concepts with concrete behaviors.

### 3. Clarification Questions (What Do You Mean By)

Challenge assumptions and jargon.

- "When you say 'real-time', do you mean seconds or minutes?"
- "What does 'admin' mean in this context — what can they do?"
- "You mentioned 'integration' — with what systems specifically?"
- "What does 'simple' mean to you here?"

**Purpose**: Ensure shared understanding of terms and expectations.

### 4. Success Questions (How Will You Know)

Define observable success criteria.

- "How will you know this is working?"
- "What would a user say if this was done right?"
- "What's the first thing you'd test?"
- "If I showed you the finished product, what would you check?"

**Purpose**: Create verifiable acceptance criteria, not aspirational goals.

## Conversation Principles

### Follow Energy

When the user gets excited about something, explore it deeper. When they're vague or disengaged, they may not care about that aspect — note it and move on.

### Challenge Vagueness

Don't accept "it should be good" or "make it intuitive." Always push for specifics:
- "Good compared to what?"
- "Intuitive for whom — a developer or a first-time user?"

### Make Abstract Concrete

Every abstract concept should become a specific scenario:
- Abstract: "The system should be fast"
- Concrete: "Search results appear in under 200ms"

### One Question at a Time

Never list multiple questions. Ask one, wait for the answer, then follow up based on what they said. This creates a natural conversation, not an interview.

### Know When to Stop

Stop questioning when:
- You have enough to write a clear PROJECT.md
- The user's energy is flagging
- You're getting repetitive answers
- The user says "that's enough" or "let's move on"

## Output

The questioning session produces raw material for the `project-setup` skill:
- Vision and purpose (from motivation questions)
- Concrete features and behaviors (from concreteness questions)
- Clarified terms and boundaries (from clarification questions)
- Success criteria (from success questions)
