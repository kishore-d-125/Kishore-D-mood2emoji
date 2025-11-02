# Build a Mood2Emoji App – Lesson Plan

**Project Title:** Kid-safe Text-Mood Detector (Mood2Emoji App)  
**Target Audience:** Students aged 12-16  
**Duration:** 60 minutes  
**Subject Area:** Computer Science, Technology, Natural Language Processing  
**Difficulty Level:** Beginner to Intermediate

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. **Understand** the basic concept of text sentiment analysis and mood detection
2. **Explain** how computers can analyze human emotions from text
3. **Demonstrate** how to use the Mood2Emoji app to detect moods in sentences
4. **Identify** the components of a simple text classification system
5. **Recognize** the importance of safety filters in technology applications
6. **Apply** knowledge by predicting and testing mood outcomes for different sentences

---

## Materials Needed

### For Instructor:
- Computer with Python 3.9+ installed
- Streamlit app running (locally or deployed)
- Projector or large screen for demonstration
- Whiteboard or flip chart
- Markers for visual aids
- Timer/clock

### For Students:
- Computer or tablet with internet access (one per student or in pairs)
- Access to the Mood2Emoji app (via deployed link or local installation)
- Notebook or paper for notes (optional)
- Pen/pencil

### Optional:
- Student worksheets with prediction charts
- Printed examples of sentences for mood detection
- Sticky notes for quick feedback

---

## Lesson Flow

### **Phase 1: Introduction to Moods and Emojis (10 minutes)**

#### Opening Hook (3 minutes)
- **Engage students**: "Show me with an emoji how you're feeling right now!"
- **Collect responses**: Students share emojis (😀, 😐, 😞, etc.)
- **Transition question**: "How do you think a computer could understand how we feel from words?"

#### Introduction to the App (4 minutes)
- **Demonstrate live**: Show the Mood2Emoji app on projector
- **Quick demo**: Enter "I'm excited about the weekend!" 
  - Show result: Happy emoji 😀 with "Sounds happy!" message
- **Explain purpose**: "Today we're learning how computers can read text and understand emotions"

#### Set Learning Goals (3 minutes)
- **Share objectives**: Display or announce what students will learn
- **Connect to real-world**: 
  - "Have you noticed YouTube comments sorted by sentiment?"
  - "Ever seen movie reviews categorized as positive or negative?"
- **Create anticipation**: "By the end of class, you'll understand how this works!"

**Key Questions to Ask:**
- What words make you feel happy when you read them?
- Can you think of a sentence that sounds sad?
- How might computers use this technology in real life?

---

### **Phase 2: Basic Idea of Text Sentiment (10 minutes)**

#### Concept Introduction (5 minutes)

**Explain Sentiment Analysis:**
- **Definition**: "Sentiment analysis is when computers figure out if text sounds positive, negative, or neutral"
- **Simple analogy**: "Like a friend who reads your message and understands if you're happy or sad"
- **Visual aid**: Draw a simple diagram on whiteboard:

```
Text Input → Computer Analysis → Mood Output
   "I love pizza!"  →  😀 Happy  →  "Sounds happy!"
```

**Introduce Key Terms:**
- **Sentiment**: The feeling or emotion in text
- **Polarity Score**: A number from -1 to +1 that represents mood
  - Show number line: `-1 (sad) ... 0 (neutral) ... +1 (happy)`

#### Interactive Demonstration (5 minutes)

**Show Teacher Mode:**
- Toggle "Teacher Mode" in the app
- Enter example sentences and show polarity scores:

| Sentence | Polarity | Mood |
|----------|----------|------|
| "I love ice cream!" | +0.5 | Happy 😀 |
| "It's okay." | 0.0 | Neutral 😐 |
| "I'm worried about the test." | -0.3 | Sad 😞 |

**Interactive Quiz Activity:**
- Display sentence: "I'm so excited!"
- Ask: "What do you think the polarity score will be? Happy, neutral, or sad?"
- Reveal answer and discuss why

