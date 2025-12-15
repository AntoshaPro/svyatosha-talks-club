"""
Content Templates for Quantum Empire Builder
Pre-defined templates for various content formats
"""

# TikTok Script Templates
TIKTOK_TEMPLATES = {
    "problem_agitation_solution": {
        "title": "Problem Agitation Solution",
        "prompt_template": """
Create a TikTok script using the PAS (Problem-Agitation-Solution) formula:
1. Hook: Identify a relatable problem in {topic}
2. Agitation: Amplify the pain of this problem
3. Solution: Present how {topic} can resolve it
Make it under 60 seconds, conversational, and include a strong call to action.
""",
        "duration": "60 seconds",
        "tone": "Relatable, energetic, solution-focused"
    },
    "before_after_bridge": {
        "title": "Before After Bridge",
        "prompt_template": """
Create a transformation-focused TikTok script:
1. Before: Show the limiting state related to {topic}
2. After: Paint the vision of the transformed state
3. Bridge: Explain the key shift that creates the transformation
Make it engaging, visual, and include personal pronouns like 'you'.
""",
        "duration": "60 seconds",
        "tone": "Inspirational, transformational"
    },
    "storytelling_hook": {
        "title": "Storytelling Hook",
        "prompt_template": """
Create a TikTok script starting with a compelling story hook about {topic}:
1. Start with 'Let me tell you about the time when...'
2. Tell a brief, relatable story
3. Connect it to a universal truth about {topic}
4. End with a thought-provoking question for viewers
Keep it personal and relatable.
""",
        "duration": "60 seconds",
        "tone": "Personal, vulnerable, authentic"
    }
}

# Instagram Caption Templates
INSTAGRAM_CAPTION_TEMPLATES = {
    "hook_question": {
        "title": "Hook Question",
        "prompt_template": """
Write an Instagram caption about {topic} that starts with a compelling question:
1. Open with a thought-provoking question about {topic}
2. Provide value-packed content addressing the question
3. End with a clear call to action
4. Include 15-20 relevant hashtags
Make it scroll-stopping and valuable.
""",
        "tone": "Engaging, valuable, conversational"
    },
    "listicle": {
        "title": "Listicle Format",
        "prompt_template": """
Create an Instagram listicle caption about {topic}:
1. Start with 'X signs you're ready for [related to {topic}]'
2. Number each point clearly
3. Make each point actionable or insightful
4. End with a conclusion and call to action
Include emojis and line breaks for readability.
""",
        "tone": "Informative, structured, scannable"
    },
    "vulnerability_power": {
        "title": "Vulnerability Power",
        "prompt_template": """
Write an Instagram caption about {topic} using vulnerability:
1. Share a personal challenge related to {topic}
2. Describe the lesson learned
3. Offer hope or guidance to others
4. End with encouragement
Make it raw and real while still being uplifting.
""",
        "tone": "Authentic, vulnerable, empowering"
    }
}

# YouTube Hook Templates
YOUTUBE_HOOK_TEMPLATES = {
    "shocking_stat": {
        "title": "Shocking Statistic",
        "prompt_template": """
Create a YouTube hook about {topic} starting with a shocking statistic:
1. Lead with 'Did you know that [statistic about {topic}]?'
2. Briefly explain why this matters
3. Promise to reveal the solution in the video
4. Create curiosity gap
Keep it under 15 seconds and attention-grabbing.
""",
        "duration": "15 seconds",
        "tone": "Surprising, informative, curiosity-driven"
    },
    "controversial_take": {
        "title": "Controversial Take",
        "prompt_template": """
Create a YouTube hook about {topic} with a controversial take:
1. State an unpopular opinion about {topic}
2. Acknowledge it might be controversial
3. Promise to explain the reasoning
4. Invite discussion in comments
Make it bold but respectful.
""",
        "duration": "15 seconds",
        "tone": "Bold, thought-provoking, discussion-inviting"
    },
    "story_setup": {
        "title": "Story Setup",
        "prompt_template": """
Create a YouTube hook about {topic} using story setup:
1. Start with 'Three years ago, I discovered something about {topic}...'
2. Set up the intriguing discovery
3. Hint at the transformation that followed
4. Promise the full story in the video
Make it personal and mysterious.
""",
        "duration": "15 seconds",
        "tone": "Personal, mysterious, intriguing"
    }
}

