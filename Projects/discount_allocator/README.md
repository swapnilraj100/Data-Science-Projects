# Smart Discount Allocation Engine

## Overview

This engine fairly distributes a fixed discount kitty among sales agents based on data-driven metrics: performance, seniority, target achievement, and active clients.

## How It Works

Each attribute is normalized and weighted:
- Performance: 40%
- Seniority: 20%
- Target Achieved: 30%
- Active Clients: 10%

The weighted scores determine how much of the kitty each agent deserves. A justification is generated for transparency.

## Input

Provide a JSON file like `sample_input.json` with:
- `siteKitty`: total discount amount
- `salesAgents`: list with each agent’s metrics

## Output

A JSON output file `sample_output.json` showing:
- Agent ID
- Assigned discount
- Justification

## Run Instructions

```bash
python main.py
