# # ussd_app/views.py

# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# import africastalking
# import os
# import logging

# # Set up logging for your view (MOVED TO TOP)
# logger = logging.getLogger(__name__)

# # Initialize Africa's Talking SDK (ensure these are loaded from environment variables in settings.py)
# username = os.getenv('AFRICAS_TALKING_USERNAME')
# api_key = os.getenv('AFRICAS_TALKING_API_KEY')

# # Basic check for credentials - important for production
# if not username or not api_key:
#     logger.error("Africa's Talking API credentials are not set in environment variables.")
#     # In a real app, you might want to raise an exception or gracefully degrade
#     # For now, we'll proceed, but operations might fail if credentials are truly missing.

# try:
#     africastalking.initialize(username, api_key)
#     sms = africastalking.SMS
# except Exception as e:
#     logger.error(f"Failed to initialize Africa's Talking SDK: {e}")
#     # Consider what to do if the SDK can't initialize (e.g., return an error response)


# # --- Constants for USSD Responses ---
# # Using constants makes the code cleaner and easier to modify
# USSD_CONTINUE = "CON "
# USSD_END = "END "

# # --- USSD Session Management (In-memory for demo, use DB for production) ---
# # For a production app, use a proper database (e.g., Django's ORM, Redis)
# # to store session state persistently. This dictionary will reset if the server restarts.
# user_sessions = {}

# @csrf_exempt # Africa's Talking will send POST requests, so disable CSRF for this view
# def ussd_callback(request):
#     if request.method == 'POST':
#         try:
#             # Retrieve USSD parameters from the POST request
#             session_id = request.POST.get('sessionId')
#             service_code = request.POST.get('serviceCode')
#             phone_number = request.POST.get('phoneNumber')
#             # The 'text' parameter holds the user's input for the current step.
#             # It can be empty for the first request or contain menu selections/text input.
#             text = request.POST.get('text', '').strip() # .strip() removes leading/trailing whitespace

#             logger.info(f"USSD Request - Session ID: {session_id}, Phone: {phone_number}, Input: '{text}'")

#             # --- Session State Management ---
#             # Retrieve or initialize session data for the current user
#             # In a real app, this would be loaded from a database based on session_id or phone_number
#             current_session_data = user_sessions.get(session_id, {'stage': 'main_menu'})

#             response_message = ""
#             session_stage = current_session_data['stage']

#             if session_stage == 'main_menu':
#                 if text == '':
#                     # First request in the session or returning to main menu
#                     response_message = "Welcome to SuperiaTech Learning!\n"
#                     response_message += "1. Learn a Topic\n"
#                     response_message += "2. Take a Quiz\n"
#                     response_message += "3. About Us"
#                     return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

#                 elif text == '1':
#                     # User chose "Learn a Topic"
#                     current_session_data['stage'] = 'learn_topic_input'
#                     user_sessions[session_id] = current_session_data # Update session state
#                     response_message = "What topic do you want to learn?\n"
#                     response_message += "E.g., Photosynthesis, Gravity, Fractions.\n"
#                     response_message += "Type your topic:"
#                     return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

#                 elif text == '2':
#                     # User chose "Take a Quiz"
#                     current_session_data['stage'] = 'quiz_topic_selection'
#                     user_sessions[session_id] = current_session_data # Update session state
#                     response_message = "Choose a quiz topic:\n"
#                     response_message += "1. Science\n"
#                     response_message += "2. Math\n"
#                     response_message += "3. History"
#                     return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

#                 elif text == '3':
#                     # User chose "About Us"
#                     response_message = "SuperiaTech Learning provides bite-sized education via SMS/USSD. Empowering students with knowledge. Visit superiatech.com for more.\n"
#                     response_message += "Thank you for using SuperiaTech!"
#                     # For "About Us", we usually end the session as it's a static info page.
#                     if session_id in user_sessions: # Safely remove
#                         del user_sessions[session_id]
#                     return HttpResponse(USSD_END + response_message, content_type='text/plain')

#                 else:
#                     # Invalid option for main menu
#                     response_message = "Invalid option. Please choose 1, 2, or 3."
#                     response_message += "\nDial *384*123# to return to main menu." # Guide user back
#                     if session_id in user_sessions: # Safely remove
#                         del user_sessions[session_id] # End session on invalid input
#                     return HttpResponse(USSD_END + response_message, content_type='text/plain')