**Engage Students:**
- Ask for examples of happy words (love, excited, amazing)
- Ask for examples of sad words (worried, upset, disappointed)
- Connect to polarity: Happy words → positive polarity, Sad words → negative polarity

---

### **Phase 3: Walkthrough of the App (15 minutes)**

#### Feature Exploration (8 minutes)

**Navigate Interface Together:**

1. **Text Input Box** (2 min)
   - Show where to type
   - Explain placeholder text
   - Demonstrate with: "Today is a beautiful day!"

2. **Detect Mood Button** (2 min)
   - Show button location
   - Click and observe result
   - Point out emoji and message

3. **Results Display** (2 min)
   - Explain emoji meaning
   - Discuss the one-line message
   - Show how results change with different inputs

4. **Safety Features** (2 min)
   - Discuss why we need filters
   - Explain neutral fallback
   - Emphasize: "Safety is important in all technology!"

#### Guided Examples (4 minutes)

**Work Through Examples Together:**

**Example 1: Happy Mood**
- Input: "I love my new bike!"
- Process: Type together, predict outcome, click button
- Result: 😀 "Sounds happy!"
- Discussion: What words made it happy? (love, new)

**Example 2: Neutral Mood**
- Input: "Today is Monday."
- Process: Predict, test, observe
- Result: 😐 "Sounds neutral."
- Discussion: Why is it neutral? (no strong emotion words)

**Example 3: Sad Mood**
- Input: "I'm worried about my exam."
- Process: Predict, test, observe
- Result: 😞 "Sounds a bit sad."
- Discussion: What word indicates sadness? (worried)

#### Teacher Mode Deep Dive (3 minutes)

**Explore Internal Workings:**
- Toggle Teacher Mode on
- Read through the explanation panel together
- Point out:
  - Safety check step
  - Sentiment analysis process
  - Classification rules
  - Visual flow diagram

**Ask students to identify:**
- "What happens first?" (Safety check)
- "How does the computer analyze text?" (TextBlob, polarity score)
- "What determines the emoji?" (Polarity threshold)

---

### **Phase 4: Hands-On Coding/App Demo (20 minutes)**

#### Activity 1: Sentence Creation Challenge (8 minutes)

**Individual or Pair Work:**

**Task:** Create three sentences:
1. One that will be detected as **happy** 😀
2. One that will be detected as **neutral** 😐
3. One that will be detected as **sad** 😞

**Instructions:**
- Open the Mood2Emoji app
- Write each sentence
- Test it and verify it gives the correct mood
- If it doesn't match, try again!

**Share Results (2 minutes):**
- Call on 2-3 students to share their sentences
- Discuss why certain words work better than others
- Celebrate creative examples!

**Example Student Sentences:**
- Happy: "I'm thrilled about the school trip!"
- Neutral: "The weather is cloudy today."
- Sad: "I'm disappointed about the cancellation."

#### Activity 2: Mood Prediction Game (7 minutes)

**Interactive Game Format:**

**Round 1 - Easy Level (3 sentences, 3 min):**
- Display sentence on board/screen
- Students predict mood (raise hand: 😀, 😐, or 😞)
- Test in app and reveal answer
- Discuss why

**Sentences for Round 1:**
1. "I'm so happy today!"
2. "The cat sat on the mat."
3. "I feel terrible."

**Round 2 - Challenge Level (3 sentences, 4 min):**
- More complex sentences
- Students predict and justify their answer
- Test and discuss

**Sentences for Round 2:**
1. "It's not bad, I guess."
2. "I can't wait for summer vacation!"
3. "I'm not sure how I feel."

**Learning Moment:**
- Discuss why some sentences are harder (context, negation)
- Connect to real-world: "This is why sentiment analysis is still improving!"

#### Activity 3: Teacher Mode Investigation (5 minutes)

**Exploration Task:**

**Instructions:**
1. Toggle Teacher Mode ON
2. Enter a sentence of your choice
3. After getting the result, look at the explanation panel
4. Find the polarity score (if visible)
5. Answer: "What polarity score did your sentence get?"

