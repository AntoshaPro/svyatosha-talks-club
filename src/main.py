#!/usr/bin/env python3
"""
SvyaTosha: Quantum Empire Builder
AI-powered command center for building and scaling digital empires of spiritual entrepreneurs
"""

import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime, timedelta

# Import our modules
from src.api.gemini_api import GeminiAPI
from src.utils.helpers import (
    calculate_growth_projection, 
    format_currency, 
    calculate_percentage_progress, 
    generate_timeline_dates,
    format_large_number,
    create_performance_dataframe,
    create_sentiment_dataframe,
    validate_social_media_url
)
from src.templates.content_templates import (
    CONTENT_TEMPLATES,
    apply_template,
    get_all_template_types
)

# Load environment variables
load_dotenv()

# Initialize API
gemini_api = GeminiAPI()

st.set_page_config(
    page_title="SvyaTosha: Quantum Empire Builder",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "empire"

# Sidebar
with st.sidebar:
    st.title("🔮 Quantum Empire Builder")
    st.markdown("---")
    
    # Navigation
    tab_options = [
        "🎯 Empire Dashboard",
        "⚡ Viral Workshop", 
        "💰 Money Flow",
        "🧠 Quantum Insights"
    ]
    
    selected_tab = st.radio("Navigate", tab_options)
    
    # Update session state based on selection
    if "Empire" in selected_tab:
        st.session_state.current_tab = "empire"
    elif "Viral" in selected_tab:
        st.session_state.current_tab = "viral"
    elif "Money" in selected_tab:
        st.session_state.current_tab = "money"
    elif "Insights" in selected_tab:
        st.session_state.current_tab = "insights"
    
    st.markdown("---")
    
    # User stats
    st.subheader("Your Current Empire Stats")
    st.metric(label="Subscribers", value="20", delta="+3 this week")
    st.metric(label="Paying Members", value="6", delta="+1 this week")
    st.metric(label="Revenue", value="$420", delta="+$80 this week")
    
    st.markdown("---")
    
    # Goals
    st.subheader("Your Big Dreams")
    st.progress(0.002, text="Towards 10M subs: **0.002%**")
    st.progress(0.0004, text="Towards $1B: **0.0004%**")

# Main content based on selected tab
if st.session_state.current_tab == "empire":
    st.title("🎯 Quantum Empire Dashboard")
    st.markdown("Your high-vibration command center for empire building")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Your Empire Goals")
        
        # Goal setting
        target_subscribers = st.number_input("Target Subscribers", min_value=1000, max_value=100000000, value=10000000, step=100000)
        target_revenue = st.number_input("Target Revenue ($)", min_value=1000, max_value=1000000000, value=1000000000, step=1000000)
        
        # Current status
        current_subscribers = st.number_input("Current Subscribers", min_value=0, value=20, step=1)
        current_revenue = st.number_input("Current Revenue ($)", min_value=0, value=420, step=10)
        
        # Calculate progress
        subscriber_progress = calculate_percentage_progress(current_subscribers, target_subscribers)
        revenue_progress = calculate_percentage_progress(current_revenue, target_revenue)
        
        st.markdown(f"**Subscriber Progress:** {subscriber_progress:.4f}%")
        st.progress(subscriber_progress / 100)
        
        st.markdown(f"**Revenue Progress:** {revenue_progress:.4f}%")
        st.progress(revenue_progress / 100)
    
    with col2:
        st.subheader("Quantum Timeline Projection")
        
        # Create a simple projection chart
        dates = generate_timeline_dates(12)
        projected_subs = calculate_growth_projection(current_subscribers, 1.5, 12)
        projected_revenue = calculate_growth_projection(current_revenue, 1.8, 12)
        
        df = pd.DataFrame({
            'Date': dates,
            'Projected Subscribers': projected_subs,
            'Projected Revenue': projected_revenue
        })
        
        # Display charts
        st.line_chart(df.set_index('Date')['Projected Subscribers'], height=200)
        st.line_chart(df.set_index('Date')['Projected Revenue'], height=200)
    
    st.markdown("---")
    
    # AI Oracle Section
    st.subheader("🔮 AI Oracle - Your Strategic Guide")
    
    oracle_mode = st.checkbox("Enable Deep Thinking Mode (More Powerful Analysis)")
    
    if st.button("Ask Oracle for Strategy"):
        with st.spinner("Oracle is contemplating your empire's next moves..."):
            current_stats = {
                "subscribers": current_subscribers,
                "revenue": current_revenue,
                "target_subscribers": target_subscribers,
                "target_revenue": target_revenue
            }
            
            response = gemini_api.generate_strategy_oracle(current_stats)
            st.success("Oracle's wisdom:")
            st.write(response)

elif st.session_state.current_tab == "viral":
    st.title("⚡ Viral Content Laboratory")
    st.markdown("Where quantum vibrations become viral masterpieces")
    
    # Step 0: Personality Calibration
    st.subheader("0. 🧬 Personality Calibration")
    social_links = st.text_area("Enter your social media links (one per line) to calibrate your digital DNA:", 
                                placeholder="https://tiktok.com/@your_account\nhttps://instagram.com/your_account\nhttps://youtube.com/c/yourchannel")
    
    if st.button("Calibrate Digital DNA"):
        with st.spinner("Analyzing your quantum signature..."):
            if social_links.strip():
                response = gemini_api.analyze_personality(social_links)
                st.session_state.personality_profile = response
                st.success("Digital DNA calibrated!")
                st.write(response)
            else:
                st.warning("Please enter your social media links first")
    
    # Step 0.5: Empathetic Resonance
    st.subheader("0.5 💖 Empathetic Resonance")
    audience_topic = st.selectbox("Select audience topic to analyze:", 
                                  ["Anxiety & Stress", "Manifestation Blocks", "Spiritual Awakening", 
                                   "Financial Abundance", "Relationship Issues", "Personal Growth", "Other"])
    other_topic = None
    if audience_topic == "Other":
        other_topic = st.text_input("Specify your own topic:")
    
    topic_to_analyze = other_topic if other_topic else audience_topic
    
    if st.button("Analyze Audience Resonance"):
        with st.spinner("Connecting with your audience's soul..."):
            response = gemini_api.analyze_audience_resonance(topic_to_analyze)
            st.success("Resonance analysis complete!")
            st.write(response)
    
    # Step 1: Trend Scanner
    st.subheader("1. 🔍 Trend Scanner & Spy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        niche = st.selectbox("Select your niche:", 
                            ["Spirituality", "Manifestation", "Yoga", "NLP", "Personal Development", 
                             "Mindfulness", "Consciousness", "Quantum Reality", "Self-Help"])
        
        if st.button("Scan Current Trends"):
            with st.spinner("Scanning the noosphere for trending topics..."):
                response = gemini_api.scan_trends(niche)
                st.success("Trend scan complete!")
                st.write(response)
    
    with col2:
        competitor_urls = st.text_area("Competitor URLs (optional, for analysis):", 
                                      placeholder="Paste competitor social media links here...")
        
        if st.button("Spy on Competitors"):
            with st.spinner("Gathering competitive intelligence..."):
                if competitor_urls.strip():
                    response = gemini_api.analyze_competitors(competitor_urls, niche)
                    st.success("Competitive analysis complete!")
                    st.write(response)
                else:
                    st.warning("Please enter competitor URLs first")
    
    # Step 1.5: Neuro-Scout
    st.subheader("1.5 🤖 Neuro-Scout (Free AI Tools)")
    
    if st.button("Find Free AI Video Generation Tools"):
        with st.spinner("Scouting the internet for free AI tools..."):
            response = gemini_api.find_ai_tools()
            st.success("Neuro-scout mission complete!")
            st.write(response)
    
    # Step 2: Masterpiece Generation
    st.subheader("2. 🎨 Masterpiece Generator")
    
    content_format = st.selectbox("Choose content format:", 
                                 ["TikTok Script", "Instagram Caption", "YouTube Hook", 
                                  "Twitter Thread", "Blog Post Intro", "Podcast Topic", 
                                  "Newsletter Content", "Video Idea", "AI Image Prompt", "Other"])
    
    content_topic = st.text_input("Content topic or idea:", 
                                 placeholder="E.g., How to release trapped energy, Quantum manifestation techniques...")
    
    custom_prompt = st.text_area("Custom instructions for the content (optional):", 
                                placeholder="E.g., Make it funny, use emojis, keep it under 60 seconds, etc.")
    
    generate_btn = st.button("Materialize Content Masterpiece")
    
    if generate_btn:
        with st.spinner("Creating your viral masterpiece..."):
            if not content_topic:
                st.warning("Please enter a content topic")
            else:
                response = gemini_api.generate_viral_content(
                    content_topic, 
                    content_format, 
                    custom_prompt,
                    st.session_state.get('personality_profile', 'Not calibrated yet')
                )
                
                st.success("Masterpiece materialized! ✨")
                
                # Display the generated content with special formatting based on type
                if content_format == "TikTok Script":
                    st.subheader("🎬 TikTok Script:")
                    st.code(response, language="text")
                elif content_format == "Instagram Caption":
                    st.subheader("📱 Instagram Caption:")
                    st.write(response)
                    # Also suggest hashtags
                    from src.utils.helpers import extract_hashtags
                    hashtags = extract_hashtags(response)
                    st.subheader("🏷️ Suggested Hashtags:")
                    st.write(" ".join(hashtags[:15]))  # Show first 15 hashtags
                elif content_format == "AI Image Prompt":
                    st.subheader("🖼️ AI Image Prompt:")
                    st.write(response)
                else:
                    st.write(response)

elif st.session_state.current_tab == "money":
    st.title("💰 Money Flow - Mindset Transformation Lab")
    st.markdown("Dissolve financial blocks and activate abundance consciousness")
    
    st.subheader(" diagnose your financial blocks:")
    financial_block = st.text_area("Describe your money situation, fear, or limitation:", 
                                  placeholder="E.g., I'm afraid to raise my prices, I feel guilty charging for spiritual work, I struggle with abundance mindset...",
                                  height=100)
    
    if st.button("Dissolve Block & Transform"):
        if financial_block.strip():
            with st.spinner("Processing your financial transformation..."):
                response = gemini_api.transform_financial_block(financial_block)
                st.success("Block dissolved! New reality activated! 🌟")
                st.write(response)
        else:
            st.warning("Please describe your financial block first")
    
    st.markdown("---")
    
    # Predefined common blocks
    st.subheader("Common Financial Blocks & Solutions")
    
    common_blocks = [
        "Fear of raising prices",
        "Guilt about charging for spiritual work", 
        "Belief that money is evil",
        "Worthiness issues around wealth",
        "Scarcity mindset",
        "Procrastination on launches",
        "Undervaluing services"
    ]
    
    selected_block = st.selectbox("Or select a common block to address:", common_blocks)
    
    if st.button("Transform Selected Block"):
        with st.spinner("Working on the transformation..."):
            prompt = f"""
            Address this common financial block for a spiritual entrepreneur: '{selected_block}'
            
            Provide:
            1. The root cause of this block
            2. A powerful reframing perspective
            3. An actionable 'Universe Assignment' 
            4. Affirmations to reinforce the new belief
            """
            
            response = gemini_api.generate_content(prompt)
            st.success(f"Transformation for '{selected_block}' complete!")
            st.write(response)

elif st.session_state.current_tab == "insights":
    st.title("🧠 Quantum Insights Dashboard")
    st.markdown("Deep analytics and strategic insights for your empire")
    
    st.subheader("Content Performance Analytics")
    
    # Simulated content performance data
    content_types = ['TikTok', 'Instagram', 'YouTube', 'Telegram', 'Newsletter']
    engagement_rates = [8.5, 4.2, 6.1, 12.3, 3.7]  # Simulated engagement rates
    
    perf_data = create_performance_dataframe(content_types, engagement_rates)
    
    st.bar_chart(perf_data.set_index('Platform'), height=300)
    
    st.subheader("Audience Sentiment Analysis")
    
    sentiment_options = ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative"]
    sentiment_distribution = [35, 40, 15, 7, 3]  # Percentages
    
    sent_df = create_sentiment_dataframe(sentiment_options, sentiment_distribution)
    
    st.bar_chart(sent_df.set_index('Sentiment'), height=300)
    
    st.subheader("Quantum Opportunity Scanner")
    
    if st.button("Scan for Opportunities"):
        with st.spinner("Scanning quantum field for opportunities..."):
            response = gemini_api.scan_opportunities()
            st.success("Opportunity scan complete!")
            st.write(response)

# Footer
st.markdown("---")
st.markdown("*SvyaTosha: Quantum Empire Builder - Building your spiritual business empire with AI-powered magic* ✨")