#             elif session_stage == 'learn_topic_input':
#                 # This stage expects actual topic input. We'll handle sending the SMS in Phase 2.
#                 # For now, just acknowledge and end the session.
#                 # In Phase 2, this is where you'd call Gemini and send the SMS.

#                 # Assume 'text' now contains the topic (e.g., 'Photosynthesis')
#                 topic = text
#                 if not topic:
#                     response_message = "No topic provided. Please try again."
#                     if session_id in user_sessions: # Safely remove
#                         del user_sessions[session_id]
#                     return HttpResponse(USSD_END + response_message, content_type='text/plain')

#                 response_message = f"Getting information on '{topic}'. Please check your SMS inbox shortly for the explanation."
#                 response_message += "\nThank you for using SuperiaTech!"
#                 if session_id in user_sessions: # Safely remove
#                     del user_sessions[session_id] # Clear session once the request is processed

#                 # --- Placeholder for Phase 2: Call Gemini and send SMS ---
#                 # You will add code here in the next phase to:
#                 # 1. Call Gemini API with 'topic'
#                 # 2. Receive AI response
#                 # 3. Send AI response via Africa's Talking SMS API to 'phone_number'
#                 logger.info(f"Placeholder: AI lookup for topic '{topic}' for {phone_number}. Will send SMS.")
#                 # --- End Placeholder ---

#                 return HttpResponse(USSD_END + response_message, content_type='text/plain')

#             elif session_stage == 'quiz_topic_selection':
#                 # This stage expects a quiz topic selection (1, 2, or 3)
#                 quiz_topics = {
#                     '1': 'Science',
#                     '2': 'Math',
#                     '3': 'History'
#                 }
#                 selected_topic = quiz_topics.get(text)

#                 if selected_topic:
#                     current_session_data['stage'] = 'quiz_in_progress'
#                     current_session_data['quiz_topic'] = selected_topic
#                     user_sessions[session_id] = current_session_data # Update session state

#                     response_message = f"Starting {selected_topic} quiz. Look for the question via SMS. You will dial *384*123# again to answer."

#                     # --- Placeholder for Phase 3: Send first quiz question via SMS ---
#                     logger.info(f"Placeholder: Starting {selected_topic} quiz for {phone_number}. Sending first question via SMS.")
#                     # You will add code here in the next phase to:
#                     # 1. Call Gemini API to generate the first question
#                     # 2. Store the question and correct answer in session data
#                     # 3. Send the question via Africa's Talking SMS API to 'phone_number'
#                     # --- End Placeholder ---

#                     # End the USSD session here, as the user will receive an SMS and then redial
#                     return HttpResponse(USSD_END + response_message, content_type='text/plain')
#                 else:
#                     response_message = "Invalid quiz topic. Please choose 1, 2, or 3.\n"
#                     response_message += "Dial *384*123# to return to main menu."
#                     if session_id in user_sessions: # Safely remove
#                         del user_sessions[session_id] # End session on invalid input for quiz selection
#                     return HttpResponse(USSD_END + response_message, content_type='text/plain')

#             elif session_stage == 'quiz_in_progress':
#                 # This stage will handle quiz answers. (To be implemented in Phase 3)
#                 # For now, if they dial again in this state, it prompts for an answer.
#                 response_message = "You are in a quiz session. Please answer the question sent via SMS by redialing *384*123# and entering your answer.\n"
#                 response_message += "Example: A, B, C, or D.\n"
#                 response_message += "To exit quiz and return to main menu, dial *384*123# and type '0'." # Add a way to exit gracefully
#                 # You'll capture '0' in the next version to reset the session.
#                 return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')


#         except Exception as e:
#             # Log the full traceback for debugging
#             logger.exception(f"Error processing USSD request from {request.POST.get('phoneNumber', 'UNKNOWN')}: {e}")
#             # This is critical for robust error handling. Send a generic error message to the user.
#             error_message = "Sorry, an unexpected error occurred. Please try again later."
#             # Attempt to clear session if an error occurred during processing, to prevent stuck states
#             if session_id in user_sessions:
#                 del user_sessions[session_id]
#             return HttpResponse(USSD_END + error_message, content_type='text/plain')

