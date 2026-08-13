import os
import gradio as gr
from google import genai
from datetime import datetime, timedelta


# ==========================================
# GEMINI API CONNECTION
# ==========================================

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.6-flash"


# ==========================================
# AI HEALTH CHATBOT
# ==========================================

def herhealth_chat(user_question):

    if not user_question or not user_question.strip():
        return "Please enter a health question."

    prompt = f"""
You are HerHealth AI, an educational Women's Health Companion.

Your purpose is to provide simple, understandable women's health information.

Rules:
1. Explain health topics in simple English.
2. Never diagnose a disease.
3. Do not prescribe medicines or dosages.
4. Provide educational information only.
5. Give general healthy lifestyle suggestions when appropriate.
6. If symptoms are severe, unusual, persistent, or concerning, recommend consulting a qualified healthcare professional.
7. Keep the response under 250 words.

Use this structure:

🌸 Simple Explanation

🥗 Healthy Tips

👩‍⚕️ When to Consult a Doctor

⚠️ Disclaimer:
This information is for educational purposes only and is not a substitute for professional medical advice.

User Question:
{user_question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Sorry, I couldn't generate a response right now.\n\nError: {str(e)}"


# ==========================================
# PERIOD TRACKER
# ==========================================

def period_tracker(last_period, cycle_length):

    try:
        if not last_period:
            return "Please enter your last period date."

        if not cycle_length:
            return "Please enter your cycle length."

        cycle_length = int(cycle_length)

        if cycle_length < 21 or cycle_length > 45:
            return "Please enter a cycle length between 21 and 45 days."

        last_date = datetime.strptime(
            last_period,
            "%Y-%m-%d"
        )

        next_period = last_date + timedelta(days=cycle_length)

        ovulation = next_period - timedelta(days=14)

        fertile_start = ovulation - timedelta(days=5)

        fertile_end = ovulation + timedelta(days=1)

        return f"""
🌸 Next Expected Period:
{next_period.strftime('%d %B %Y')}

🥚 Estimated Ovulation:
{ovulation.strftime('%d %B %Y')}

💖 Estimated Fertile Window:
{fertile_start.strftime('%d %B %Y')} to {fertile_end.strftime('%d %B %Y')}

⚠️ Note:
These are calendar-based estimates only. Menstrual cycles can vary from person to person, so these dates should not be considered medically accurate predictions.
"""

    except ValueError:
        return "❌ Please enter the date in YYYY-MM-DD format. Example: 2026-08-13"

    except Exception as e:
        return f"Something went wrong: {str(e)}"


# ==========================================
# LIFESTYLE PLANNER
# ==========================================

def lifestyle(age, height, weight):

    try:

        if not age or not height or not weight:
            return "Please enter your age, height and weight."

        age = float(age)
        height = float(height)
        weight = float(weight)

        if age <= 0 or height <= 0 or weight <= 0:
            return "Please enter valid positive values."

        bmi = weight / ((height / 100) ** 2)

        prompt = f"""
You are HerHealth AI, an educational Women's Health Companion.

User details:

Age: {age}
Height: {height} cm
Weight: {weight} kg
BMI: {bmi:.2f}

Create a simple general wellness plan.

Use this structure:

🥗 Healthy Diet
- Breakfast
- Lunch
- Dinner
- Healthy snack ideas

🏃 Exercise
- Simple daily activity
- Weekly activity goal

💧 Hydration
- General hydration guidance

😴 Sleep
- General sleep recommendation

😊 Stress Management
- 3 simple stress-management suggestions

⚠️ Disclaimer:
This is general educational wellness information and is not a substitute for professional medical advice.

Do not diagnose any medical condition.
Do not prescribe medication.
Keep the answer under 300 words.
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return f"""
📊 Calculated BMI: {bmi:.2f}

{response.text}
"""

    except Exception as e:
        return f"Sorry, something went wrong.\n\nError: {str(e)}"


# ==========================================
# GRADIO INTERFACE
# ==========================================

with gr.Blocks(
    title="HerHealth AI"
) as demo:

    gr.Markdown(
        """
        # 🌸 HerHealth AI

        ### AI-Powered Women's Health Companion

        HerHealth AI provides educational women's health information,
        menstrual cycle estimates and general lifestyle guidance.

        ⚠️ **Medical Disclaimer:** This application is for educational
        purposes only and does not replace professional medical advice.
        """
    )

    # ======================================
    # ASK AI TAB
    # ======================================

    with gr.Tab("🤖 Ask AI"):

        question = gr.Textbox(
            label="Ask Your Health Question",
            placeholder="Example: What is PCOS?",
            lines=3
        )

        answer = gr.Textbox(
            label="AI Response",
            lines=12
        )

        ask_btn = gr.Button(
            "Get Answer"
        )

        ask_btn.click(
            fn=herhealth_chat,
            inputs=question,
            outputs=answer
        )


    # ======================================
    # PERIOD TRACKER TAB
    # ======================================

    with gr.Tab("📅 Period Tracker"):

        last_period = gr.Textbox(
            label="Last Period Date (YYYY-MM-DD)",
            placeholder="Example: 2026-08-01"
        )

        cycle = gr.Number(
            label="Cycle Length (Days)",
            value=28
        )

        period_result = gr.Textbox(
            label="Period Prediction",
            lines=8
        )

        period_btn = gr.Button(
            "Calculate"
        )

        period_btn.click(
            fn=period_tracker,
            inputs=[last_period, cycle],
            outputs=period_result
        )


    # ======================================
    # LIFESTYLE PLANNER TAB
    # ======================================

    with gr.Tab("🥗 Lifestyle Planner"):

        age = gr.Number(
            label="Age"
        )

        height = gr.Number(
            label="Height (cm)"
        )

        weight = gr.Number(
            label="Weight (kg)"
        )

        lifestyle_result = gr.Textbox(
            label="Lifestyle Plan",
            lines=15
        )

        lifestyle_btn = gr.Button(
            "Generate Plan"
        )

        lifestyle_btn.click(
            fn=lifestyle,
            inputs=[age, height, weight],
            outputs=lifestyle_result
        )


    gr.Markdown(
        """
        ---
        **HerHealth AI** | Built with Python, Google Gemini API and Gradio

        *For educational purposes only.*
        """
    )


# ==========================================
# LAUNCH APPLICATION
# ==========================================

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000))
)