# Twitter Thread Templates
TWITTER_THREAD_TEMPLATES = {
    "thread_by_thread": {
        "title": "Thread by Thread",
        "prompt_template": """
Create a Twitter thread about {topic} in 7 tweets:
1. Tweet 1: Compelling hook about {topic}
2. Tweets 2-6: Each tweet builds on the concept with practical tips
3. Tweet 7: Strong conclusion with call to action
Keep each tweet under 280 characters and include emojis.
""",
        "tweet_count": 7,
        "tone": "Conversational, valuable, actionable"
    },
    "common_mistakes": {
        "title": "Common Mistakes",
        "prompt_template": """
Create a Twitter thread about common mistakes in {topic}:
1. Tweet 1: Hook about the mistakes people make with {topic}
2. Tweets 2-6: Each tweet highlights one mistake with explanation
3. Tweet 7: How to avoid these mistakes
Format as an educational series.
""",
        "tweet_count": 7,
        "tone": "Educational, cautionary, helpful"
    }
}

# Blog Post Introduction Templates
BLOG_INTRO_TEMPLATES = {
    "anecdote_leading": {
        "title": "Anecdote Leading",
        "prompt_template": """
Write an engaging blog post introduction about {topic}:
1. Start with a personal anecdote related to {topic}
2. Connect the anecdote to a broader principle
3. Preview what the reader will learn
4. End with a smooth transition into the main content
Aim for 150-200 words.
""",
        "word_count": "150-200",
        "tone": "Personal, relatable, informative"
    },
    "statistic_stunning": {
        "title": "Stunning Statistic",
        "prompt_template": """
Create a blog intro about {topic} starting with a stunning statistic:
1. Lead with a surprising fact about {topic}
2. Explain the significance of this statistic
3. Pose a question that the article will answer
4. Preview the main points
Make it attention-grabbing and informative.
""",
        "word_count": "150-200",
        "tone": "Surprising, authoritative, informative"
    }
}

# Podcast Topic Templates
PODCAST_TOPIC_TEMPLATES = {
    "interview_style": {
        "title": "Interview Style",
        "prompt_template": """
Suggest a podcast episode about {topic} in interview format:
1. Title: Catchy title incorporating {topic}
2. Description: What will be discussed about {topic}
3. Questions: 5-7 thought-provoking questions
4. Value: What listeners will gain
Focus on transformation and practical insights.
""",
        "format": "Interview",
        "tone": "Insightful, conversational, valuable"
    },
    "solo_monologue": {
        "title": "Solo Monologue",
        "prompt_template": """
Create a solo podcast episode outline about {topic}:
1. Opening hook related to {topic}
2. Main content sections (3-4 segments)
3. Practical takeaway for listeners
4. Closing with call to action
Make it educational and inspiring.
""",
        "format": "Solo",
        "tone": "Educational, inspiring, actionable"
    }
}

# Newsletter Content Templates
NEWSLETTER_TEMPLATES = {
    "weekly_wisdom": {
        "title": "Weekly Wisdom",
        "prompt_template": """
Create a newsletter section about {topic} titled 'Weekly Wisdom':
1. Short reflection on {topic}
2. One key insight or practice
3. Quote related to {topic}
4. Personal note connecting to readers
Keep it warm and insightful.
""",
        "tone": "Warm, reflective, personal"
    },
    "tool_technique": {
        "title": "Tool & Technique",
        "prompt_template": """
Create a newsletter segment about {topic} focusing on practical tools:
1. Introduce a technique related to {topic}
2. Explain how it works
3. Provide step-by-step implementation
4. Encourage reader to try it
Make it actionable and clear.
""",
        "tone": "Practical, instructional, encouraging"
    }
}