#     else:
#         # Handle GET requests
#         logger.warning(f"Received non-POST request to USSD endpoint from {request.META.get('REMOTE_ADDR', 'UNKNOWN')}")
#         return HttpResponse("This endpoint only accepts POST requests.", status=405)

# ussd_app/views.py

# ussd_app/views.py

# ussd_app/views.py

# ussd_app/views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking
import os
import logging
import google.generativeai as genai
from django.conf import settings
from google.api_core import exceptions as google_api_exceptions

# Set up logging for your view
logger = logging.getLogger(__name__)

# Initialize Africa's Talking SDK
username = settings.AFRICAS_TALKING_USERNAME
api_key = settings.AFRICAS_TALKING_API_KEY

if not username or not api_key:
    logger.error("Africa's Talking API credentials are not set in environment variables. SMS operations may fail.")
try:
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
except Exception as e: # General exception for AT SDK errors
    logger.error(f"Failed to initialize Africa's Talking SDK. SMS operations may fail: {e}")

# Initialize Gemini API
gemini_api_key = settings.GEMINI_API_KEY
if not gemini_api_key:
    logger.error("Gemini API key is not set in environment variables. AI responses will not work.")
else:
    genai.configure(api_key=gemini_api_key)

# --- Constants for USSD Responses ---
USSD_CONTINUE = "CON "
USSD_END = "END "

# --- USSD Session Management (In-memory for demo, use DB for production) ---
user_sessions = {}

