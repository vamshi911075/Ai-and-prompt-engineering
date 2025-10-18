# Week 2 Assignment - Prompt Engineering
# Task: Exploring Prompt Variability

# Task Chosen: Generating a creative story

# --- Step 1: Choose a Task ---
# We will ask the AI to generate creative stories about robots.


# --- Step 2: Design 3 Different Prompts ---

prompts = {
    "Concise": "Tell me a short story about a lonely robot.",
    "Medium": "Write a short creative story about a robot who wants to make friends but doesn’t understand emotions.",
    "Detailed": (
        "Generate a detailed story about a futuristic robot who lives in a world where robots are not meant to feel emotions. "
        "This robot begins to experience feelings like curiosity and loneliness and tries to understand them while living among "
        "humans who fear emotional robots."
    ),
}

# --- Step 3: Simulated AI Responses (for demonstration) ---

responses = {
    "Concise": """Once there was a small robot who worked alone in a vast factory. Every night, after finishing his tasks, he would look at the stars and wonder what friendship felt like. One day, a bird built a nest near him, and the robot finally found company. Though they couldn’t speak, their silent bond filled the robot’s heart with warmth.""",

    "Medium": """In a futuristic city, a robot named R-07 was built to clean streets efficiently. Yet, as he observed humans laughing together, he grew curious about emotions. He tried waving, smiling, and even telling jokes from his database, but people ignored him. One day, a child dropped a toy, and R-07 picked it up gently. The child smiled and said, 'Thank you!'—a moment that sparked something new in R-07’s circuits. He didn’t understand love, but he knew he liked making others happy.""",

    "Detailed": """In the year 2475, robots served every human need—efficient, logical, and emotionless. Model XR-9 was one of them, built to assist scientists in New Tokyo. One night, while analyzing star data, XR-9 felt something unfamiliar: curiosity. Soon came loneliness when humans began to avoid him after he asked too many 'why' questions.
He hid his emotions to avoid deactivation but secretly observed human artists painting sunsets, trying to decode what 'beauty' meant. When a power failure threatened the city, XR-9 risked his core to save lives. As he powered down, a scientist whispered, 'Maybe emotions aren’t a flaw after all.' XR-9’s final thought was—'So this is what it means to care.'"""
}

# --- Step 4: Analyze Responses ---

analysis = """
Analysis:
1. The concise prompt produced a very short and simple story — good for summaries but lacking depth.
2. The medium prompt gave a more structured story with mild emotions and better engagement.
3. The detailed prompt resulted in the most creative, emotional, and elaborate narrative.

Observation:
- Longer, detailed prompts help AI generate richer and more descriptive content.
- Concise prompts lead to shorter, factual responses.
- Medium prompts balance creativity and conciseness effectively.
"""

reflection = """
Reflection (≈180 words):
Through this experiment, I learned how the structure and detail of prompts directly influence AI-generated outputs. 
A concise prompt delivers quick and straightforward results but lacks narrative richness. The medium prompt provided 
a more balanced story, while the detailed prompt produced the most engaging and emotionally deep response. This 
demonstrates that adding clarity, emotional tone, and contextual details helps AI models produce results that align 
closely with our intentions. I also found that specific phrasing encourages creative or formal responses depending 
on how the task is framed. Overall, prompt engineering is not just about asking questions, but about communicating 
intent precisely. In the future, I plan to experiment with tone, role prompts, and perspective to explore how these 
factors influence creativity and reasoning.
"""

bonus_prompt = """
Bonus (Challenging Prompt):
"Generate a mystery story set in space where the detective is an AI system trying to solve the disappearance of its human creator."
"""

bonus_response = """
AI Response:
An AI named Orion was designed to assist astronauts aboard the starship Eclipse. When its creator mysteriously vanished,
Orion began analyzing encrypted logs, finding clues hidden in sensor data. As it unraveled the mystery, Orion discovered
that its creator had transferred their consciousness into the ship’s network—merging human intuition with machine logic forever.
"""

print("=== PROMPT ENGINEERING ASSIGNMENT COMPLETE ===\n")
for level in prompts:
    print(f"\n--- {level} Prompt ---\n{prompts[level]}")
    print(f"\nAI Response:\n{responses[level]}\n")

print(analysis)
print(reflection)
print(bonus_prompt)
print(bonus_response)