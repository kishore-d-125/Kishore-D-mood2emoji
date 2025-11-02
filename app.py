"""
Kid-safe Text-Mood Detector (Mood2Emoji App)
A simple web application that detects mood from text input and returns appropriate emojis.
Designed for kids aged 12-16 with safety filters and educational features.
"""

import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(
    page_title="Mood2Emoji App",
    page_icon="😀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Bad words filter for kid safety
BAD_WORDS = []

# Sensitive topics that trigger neutral fallback
SENSITIVE_TOPICS = [
    'death', 'die', 'dying', 'dead', 'suicide', 'kill', 'violence',
    'harm', 'hurt', 'abuse', 'danger', 'dangerous', 'passed away',
    'passed on', 'lost someone', 'funeral', 'grave', 'buried'
]

# Sensitive phrases checked as whole phrases
SENSITIVE_PHRASES = [
    'passed away', 'passed on', 'lost my', 'lost a', 'funeral', 
    'taking my life', 'end my life', 'want to die'
]

def contains_bad_words(text):
    """
    Check if text contains inappropriate words.
    Returns True if bad words are detected, False otherwise.
    """
    text_lower = text.lower()
    for word in BAD_WORDS:
        if word.lower() in text_lower:
            return True
    return False

def contains_sensitive_topics(text):
    """
    Check if text contains sensitive or concerning topics.
    Returns True if sensitive topics are detected, False otherwise.
    """
    text_lower = text.lower()
    
    # Check for sensitive words
    for topic in SENSITIVE_TOPICS:
        if topic in text_lower:
            return True
    
    # Check for sensitive phrases (as whole phrases, not just words)
    for phrase in SENSITIVE_PHRASES:
        if phrase in text_lower:
            return True
    
    return False

def detect_mood(text):
    """
    Detects mood from text using TextBlob sentiment analysis.
    Returns: (mood_type, emoji, message)
    - mood_type: 'happy', 'neutral', 'sad', or 'unknown'
    - emoji: corresponding emoji character
    - message: kid-friendly one-line explanation
    """
    # Safety check: filter out bad words
    if contains_bad_words(text):
        return 'neutral', '😐', "Hmm, let's try a different message!"
    
    # Safety check: filter out sensitive topics
    if contains_sensitive_topics(text):
        return 'neutral', '😐', "Let's keep it positive and appropriate!"
    
    # Check for empty or very short input
    if not text or len(text.strip()) < 2:
        return 'neutral', '😐', "Please enter a sentence with more words!"
    
    try:
        # Use TextBlob for sentiment analysis
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        # Classify mood based on polarity score
        # Polarity ranges from -1 (very negative) to 1 (very positive)
        if polarity > 0.1:
            return 'happy', '😀', "Sounds happy!"
        elif polarity < -0.1:
            return 'sad', '😞', "Sounds a bit sad."
        else:
            return 'neutral', '😐', "Sounds neutral."
    
    except Exception as e:
        # Fallback to neutral for any errors
        return 'neutral', '😐', "Hmm, I'm not sure about this one. Try again!"

def explain_how_it_works():
    """
    Returns a simple explanation of how the app works.
    Used in Teacher Mode.
    """
    explanation = """
    ## How Mood2Emoji Works
    
    ### Step 1: Safety Check
    The app first checks if your text contains any inappropriate words.
    If found, it shows a neutral response for safety.
    
    ### Step 2: Sentiment Analysis
    The app uses **TextBlob**, a Python library that analyzes text sentiment.
    
    **How it works:**
    - TextBlob reads your sentence and assigns a **polarity score**
    - Polarity ranges from **-1** (very negative) to **+1** (very positive)
    - **0** means neutral
    
    ### Step 3: Mood Classification
    
    ```
    Polarity > 0.1  → Happy 😀
    Polarity = -0.1 to 0.1  → Neutral 😐
    Polarity < -0.1  → Sad 😞
    ```
    
    ### Example:
    - "I love ice cream!" → Polarity = +0.5 → Happy 😀
    - "It's okay." → Polarity = 0.0 → Neutral 😐
    - "I'm feeling down." → Polarity = -0.3 → Sad 😞
    
    ### Visual Flow:
    ```
    Your Text Input
         ↓
    [Safety Filter] → Bad words? → Neutral Response
         ↓
    [TextBlob Analysis] → Calculate Polarity Score
         ↓
    [Classification] → Happy/Neutral/Sad
         ↓
    [Display Result] → Emoji + Message
    ```
    
    ### Why This Matters:
    This is a simple example of **Natural Language Processing (NLP)**.
    Computers can understand human feelings from text!
    """
    return explanation

def main():
    """Main application function"""
    
    # Title and header
    st.title("😀 Mood2Emoji App")
    st.markdown("### Enter a sentence and discover its mood!")
    st.markdown("*A kid-safe text mood detector for ages 12-16*")
    
    # Teacher Mode toggle in sidebar
    st.sidebar.title("⚙️ Settings")
    teacher_mode = st.sidebar.checkbox("👨‍🏫 Teacher Mode", 
                                        help="Enable to see how the app works internally")
    
    # Display explanation if Teacher Mode is enabled
    if teacher_mode:
        st.sidebar.markdown("---")
        st.sidebar.markdown(explain_how_it_works())
    
    # Main content area
    st.markdown("---")
    
    # Text input box
    user_input = st.text_area(
        "📝 Enter your sentence here:",
        placeholder="Try: 'I'm excited about my birthday party!' or 'I feel tired today.'",
        height=100,
        help="Type any sentence and see what mood it has!"
    )
    
    # Analyze button
    if st.button("🔍 Detect Mood", type="primary"):
        if user_input:
            # Detect mood
            mood_type, emoji, message = detect_mood(user_input)
            
            # Display result in a prominent box
            st.markdown("---")
            st.markdown("### Result:")
            
            # Create columns for better layout
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.markdown(f"# {emoji}")
            
            with col2:
                st.markdown(f"### {message}")
                if teacher_mode:
                    try:
                        blob = TextBlob(user_input)
                        polarity = blob.sentiment.polarity
                        st.caption(f"*Polarity Score: {polarity:.2f} (Teacher Mode)*")
                    except Exception:
                        pass
            
            # Add some visual feedback
            if mood_type == 'happy':
                st.balloons()
                st.success("Positive mood detected! 🎉")
            elif mood_type == 'sad':
                st.info("Remember, it's okay to feel sad sometimes. 💙")
            else:
                st.info("Neutral mood detected.")
            
        else:
            st.warning("⚠️ Please enter a sentence first!")
    
    # Additional information section
    st.markdown("---")
    st.markdown("### 💡 Tips:")
    st.markdown("""
    - Try different sentences to see how moods change
    - Use words like "love", "happy", "excited" for happy moods
    - Use words like "sad", "tired", "upset" for sad moods
    - Keep your messages positive and appropriate!
    """)
    
    # Footer
    st.markdown("---")
    st.caption("Built with ❤️ for educational purposes | Ages 12-16")

if __name__ == "__main__":
    main()