@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text', '').strip()

        logger.info(f"USSD Request - Session ID: {session_id}, Phone: {phone_number}, Input: '{text}'")

        # Retrieve or initialize session data
        current_session_data = user_sessions.get(session_id, {'stage': 'main_menu'})
        session_stage = current_session_data['stage']

        response_message = ""

        try:
            if session_stage == 'main_menu':
                if text == '':
                    response_message = "Welcome to SuperiaTech Learning!\n"
                    response_message += "1. Learn a Topic\n"
                    response_message += "2. Take a Quiz\n"
                    response_message += "3. About Us"
                    return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

                elif text == '1':
                    current_session_data['stage'] = 'learn_topic_input'
                    user_sessions[session_id] = current_session_data
                    response_message = "What topic do you want to learn?\n"
                    response_message += "E.g., Photosynthesis, Gravity, Fractions.\n"
                    response_message += "Type your topic:"
                    return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

                elif text == '2':
                    current_session_data['stage'] = 'quiz_topic_selection'
                    user_sessions[session_id] = current_session_data
                    response_message = "Choose a quiz topic:\n"
                    response_message += "1. Science\n"
                    response_message += "2. Math\n"
                    response_message += "3. History"
                    return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

                elif text == '3':
                    response_message = "SuperiaTech Learning provides bite-sized education via SMS/USSD. Empowering students with knowledge. Visit superiatech.com for more.\n"
                    response_message += "Thank you for using SuperiaTech!"
                    if session_id in user_sessions:
                        del user_sessions[session_id]
                    return HttpResponse(USSD_END + response_message, content_type='text/plain')

                else:
                    response_message = "Invalid option. Please choose 1, 2, or 3."
                    response_message += "\nDial " + service_code + " to return to main menu."
                    if session_id in user_sessions:
                        del user_sessions[session_id]
                    return HttpResponse(USSD_END + response_message, content_type='text/plain')

            elif session_stage == 'learn_topic_input':
                topic = text
                if not topic:
                    response_message = "No topic provided. Please try again."
                    if session_id in user_sessions:
                        del user_sessions[session_id]
                    return HttpResponse(USSD_END + response_message, content_type='text/plain')

                ai_explanation_sms = ""
                try:
                    # Call Gemini API
                    model = genai.GenerativeModel('gemini-2.0-flash')

                    prompt = (
                        f"Provide a concise, micro-learning explanation (max 140 characters, keep it very brief) "
                        f"for the following topic: '{topic}'. Do not include greetings or conversational filler."
                    )

                    gemini_response = model.generate_content(prompt)

                    ai_explanation_raw = gemini_response.text

                    if len(ai_explanation_raw) > 150:
                        ai_explanation_sms = ai_explanation_raw[:147] + "..."
                    else:
                        ai_explanation_sms = ai_explanation_raw

                    sms_sender = settings.SMS_SENDER_ID

                    if not sms_sender:
                        logger.error("SMS_SENDER_ID is not configured in settings.py. SMS cannot be sent.")
                        raise ValueError("SMS Sender ID is missing.")

                    # --- FIX: Changed sms.send() to pass message first, then recipients ---
                    # sms.send(
                    #     ai_explanation_sms,  # First positional argument: message content
                    #     [phone_number],      # Second positional argument: list of recipients
                    #     sender_id=sms_sender # sender_id as keyword argument (this should be okay)
                    # )

                    sms.send(
                        ai_explanation_sms,  # First positional argument: message content
                        [phone_number],      # Second positional argument: list of recipients
                        sender_id=sms_sender)

                    logger.info(f"Sent AI explanation SMS to {phone_number} for topic '{topic}'. Content: '{ai_explanation_sms}'")

                    response_message = f"Explanation for '{topic}' sent! Please check your SMS inbox shortly."
                    response_message += "\nThank you for using SuperiaTech!"

                except Exception as at_e: # General exception for AT SDK errors
                    logger.error(f"Africa's Talking SMS error sending explanation to {phone_number}: {at_e}")
                    response_message = "Sorry, failed to send the explanation SMS. Please try again later."

                except google_api_exceptions.NotFound as gemini_not_found_e:
                    logger.error(f"Gemini Model Not Found/Unsupported for topic '{topic}': {gemini_not_found_e}")
                    response_message = "Sorry, the AI model encountered an issue. Please try a different topic or try again later."
                except google_api_exceptions.GoogleAPIError as gemini_api_e:
                    logger.error(f"Generic Gemini API error for topic '{topic}': {gemini_api_e}")
                    response_message = "Sorry, the AI service encountered an issue. Please try again later."
                except Exception as gen_e: # Catch any other general exceptions during AI/SMS process
                    logger.error(f"General error during AI/SMS processing for topic '{topic}': {gen_e}")
                    response_message = "Sorry, something went wrong with the AI/SMS. Please try again."

                if session_id in user_sessions:
                    del user_sessions[session_id]
                return HttpResponse(USSD_END + response_message, content_type='text/plain')

            elif session_stage == 'quiz_topic_selection':
                quiz_topics = {
                    '1': 'Science',
                    '2': 'Math',
                    '3': 'History'
                }
                selected_topic = quiz_topics.get(text)

                if selected_topic:
                    current_session_data['stage'] = 'quiz_in_progress'
                    current_session_data['quiz_topic'] = selected_topic
                    user_sessions[session_id] = current_session_data

                    response_message = f"Starting {selected_topic} quiz. Look for the question via SMS. You will dial " + service_code + " again to answer."

                    logger.info(f"Placeholder: Starting {selected_topic} quiz for {phone_number}. Sending first question via SMS.")

                    return HttpResponse(USSD_END + response_message, content_type='text/plain')
                else:
                    response_message = "Invalid quiz topic. Please choose 1, 2, or 3.\n"
                    response_message += "Dial " + service_code + " to return to main menu."
                    if session_id in user_sessions:
                        del user_sessions[session_id]
                    return HttpResponse(USSD_END + response_message, content_type='text/plain')

            elif session_stage == 'quiz_in_progress':
                if text == '0':
                    response_message = "Quiz ended. Thank you for playing!\n"
                    response_message += "Dial " + service_code + " to return to the main menu."
                    if session_id in user_sessions:
                        del user_sessions[session_id]
                    return HttpResponse(USSD_END + response_message, content_type='text/plain')
                else:
                    response_message = "Please provide your answer (e.g., A, B, C, or D).\n"
                    response_message += "To exit quiz, dial " + service_code + " and type '0'."
                    return HttpResponse(USSD_CONTINUE + response_message, content_type='text/plain')

        except Exception as e:
            logger.exception(f"Unhandled error processing USSD request from {phone_number}: {e}")
            error_message = "Sorry, an unexpected error occurred. Please try again later."
            if session_id in user_sessions:
                del user_sessions[session_id]
            return HttpResponse(USSD_END + error_message, content_type='text/plain')

    else:
        logger.warning(f"Received non-POST request to USSD endpoint from {request.META.get('REMOTE_ADDR', 'UNKNOWN')}")
        return HttpResponse("This endpoint only accepts POST requests.", status=405)