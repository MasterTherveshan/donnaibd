import streamlit as st
import time
import re
from openai import OpenAI


def display_assistant():
    # ------------------------------
    # 1. Initialization
    # ------------------------------
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "thread_id" not in st.session_state:
        thread = client.beta.threads.create(
            tool_resources={"file_search": {"vector_store_ids": [st.secrets["VECTOR_STORE_ID"]]}}
        )
        st.session_state.thread_id = thread.id

    if "messages" not in st.session_state:
        st.session_state.messages = []

    assistant = client.beta.assistants.retrieve(st.secrets["ASSISTANT_ID"])

    # ------------------------------
    # 2. Layout
    # ------------------------------
    tab_layout = st.columns([3, 1])

    # Left column: main chat
    with tab_layout[0]:
        st.title("Welcome to the Assistant Page")

        # 2a) Show all existing conversation messages
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # 2b) Chat input at bottom
        if user_prompt := st.chat_input("Ask me anything about IBD structuring..."):
            # Display user bubble
            with st.chat_message("user"):
                st.write(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            # Send to LLM
            run_llm(client, assistant, user_prompt)
            st.rerun()  # Refresh the UI to show updated conversation

    # Right column: about & example questions
    with tab_layout[1]:
        st.markdown("""
            <div class="instruction-box">
                <h3>📚 About</h3>
                <p>Welcome to the Donna Q&A Section. This AI-powered tool helps with:</p>
                <ul>
                    <li>Product structuring queries</li>
                    <li>Documentation searches</li>
                    <li>Process guidance</li>
                    <li>Best practice advice</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='example-box'><h3>🔍 Example Questions</h3></div>", unsafe_allow_html=True)

        # Example question 1
        if st.button("What role does the FSCA play in structured finance?"):
            question = "What role does the Financial Sector Conduct Authority (FSCA) play in structured finance transactions in South Africa?"
            # Show user bubble
            with st.chat_message("user"):
                st.write(question)
            st.session_state.messages.append({"role": "user", "content": question})

            run_llm(client, assistant, question)
            st.rerun()

        # Example question 2
        if st.button("What are the typical risk management strategies for currency volatility?"):
            question = ("What are the typical risk management strategies employed by South African banks when dealing "
                        "with currency volatility in cross-border structured finance transactions?")
            with st.chat_message("user"):
                st.write(question)
            st.session_state.messages.append({"role": "user", "content": question})

            run_llm(client, assistant, question)
            st.rerun()

        # Example question 3
        if st.button("What are the differences between JSE Main Board and AltX listing requirements?"):
            question = (
                "What are the key differences in regulatory requirements between the JSE's Main Board and the AltX "
                "for listing structured finance products?")
            with st.chat_message("user"):
                st.write(question)
            st.session_state.messages.append({"role": "user", "content": question})

            run_llm(client, assistant, question)
            st.rerun()

        # Example question 4
        if st.button("How do SA Banks Act requirements shape SPV establishment?"):
            question = (
                "How do the South African Banks Act requirements shape the establishment and operation of SPVs used "
                "in structured finance transactions?")
            with st.chat_message("user"):
                st.write(question)
            st.session_state.messages.append({"role": "user", "content": question})

            run_llm(client, assistant, question)
            st.rerun()

        st.markdown("""
            <div class="instruction-box">
                <h3>⚠️ Important Notes</h3>
                <ul>
                    <li>All advice should be verified with your team</li>
                    <li>The assistant has access to approved documentation</li>
                    <li>Confidential information should not be shared</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def run_llm(client, assistant, user_prompt):
    """
    Send the user's question to the LLM, wait for the run to complete,
    display an assistant bubble with 'Thinking...' then final answer,
    and store the final answer in st.session_state.messages.
    """
    # 1) Create a thread message for the user prompt
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=user_prompt
    )

    # 2) Start a run
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=assistant.id
    )

    # 3) Create an assistant bubble
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.write("Thinking...")

        # 4) Wait until run completes
        while run.status != "completed":
            time.sleep(0.5)
            run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )

        # 5) Retrieve the new assistant message
        messages_resp = client.beta.threads.messages.list(
            thread_id=st.session_state.thread_id
        )
        # Typically the newest message is data[0]. If that merges Q&A, switch to data[-1].
        raw_assistant_msg = messages_resp.data[0].content[0].text.value

        cleaned_message = clean_response(raw_assistant_msg)
        placeholder.markdown(cleaned_message, unsafe_allow_html=True)

    # 6) Append the final answer to the chat history
    st.session_state.messages.append({"role": "assistant", "content": cleaned_message})


def clean_response(raw_text: str) -> str:
    """
    Clean references like [1], bracketed text, etc.
    """
    text = re.sub(r'\[\d+\]', '', raw_text)
    text = re.sub(r'\d+:\d+†[^】]*】', '', text)
    text = re.sub(r'【.*?】', '', text)
    text = re.sub(r'[【】]', '', text)

    # Break into sentences, do minimal reformat
    lines = text.split('.')
    formatted_lines = []
    for line in lines:
        if not line.strip():
            continue
        if re.match(r'^\s*\d+\s*', line):
            formatted_lines.append('\n' + line.strip() + '.')
        else:
            formatted_lines.append(line.strip() + '.')
    text = ' '.join(formatted_lines)
    text = re.sub(r'\n\s*\n', '\n', text)
    return text.strip()
