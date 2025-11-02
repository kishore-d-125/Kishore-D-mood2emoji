# Mood2Emoji App
## Kid-safe Text-Mood Detector

A simple, educational web application that detects mood from text input and returns appropriate emojis. Designed specifically for children aged 12-16 as a learning tool for understanding text sentiment analysis and natural language processing concepts.

---

## 📋 Table of Contents

- [What is Mood2Emoji?](#what-is-mood2emoji)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Teaching Approach](#teaching-approach)
- [How to Teach This Project in 60 Minutes](#how-to-teach-this-project-in-60-minutes)
- [Known Limitations](#known-limitations)
- [Technical Details](#technical-details)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## 🎯 What is Mood2Emoji?

Mood2Emoji is an interactive web application that analyzes short sentences entered by users and determines their emotional mood. The app returns:
- A kid-safe emoji representing the detected mood (happy 😀, neutral 😐, or sad 😞)
- A concise, child-friendly one-line explanation
- Safety filters to protect children from inappropriate content

This project serves as an educational tool to introduce students to:
- Basic concepts of sentiment analysis
- Natural Language Processing (NLP)
- Text classification
- Programming and web application development

---

## ✨ Features

### Core Functionality
- **Text Input**: Simple text area for users to enter sentences
- **Mood Detection**: Analyzes text using TextBlob sentiment analysis
- **Visual Output**: Displays appropriate emoji (😀, 😐, 😞) based on detected mood
- **Kid-Friendly Messages**: Provides age-appropriate explanations
- **Safety Filters**: Detects and blocks inappropriate words, showing neutral fallback

### Educational Features
- **Teacher Mode**: Toggle to display internal workings of the app
- **Visual Explanations**: Shows how sentiment analysis works with diagrams and examples
- **Polarity Scores**: Displays sentiment scores in Teacher Mode for educational purposes

### Safety Features
- Bad word filtering
- Neutral fallback for unrecognized or inappropriate input
- Empty input handling
- Error handling for edge cases

---

## 🚀 Setup and Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Internet connection (for initial package installation)

### Step-by-Step Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/your-username/firstname-lastname-mood2emoji.git
   cd firstname-lastname-mood2emoji
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   This will install:
   - `streamlit`: Web application framework
   - `textblob`: Text processing and sentiment analysis library

---

## 🏃 How to Run

1. **Activate your virtual environment** (if using one)

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

4. **Start using the app!**
   - Enter a sentence in the text box
   - Click "Detect Mood" to see the result
   - Enable "Teacher Mode" in the sidebar to see how it works

---

## 🔧 How It Works

### Technical Overview

Mood2Emoji uses **TextBlob**, a Python library that performs sentiment analysis on text. Here's the process:

1. **Input Reception**: User enters text via the Streamlit interface

2. **Safety Check**: The app checks for inappropriate words
   - If detected → Returns neutral emoji with a safe message

3. **Sentiment Analysis**: TextBlob analyzes the text and calculates a **polarity score**
   - Polarity ranges from **-1** (very negative) to **+1** (very positive)
   - **0** indicates neutral sentiment

4. **Mood Classification**:
   - **Polarity > 0.1** → Happy 😀
   - **Polarity between -0.1 and 0.1** → Neutral 😐
   - **Polarity < -0.1** → Sad 😞

5. **Output Display**: Shows emoji and kid-friendly message

### Example Analysis

| Input Text | Polarity Score | Detected Mood | Output |
|------------|----------------|---------------|--------|
| "I love ice cream!" | +0.5 | Happy | 😀 "Sounds happy!" |
| "It's okay." | 0.0 | Neutral | 😐 "Sounds neutral." |
| "I'm feeling down." | -0.3 | Sad | 😞 "Sounds a bit sad." |

---

## 🎓 Teaching Approach

### Learning Objectives for Students (Ages 12-16)

By the end of working with this project, students should understand:
1. **Basic Sentiment Analysis**: What it means to analyze feelings in text
2. **Text Classification**: How computers can categorize text into groups
3. **Natural Language Processing (NLP)**: Introduction to how computers understand human language
4. **Programming Concepts**: Basic understanding of inputs, processing, and outputs
5. **Safety in Technology**: Importance of content filtering and safe online behavior

### Age-Appropriate Explanations

**For 12-14 year olds:**
- Focus on the interactive nature and emoji outputs
- Simple analogies: "The app is like a friend who reads your message and understands how you feel"
- Emphasize creativity and experimentation

**For 15-16 year olds:**
- Introduce technical concepts: polarity scores, algorithms
- Discuss real-world applications: social media sentiment, customer reviews
- Explore limitations and improvements

---

## 📚 How to Teach This Project in 60 Minutes

### Session Breakdown

#### **Introduction (10 minutes)**
- **Icebreaker**: Ask students to describe how they feel today using emojis
- **Introduce the app**: Show a live demonstration
- **Key Question**: "How do you think a computer can understand feelings in text?"

**Activities:**
- Quick demo: Enter "I'm excited about the weekend!" and show the happy emoji result
- Discuss: What makes text happy or sad?

#### **Basic Concepts (10 minutes)**
- **Sentiment Analysis Explained**: Use simple language
  - "Computers can read text and figure out if it sounds happy, sad, or neutral"
  - "They do this by looking at words and their meanings"
- **Show Teacher Mode**: Toggle on and explain the polarity score
- **Visual Aid**: Draw a number line from -1 to +1 showing mood ranges

**Activities:**
- Interactive quiz: "Is this happy or sad?" with example sentences
- Polarity score guessing game

#### **App Walkthrough (15 minutes)**
- **Navigate the Interface**: Show all features
  - Text input box
  - Detect Mood button
  - Results display
  - Teacher Mode explanation
- **Demonstrate Examples**:
  - Happy: "I love my new bike!"
  - Neutral: "Today is Monday."
  - Sad: "I'm worried about the test."
- **Safety Discussion**: Why we filter bad words and show neutral responses

**Activities:**
- Students predict outputs before clicking "Detect Mood"
- Compare predictions with actual results

#### **Hands-On Practice (20 minutes)**
- **Activity 1**: Students write and test their own sentences
  - Goal: Create one happy, one neutral, one sad sentence
  - Share results with the class
- **Activity 2**: Mood Prediction Game
  - Teacher provides sentences, students predict the mood
  - Discuss why certain words affect mood detection
- **Activity 3**: Teacher Mode Exploration
  - Students toggle Teacher Mode and read explanations
  - Discuss polarity scores for different sentences

**Activities:**
- Sentence creation challenge
- Mood prediction competition
- Polarity score investigation

#### **Recap and Q&A (5 minutes)**
- **Review Key Concepts**:
  - What is sentiment analysis?
  - How does the app work?
  - Why is safety important?
- **Real-World Connections**:
  - "Where have you seen computers understand text?"
  - "How could this be used in real apps?"
- **Questions and Discussion**
- **Next Steps**: Encourage students to experiment at home

### Materials Needed
- Computer with Python and Streamlit installed (or access to deployed app)
- Projector or screen for demonstration
- Whiteboard or flip chart for visual explanations
- Student worksheets (optional): Sentence examples, prediction charts

### Assessment Ideas
- **Quick Check**: Can students explain what sentiment analysis is?
- **Practical**: Students correctly predict moods for 3-5 sentences
- **Reflection**: Students write 2-3 sentences about what they learned

---

## ⚠️ Known Limitations

### Technical Limitations

1. **Simple Sentiment Analysis**
   - TextBlob uses basic sentiment analysis, not advanced machine learning
   - May misinterpret sarcasm, irony, or complex emotions
   - Works best with clear, straightforward sentences

2. **Language Support**
   - Primarily designed for English text
   - May not work accurately with other languages or mixed languages

3. **Context Understanding**
   - Lacks deep context understanding
   - Example: "Not bad" might be interpreted as negative, though it's often positive

4. **Bad Word Filter**
   - Uses a basic word list
   - May not catch all inappropriate content
   - Should be expanded for production use

5. **Short Text Bias**
   - Works better with complete sentences
   - Very short inputs (1-2 words) may give less accurate results

### Educational Limitations

1. **Simplified Explanation**
   - Teacher Mode explanation is intentionally simplified
   - Does not cover advanced NLP concepts like neural networks or deep learning

2. **Limited Customization**
   - Cannot easily modify mood thresholds or add new moods
   - Would require code changes for customization

### Recommendations for Improvement

- **Enhanced Safety**: Implement a more comprehensive profanity filter
- **Multilingual Support**: Add support for other languages
- **Custom Moods**: Allow students to define their own mood categories
- **History Feature**: Save and display previous mood detections
- **Visual Analytics**: Show graphs of mood patterns over time
- **Advanced Models**: Integrate more sophisticated sentiment analysis models

---

## 🔬 Technical Details

### Dependencies

- **Streamlit (v1.28.0+)**: Web framework for creating the user interface
- **TextBlob (v0.17.1+)**: Text processing library with built-in sentiment analysis

### Architecture

```
User Input → Safety Filter → TextBlob Analysis → Mood Classification → Output Display
```

### Code Structure

- `app.py`: Main application file containing all logic
  - `detect_mood()`: Core mood detection function
  - `contains_bad_words()`: Safety filtering function
  - `explain_how_it_works()`: Teacher Mode explanation
  - `main()`: Streamlit app entry point

### File Size
- Total repository size: < 5 MB
- All files are lightweight and optimized for quick loading

---

## 🌐 Deployment

### Deploying to Streamlit Cloud

1. **Push to GitHub**
   - Ensure all files are committed and pushed to your repository

2. **Sign up for Streamlit Cloud**
   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign up with your GitHub account

3. **Deploy Your App**
   - Click "New app"
   - Select your repository: `firstname-lastname-mood2emoji`
   - Set main file path: `app.py`
   - Click "Deploy"

4. **Share Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Share this link with students and educators

### Alternative Deployment Options
- **Heroku**: Container-based deployment
- **Replit**: Browser-based IDE with one-click deployment
- **PythonAnywhere**: Free hosting for Python web apps

---

## 🤝 Contributing

This is an educational project. If you'd like to improve it:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Suggested Improvements:**
- Expand bad word filter
- Add more mood categories
- Improve Teacher Mode explanations
- Add multilingual support
- Create student worksheets

---

## 📄 License

This project is created for educational purposes. Feel free to use and modify for teaching.

---

## 👤 Author

Created as part of the Curriculum Developer Intern assignment.

**Repository Name**: `firstname-lastname-mood2emoji`

---

## 🙏 Acknowledgments

- TextBlob library developers
- Streamlit team for the excellent framework
- Educational community for inspiration

---

## 📞 Support

For questions or issues:
1. Check the README for common solutions
2. Review the lesson plan for teaching guidance
3. Contact the repository maintainer

---

**Happy Learning! 😀🎓**

