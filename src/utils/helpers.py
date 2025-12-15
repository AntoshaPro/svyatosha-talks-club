"""
Helper utilities for Quantum Empire Builder
"""

import re
from typing import List, Dict, Any
import pandas as pd
from datetime import datetime, timedelta


def extract_hashtags(text: str, count: int = 15) -> List[str]:
    """
    Extract relevant hashtags from content
    """
    # Simple hashtag extraction - in a real app, this would be more sophisticated
    words = text.split()
    potential_tags = []
    
    for word in words:
        # Remove punctuation and convert to lowercase for analysis
        clean_word = re.sub(r'[^\w\s]', '', word.lower())
        if len(clean_word) > 3:  # Only consider words longer than 3 chars
            potential_tags.append(clean_word)
    
    # Return top 'count' unique tags
    unique_tags = list(set(potential_tags))
    return ['#' + tag.replace(' ', '') for tag in unique_tags[:count]]


def calculate_growth_projection(current_value: float, growth_rate: float, periods: int = 12) -> List[float]:
    """
    Calculate growth projection over time
    """
    projections = []
    current = current_value
    
    for _ in range(periods):
        projections.append(current)
        current *= growth_rate
    
    return projections


def validate_url(url: str) -> bool:
    """
    Validate if URL is a valid web URL (for open source research)
    """
    # Basic URL validation pattern
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain
        r'(?:/[^\s]*)?$'  # optional path
    )
    return bool(url_pattern.match(url))


def parse_niche_keywords(niche: str) -> List[str]:
    """
    Parse keywords associated with a niche
    """
    niche_keywords = {
        "spirituality": ["spiritual", "enlightenment", "consciousness", "awakening", "higher self"],
        "manifestation": ["manifest", "quantum", "vibration", "energy", "intention"],
        "yoga": ["yoga", "meditation", "mindfulness", "chakra", "balance"],
        "nlp": ["nlp", "neurolinguistic", "programming", "reframing", "language"],
        "personal development": ["growth", "self-improvement", "development", "potential", "transformation"],
        "mindfulness": ["mindful", "present", "awareness", "acceptance", "peace"],
        "consciousness": ["consciousness", "awareness", "truth", "reality", "perception"],
        "quantum reality": ["quantum", "reality", "parallel", "multiverse", "consciousness"],
        "self-help": ["help", "improve", "change", "overcome", "achieve"]
    }
    
    return niche_keywords.get(niche.lower(), [])


def format_currency(amount: float) -> str:
    """
    Format currency in a readable way
    """
    if amount >= 1_000_000_000:
        return f"${amount / 1_000_000_000:.1f}B"
    elif amount >= 1_000_000:
        return f"${amount / 1_000_000:.1f}M"
    elif amount >= 1_000:
        return f"${amount / 1_000:.1f}K"
    else:
        return f"${amount}"


def calculate_percentage_progress(current: float, target: float) -> float:
    """
    Calculate percentage progress toward a goal
    """
    if target <= 0:
        return 0.0
    return min((current / target) * 100, 100.0)


def generate_timeline_dates(months: int = 12) -> List[str]:
    """
    Generate timeline dates for projections
    """
    dates = []
    for i in range(months):
        future_date = datetime.now() + timedelta(days=30*i)
        dates.append(future_date.strftime("%b %Y"))
    return dates


def format_large_number(num: float) -> str:
    """
    Format large numbers in a readable way
    """
    if num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.2f}K"
    else:
        return str(num)


def create_performance_dataframe(content_types: List[str], engagement_rates: List[float]) -> pd.DataFrame:
    """
    Create a dataframe for content performance analytics
    """
    return pd.DataFrame({
        'Platform': content_types,
        'Engagement Rate (%)': engagement_rates
    })


def create_sentiment_dataframe(sentiment_labels: List[str], percentages: List[float]) -> pd.DataFrame:
    """
    Create a dataframe for sentiment analysis
    """
    return pd.DataFrame({
        'Sentiment': sentiment_labels,
        'Percentage': percentages
    })


def clean_text_for_analysis(text: str) -> str:
    """
    Clean text for better analysis
    """
    # Remove extra whitespace
    cleaned = ' '.join(text.split())
    # Remove URLs temporarily for analysis
    cleaned = re.sub(r'http\S+', '', cleaned)
    # Remove special characters but keep basic punctuation
    cleaned = re.sub(r'[^\w\s\.\,\!\?]', ' ', cleaned)
    return cleaned.strip()


def estimate_content_performance_score(content: str, niche: str) -> float:
    """
    Estimate potential performance score for content
    """
    # This is a simplified scoring algorithm
    # In a real app, this would use more sophisticated NLP and ML models
    
    score = 50.0  # Base score
    
    # Boost for emotional triggers
    emotional_triggers = [
        "feel", "love", "happy", "free", "abundant", "manifest", 
        "transform", "breakthrough", "power", "energy", "vibration"
    ]
    
    content_lower = content.lower()
    for trigger in emotional_triggers:
        if trigger in content_lower:
            score += 5.0
    
    # Boost for niche-specific terms
    niche_terms = parse_niche_keywords(niche)
    for term in niche_terms:
        if term in content_lower:
            score += 3.0
    
    # Adjust for content length (optimal length varies by platform)
    if 100 <= len(content) <= 300:
        score += 10.0
    elif len(content) > 500:
        score -= 5.0  # Too long might reduce engagement
    
    # Cap the score between 0 and 100
    return min(max(score, 0), 100)