# Video Idea Templates
VIDEO_IDEA_TEMPLATES = {
    "tutorial_style": {
        "title": "Tutorial Style",
        "prompt_template": """
Generate a video idea about {topic} in tutorial format:
1. Title: Clear and benefit-focused
2. Objective: What viewers will learn/create
3. Steps: 3-5 main steps to achieve the objective
4. Outcome: Transformation or result promised
Make it educational and achievable.
""",
        "format": "Tutorial",
        "tone": "Educational, step-by-step, achievement-focused"
    },
    "day_in_life": {
        "title": "Day in the Life",
        "prompt_template": """
Create a 'Day in the Life' video idea incorporating {topic}:
1. Time: Part of day to feature
2. Activities: How {topic} integrates into daily life
3. Challenges: Real obstacles faced
4. Solutions: How {topic} helps overcome challenges
Make it authentic and relatable.
""",
        "format": "Documentary/Lifestyle",
        "tone": "Authentic, relatable, inspirational"
    }
}

# AI Image Prompt Templates
AI_IMAGE_PROMPT_TEMPLATES = {
    "motivational_visual": {
        "title": "Motivational Visual",
        "prompt_template": """
Create an AI image prompt for a motivational visual about {topic}:
1. Scene: Visual representation of {topic}
2. Style: Artistic style (minimalist, vibrant, ethereal, etc.)
3. Colors: Color palette that evokes emotion
4. Elements: Symbolic elements representing transformation
Make it visually striking and emotionally resonant.
""",
        "style": "Motivational",
        "tone": "Uplifting, visually striking, symbolic"
    },
    "abstract_concept": {
        "title": "Abstract Concept",
        "prompt_template": """
Generate an abstract AI art prompt for {topic}:
1. Concept: Abstract representation of {topic}
2. Visual metaphors: Symbols representing {topic}
3. Composition: How elements relate to each other
4. Mood: Emotional feeling to convey
Create something artistic and conceptual.
""",
        "style": "Abstract",
        "tone": "Artistic, conceptual, symbolic"
    }
}

# All templates grouped by content type
CONTENT_TEMPLATES = {
    "TikTok Script": TIKTOK_TEMPLATES,
    "Instagram Caption": INSTAGRAM_CAPTION_TEMPLATES,
    "YouTube Hook": YOUTUBE_HOOK_TEMPLATES,
    "Twitter Thread": TWITTER_THREAD_TEMPLATES,
    "Blog Post Intro": BLOG_INTRO_TEMPLATES,
    "Podcast Topic": PODCAST_TOPIC_TEMPLATES,
    "Newsletter Content": NEWSLETTER_TEMPLATES,
    "Video Idea": VIDEO_IDEA_TEMPLATES,
    "AI Image Prompt": AI_IMAGE_PROMPT_TEMPLATES
}


def get_template(template_type: str, sub_type: str) -> dict:
    """
    Get a specific template by type and subtype
    """
    if template_type in CONTENT_TEMPLATES:
        if sub_type in CONTENT_TEMPLATES[template_type]:
            return CONTENT_TEMPLATES[template_type][sub_type]
    return None


def get_all_templates_for_type(template_type: str) -> dict:
    """
    Get all templates for a specific content type
    """
    return CONTENT_TEMPLATES.get(template_type, {})


def get_all_template_types() -> list:
    """
    Get all available template types
    """
    return list(CONTENT_TEMPLATES.keys())


def apply_template(template_type: str, sub_type: str, topic: str) -> str:
    """
    Apply a template to a specific topic
    """
    template = get_template(template_type, sub_type)
    if template:
        prompt_template = template['prompt_template']
        return prompt_template.format(topic=topic)
    return ""