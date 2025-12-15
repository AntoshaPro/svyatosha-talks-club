"""
Gemini API Integration Module for Quantum Empire Builder
Handles all interactions with Google's Gemini AI
"""

import google.generativeai as genai
import os
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class GeminiAPI:
    def __init__(self):
        """Initialize the Gemini API client"""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            self.chat_model = genai.GenerativeModel('gemini-pro')
        else:
            logger.warning("GOOGLE_API_KEY not found in environment variables")
    
    def generate_content(self, prompt: str, use_advanced_model: bool = False) -> Optional[str]:
        """Generate content using Gemini API"""
        try:
            if not self.api_key:
                return "Error: GOOGLE_API_KEY not configured"
            
            # Use different models based on requirements
            if use_advanced_model:
                model = genai.GenerativeModel('gemini-1.5-pro-latest')
            else:
                model = self.model
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Error generating content: {str(e)}")
            return f"Error generating content: {str(e)}"
    
    def start_chat(self):
        """Start a new chat session"""
        try:
            if not self.api_key:
                return None
            return self.chat_model.start_chat()
        except Exception as e:
            logger.error(f"Error starting chat: {str(e)}")
            return None
    
    def analyze_personality(self, social_media_links: str) -> Optional[str]:
        """Analyze personality from social media links"""
        prompt = f"""
        Analyze these social media profiles to understand the personality, communication style, and core message of this spiritual influencer:
        
        {social_media_links}
        
        Identify:
        1. Core archetypes and themes
        2. Unique communication style and voice
        3. Key phrases and terminology
        4. Strengths and resonant topics
        5. Target audience profile
        
        Format as a detailed personality profile for content creation purposes.
        """
        
        return self.generate_content(prompt)
    
    def analyze_audience_resonance(self, topic: str) -> Optional[str]:
        """Analyze audience resonance for a specific topic"""
        prompt = f"""
        As a spiritual mentor and content creator, deeply analyze the psychological and emotional needs of people interested in '{topic}'.
        
        Provide:
        1. Core pain points and frustrations
        2. Hidden desires and aspirations
        3. Common fears and resistance patterns
        4. Emotional triggers that resonate
        5. Content ideas that would deeply connect
        
        Be empathetic and insightful.
        """
        
        return self.generate_content(prompt)
    
    def scan_trends(self, niche: str) -> Optional[str]:
        """Scan for current trends in a specific niche"""
        prompt = f"""
        Find the top 10 trending topics, hashtags, and viral content themes in the '{niche}' space right now.
        Include both general trends and specific examples of successful content.
        Focus on what's getting high engagement and why.
        """
        
        return self.generate_content(prompt)
    
    def analyze_competitors(self, competitor_urls: str, niche: str) -> Optional[str]:
        """Analyze competitors in a specific niche"""
        prompt = f"""
        Analyze these competitor profiles in the '{niche}' space:
        
        {competitor_urls}
        
        Provide a comprehensive report including:
        1. Their content strategy and themes
        2. Top-performing content types
        3. Engagement rates and patterns
        4. Strengths and weaknesses
        5. Opportunities for differentiation
        6. Specific viral content examples
        """
        
        return self.generate_content(prompt)
    
    def find_ai_tools(self) -> Optional[str]:
        """Find free AI tools for content creation"""
        prompt = """
        Find and list free AI tools for:
        1. Video generation (like RunwayML, Synthesia, Pictory)
        2. Image generation (like Midjourney, DALL-E, Stable Diffusion)
        3. Audio generation (for voiceovers, music)
        4. Text content enhancement
        
        Include links and brief descriptions of each tool.
        """
        
        return self.generate_content(prompt)
    
    def generate_viral_content(self, topic: str, format_type: str, custom_instructions: str = "", personality_profile: str = "") -> Optional[str]:
        """Generate viral content based on specifications"""
        prompt = f"""
        Create high-vibration viral content based on:
        
        Topic: {topic}
        Format: {format_type}
        
        Additional instructions: {custom_instructions}
        
        If available, use the personality profile: {personality_profile}
        
        Make it engaging, shareable, and aligned with spiritual business principles.
        """
        
        return self.generate_content(prompt)
    
    def transform_financial_block(self, financial_block: str) -> Optional[str]:
        """Help transform financial blocks using NLP techniques"""
        prompt = f"""
        You are an advanced NLP and coaching specialist helping a spiritual entrepreneur overcome financial blocks.
        
        Client's issue: {financial_block}
        
        Apply advanced NLP techniques, cognitive reframing, and spiritual business principles to:
        1. Identify the root belief causing this block
        2. Provide a transformative insight that reframes the situation
        3. Offer a specific 'Universe Assignment' - a concrete action to shift this pattern
        4. Give an empowering new perspective on money and service
        
        Make it profound yet practical.
        """
        
        return self.generate_content(prompt)
    
    def generate_strategy_oracle(self, current_stats: Dict[str, Any]) -> Optional[str]:
        """Generate strategic advice from the AI Oracle"""
        prompt = f"""
        You are an AI Oracle for a spiritual entrepreneur named SvyaTosha who runs 'SvyaTosha Talks Club'.
        Current stats: {current_stats}
        
        Provide a strategic plan with specific, actionable steps to grow their empire. Focus on:
        1. Content strategy for viral growth
        2. Monetization opportunities
        3. Scaling tactics
        4. Overcoming current limitations
        
        Make it inspiring and practical, using spiritual business terminology.
        """
        
        return self.generate_content(prompt)
    
    def scan_opportunities(self) -> Optional[str]:
        """Scan for new opportunities in the spiritual business space"""
        prompt = """
        Based on the profile of a spiritual entrepreneur running 'SvyaTosha Talks Club' with focus on quantum manifestation,
        enlightenment, and spirituality, identify 5 high-potential opportunities for:
        1. New content formats
        2. Revenue streams
        3. Platform expansion
        4. Collaboration possibilities
        5. Product/service development
        
        Make them innovative and aligned with spiritual business principles.
        """
        
        return self.generate_content(prompt)