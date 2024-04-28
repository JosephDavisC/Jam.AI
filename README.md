# Jam.AI - Your Personal Health Assistant for Managing Diabetes
<div style="text-align: center;">
    <img src="https://github.com/JosephDavisC/Jam.AI/assets/93409653/e18e9f32-11e7-4fec-8773-72a718e90cb1" alt="Jam Logo" style="width: 30%;">
</div>


## Team Members:

### Backend (PyCharm):
- Abraham
- Joseph

### Frontend (Figma):
- Michael

## App Description:

Jam.AI is your personal health assistant for managing diabetes. Using artificial intelligence, Jam.AI provides tailored guidance and support, helping you monitor blood sugar levels, offering nutritional advice, and sending medication reminders. With Jam.AI, managing your diabetes has never been easier.

## To run it locally:
1. Run `pip install -r requirements.txt` to install all required libraries.
2. Run flask by running `python app.py` in your terminal/command prompt.
3. Click the `http://127.0.0.1:5000/`
4. Here are some sample prompts:
   - I am 67 years old, diabetic, 180 cm tall, weigh 90 kg, and my blood sugar level is 186 mg/dl. Can I eat steak?
   - I am 35 years old, diabetic, 155 cm tall, weigh 60 kg, and my blood sugar level is 150 mg/dl. Can I eat 1 cup of cooked rice?
   - Who made you?
   - Were you made during the UWB hackathon?



## Functionality:

The user will be prompted to enter the following information:
- Blood glucose level (recent 1-2 hours)
- Weight
- Height
- Food in question
- Quantity of food

## Back-End Logic:

- Import OpenAI API, datasets in CSV.
- Pair food with sugar amount.

## Design Process & Visuals:
- Color focus on soft earthy colors for nutrition and health
- Friendly font to establish a friendly environment for the user 
- The colors were ensured to fit Adobe’s Accessibility Checks

- Inspired by ChatGPT design
- Conceptualized using Figma 
- Created using HTML, CSS, JavaScript, & Python
- Ensured functionality across mobile and desktop platforms
- Light/Dark mode & Clear History function

### User Flow:

1. User opens the website.
2. Greeted by the home page.
3. The site requests their specific diabetic information.
4. User inputs data.
5. The AI responds accordingly with information from trained datasets.
