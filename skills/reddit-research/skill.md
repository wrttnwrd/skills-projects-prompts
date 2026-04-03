---
name: reddit-research
description: Research questions people ask about a topic on Reddit. Discovers relevant subreddits automatically, extracts question-format posts, clusters by theme, and outputs a structured report for content planning and prompt modeling. Use when asked to research audience questions, find content gaps, or plan content based on what people actually ask.
command: /reddit-research
allowed-tools: Bash, Read, Write
argument-hint: <topic>
---

# Reddit Question Research

Research what people are actually asking about a topic on Reddit, without requiring any API credentials or knowing subreddits in advance.

## When Invoked

Run this when the user wants to:
- Understand what questions their audience asks about a topic
- Find content gaps and pillar content opportunities
- Model prompts based on real audience language
- Plan FAQ sections or content calendars

## Steps

1. **Get the topic** from $ARGUMENTS. If none provided, ask the user for a topic before proceeding.

2. **Run the research script:**
   ```bash
   python3 ~/.claude/skills/reddit-research/reddit_research.py "$ARGUMENTS" --output reddit_research.md
   ```
   If the script isn't found at that path, check the current directory:
   ```bash
   python3 reddit_research.py "$ARGUMENTS" --output reddit_research.md
   ```

3. **Read the output file** and present a summary to the user:
   - How many subreddits were searched
   - How many questions were found
   - The top 3 themes by volume
   - The top 5 questions by engagement

4. **Offer next steps:**
   - "Want me to turn these into content briefs?"
   - "Should I draft prompt templates from the top questions?"
   - "Want to run this for a related topic to compare?"

## Output Format

Always show the user:
- A brief summary (not the full report — that's in the .md file)
- The full path to the output file
- 3-5 of the most interesting/high-engagement questions as a preview

## Notes

- No Reddit API credentials required — uses public JSON endpoints
- Respects Reddit's rate limits with built-in delays
- Works best for topics with active Reddit communities
- Run time is typically 15-30 seconds depending on topic breadth
- Output file is ready to use as a content planning brief or paste into other workflows