**Group Discussion:**
- Compare polarity scores for different sentences
- Notice patterns: Happy sentences have positive scores, sad have negative
- Ask: "Why might scores vary even within the same mood category?"

**Extension for Advanced Students:**
- Challenge: Try to get a polarity score as close to 0 as possible (neutral)
- Challenge: Create a sentence with polarity above 0.5 (very happy)

---

### **Phase 5: Recap and Q&A (5 minutes)**

#### Review Key Concepts (3 minutes)

**Quick Recap Questions:**

1. **What is sentiment analysis?**
   - Answer: Computers analyzing text to understand emotions

2. **What is a polarity score?**
   - Answer: A number from -1 to +1 that shows how positive or negative text is

3. **How does the app work?**
   - Answer: Safety check → TextBlob analysis → Polarity calculation → Mood classification → Display result

4. **Why is safety important?**
   - Answer: To protect users from inappropriate content

**Real-World Connections:**
- "Where have you seen computers understand text before?"
  - Possible answers: Social media feeds, review sites, customer service chatbots
- "How could this technology help in real life?"
  - Possible answers: Mental health monitoring, customer feedback analysis, content moderation

#### Questions and Discussion (2 minutes)

**Open Floor for Questions:**
- Encourage students to ask about:
  - How the app works
  - Real-world applications
  - Limitations they noticed
  - Ideas for improvements

**Common Questions & Answers:**

**Q: Can the app understand sarcasm?**
- A: Not really! Sarcasm is tricky because "This is great!" said sarcastically sounds positive but means negative. This is a limitation!

**Q: What if I type in another language?**
- A: The app works best with English. Other languages might not work as accurately.

**Q: Can I add more moods like angry or excited?**
- A: Great idea! That would require modifying the code. Maybe a future project!

#### Wrap-Up and Next Steps

**Final Thoughts:**
- "You've learned about a real technology used by companies like Google and Facebook!"
- "Remember: computers understand text through algorithms and math, not magic!"
- "Keep experimenting with the app - try creative sentences and see what happens!"

**Encourage Further Learning:**
- "Try the app at home with different sentences"
- "Think about how you might improve it"
- "Consider: what other things could computers analyze in text?"

---

## Assessment

### Formative Assessment (During Lesson)

1. **Quick Checks:**
   - Can students predict moods before testing?
   - Do they understand polarity scores in Teacher Mode?
   - Can they explain why certain words affect mood?

2. **Observation:**
   - Are students engaged and experimenting?
   - Do they ask thoughtful questions?
   - Can they navigate the app independently?

### Summative Assessment (End of Lesson)

**Quick Exit Ticket (Optional, 2 minutes):**
Students write or say:
1. One thing they learned about sentiment analysis
2. One example of where this technology is used in real life
3. One question they still have

**Alternative Assessment:**
- Students create and test 3 sentences (happy, neutral, sad)
- Teacher verifies correct mood detection for each
- Students explain one sentence's polarity score (in Teacher Mode)

---

## Differentiation Strategies

### For Struggling Learners:
- Provide sentence templates to fill in
- Use more visual aids and demonstrations
- Pair with more advanced students
- Focus on interactive prediction game rather than technical details
- Simplify Teacher Mode explanations

### For Advanced Learners:
- Challenge: Try to "break" the app with confusing sentences
- Explore: Research how sentiment analysis is used in industry
- Extension: Discuss machine learning vs. rule-based systems
- Project idea: Design their own mood categories
- Critical thinking: Identify limitations and propose solutions

### For English Language Learners:
- Provide sentence examples in their language (if applicable)
- Use more visual demonstrations
- Simplify technical vocabulary
- Focus on interactive, hands-on activities
- Pair with native speakers for collaboration

---

## Extension Activities

### For Homework or Extra Time:

1. **Mood Journal (15 min):**
   - Students write 5 sentences about their day
   - Test each in the app
   - Reflect: Did the app understand their mood correctly?

2. **Research Project (30 min):**
   - Research: "How do companies use sentiment analysis?"
   - Find 3 real-world examples
   - Share findings with class

