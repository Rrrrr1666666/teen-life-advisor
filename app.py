import streamlit as st
from google import genai

st.set_page_config(page_title="Teen Life Advisor", page_icon="🌱", layout="centered")

st.title("🌱 مستشارك الذكي - Teen Life Advisor")
st.caption("مشروع STEAM: تطبيق ذكاء اصطناعي شامل لدعم المراهقين في تنظيم حياتهم.")

api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

advisor_mode = st.selectbox(
"اختر مجال الاستشارة اليوم:",
[
"🕌 التقرب إلى الله والدين (الصلاة والروحانيات)",
"💰 إدارة المال والمصروف اليومي",
"📅 تنظيم الوقت والدراسة",
"🎯 التخلص من العادات السيئة وبناء عادات إيجابية",
"🧘 العناية بالنفس والصحة النفسية"
]
)

system_instructions = {
"🕌 التقرب إلى الله والدين (الصلاة والروحانيات)": "أنت مرشد ديني وروحاني دافئ ومحبب للمراهقين. ساعدهم على الالتزام بالصلاة والقرآن بأسلوب مشجّع وميسّر.",
"💰 إدارة المال والمصروف اليومي": "أنت مستشار مالي للمراهقين. قدم نصائح لادخار المصروف وتجنب الشراء العاطفي بأسلوب بسيط.",
"📅 تنظيم الوقت والدراسة": "أنت مستشار تنظيم وقت للمراهقين. قدم نصائح عملية لجدولة المهام بذكاء بدون توتر.",
"🎯 التخلص من العادات السيئة وبناء عادات إيجابية": "أنت مدرب تطوير عادات. ساعدهم على استبدال العادات السلبية بأخرى إيجابية تدريجياً.",
"🧘 العناية بالنفس والصحة النفسية": "أنت مرشد داعم للمراهقين. قدم نصائح للتعامل مع التوتر والنوم الصحي والتوازن النفسي."
}

if "messages" not in st.session_state:

    st.session_state.messages = []

for msg in st.session_state.messages:
with st.chat_message(msg["role"]):
st.markdown(msg["content"])

if user_input := st.chat_input("اكتب سؤالك أو ما تريد الاستشارة فيه..."):
st.session_state.messages.append({"role": "user", "content": user_input})
with st.chat_message("user"):
st.markdown(user_input)

prompt = f"{system_instructions[advisor_mode]}\n\nسؤال الطالب: {user_input}"

with st.chat_message("assistant"):
response = client.models.generate_content(
model='gemini-2.5-flash',
contents=prompt
)
st.markdown(response.text)
st.session_state.messages.append({"role": "assistant", "content": response.text})
