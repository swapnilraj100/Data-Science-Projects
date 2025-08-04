import json

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0.0

def calculate_scores(sales_agents, weights):
    scores = []
    min_max = {
        key: (min(agent[key] for agent in sales_agents), max(agent[key] for agent in sales_agents))
        for key in ['performanceScore', 'seniorityMonths', 'targetAchievedPercent', 'activeClients']
    }

    for agent in sales_agents:
        score = 0
        components = []
        for key in weights:
            norm_val = normalize(agent[key], *min_max[key])
            contribution = norm_val * weights[key]
            score += contribution
            components.append((key, contribution))
        scores.append({"id": agent["id"], "score": score, "components": components})
    return scores

def allocate_discounts(site_kitty, sales_agents, config=None):
    weights = {
        "performanceScore": 0.4,
        "seniorityMonths": 0.2,
        "targetAchievedPercent": 0.3,
        "activeClients": 0.1
    }

    min_alloc = config.get("minPerAgent", 0) if config else 0
    max_alloc = config.get("maxPerAgent", site_kitty) if config else site_kitty

    scores = calculate_scores(sales_agents, weights)
    total_score = sum(agent['score'] for agent in scores)

    allocations = []
    remaining_kitty = site_kitty

    for agent in scores:
        if total_score == 0:
            assigned = site_kitty // len(scores)
        else:
            assigned = (agent['score'] / total_score) * site_kitty

        assigned = max(min_alloc, min(max_alloc, round(assigned)))
        remaining_kitty -= assigned
        justification = generate_justification(agent['components'])
        allocations.append({
            "id": agent["id"],
            "assignedDiscount": assigned,
            "justification": justification
        })

    # Adjust rounding issues
    diff = remaining_kitty
    if diff != 0:
        allocations[0]["assignedDiscount"] += diff  # adjust first agent

    return {"allocations": allocations}

def generate_justification(components):
    parts = []
    for feature, contrib in components:
        if contrib > 0.15:
            if feature == "performanceScore":
                parts.append("high performance")
            elif feature == "seniorityMonths":
                parts.append("long-term contribution")
            elif feature == "targetAchievedPercent":
                parts.append("strong target achievement")
            elif feature == "activeClients":
                parts.append("high client workload")
    return " and ".join(parts).capitalize() or "Standard allocation"