3. **Improvement Challenge (20 min):**
   - Students identify one limitation of the app
   - Brainstorm how to fix it
   - Present ideas (code not required)

4. **Creative Writing (15 min):**
   - Write a short story
   - Test key sentences in the app
   - Compare: Do the app's moods match the story's tone?

---

## Safety and Considerations

### Content Safety:
- The app includes basic profanity filtering
- Remind students to use appropriate language
- If inappropriate content appears, use it as a teaching moment about digital safety
- Have a plan for addressing any concerning student inputs (mental health resources)

### Technical Considerations:
- Ensure all students have internet access
- Have backup plan if app doesn't load (screenshots, video demo)
- Test app functionality before class
- Prepare for questions about technical implementation

### Classroom Management:
- Set expectations for appropriate language use
- Monitor student screens to ensure on-task behavior
- Use timer for activities to maintain pace
- Have extension activities ready for fast finishers

---

## Vocabulary List

**Key Terms for Students:**

1. **Sentiment**: The feeling or emotion expressed in text
2. **Polarity**: A measurement of how positive or negative text is (scale: -1 to +1)
3. **Classification**: Categorizing text into groups (happy, neutral, sad)
4. **Natural Language Processing (NLP)**: How computers understand human language
5. **Algorithm**: A set of rules or steps a computer follows
6. **Input**: What you put into the app (your sentence)
7. **Output**: What the app gives you (emoji and message)
8. **Safety Filter**: A system that blocks inappropriate content

---

## Troubleshooting

### Common Issues and Solutions:

**Issue:** App won't load
- **Solution**: Check internet connection, refresh page, try alternative device

**Issue:** Students getting unexpected results
- **Solution**: Discuss that sentiment analysis isn't perfect, explore why together

**Issue:** Technical terms too advanced
- **Solution**: Use simpler language, focus on concepts over terminology

**Issue:** Students entering inappropriate content
- **Solution**: Use as teaching moment, discuss digital citizenship, redirect to activity

**Issue:** Running out of time
- **Solution**: Prioritize hands-on activities, shorten discussion sections, assign research as homework

---

## Additional Resources

### For Students:
- App link: [To be provided when deployed]
- Simple NLP explainer videos (age-appropriate)
- Emoji usage guides

### For Instructors:
- TextBlob documentation (for technical questions)
- Streamlit documentation (for app customization)
- NLP educational resources for middle/high school

---

## Reflection and Improvement

### Post-Lesson Reflection Questions:

1. What worked well in this lesson?
2. Which activities were most engaging?
3. Where did students struggle?
4. What would I change for next time?
5. How can I extend this lesson further?

### Notes for Future Sessions:

- [ ] Track which sentences students find most interesting
- [ ] Note common misconceptions to address
- [ ] Collect student feedback on Teacher Mode
- [ ] Document technical issues for troubleshooting guide

---

## Appendices

### Appendix A: Sample Sentences

**Happy Sentences:**
- "I'm thrilled about the school trip!"
- "This is the best day ever!"
- "I love learning new things!"
- "I'm so excited for summer vacation!"

**Neutral Sentences:**
- "Today is Monday."
- "The weather is cloudy."
- "I have math class next period."
- "The book has 200 pages."

**Sad Sentences:**
- "I'm worried about the test."
- "I feel disappointed about the cancellation."
- "This is frustrating."
- "I'm not feeling well today."

### Appendix B: Quick Reference Guide

**For Students:**
```
How to Use Mood2Emoji:
1. Type a sentence in the text box
2. Click "Detect Mood"
3. See your emoji and message result
4. Try Teacher Mode to learn how it works!
```

**For Teachers:**
```
Key Thresholds:
- Polarity > 0.1  → Happy 😀
- Polarity -0.1 to 0.1 → Neutral 😐
- Polarity < -0.1 → Sad 😞
```

---

**Lesson Plan Prepared By:** [Your Name]  
**Date Created:** [Date]  
**Version:** 1.0  
**Last Updated:** [Date]

---

**End of Lesson Plan**

