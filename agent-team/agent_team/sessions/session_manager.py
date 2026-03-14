from google.adk.sessions import InMemorySessionService

APP_NAME = "weather_tutorial_app"
USER_ID = "weather_user_1"
SESSION_ID = "weather_session_001"

_session_service = InMemorySessionService()
_session_initialized = False

async def get_or_create_session():
   global _session_initialized
   if not _session_initialized:
       await _session_service.create_session(
           app_name=APP_NAME,
           user_id=USER_ID,
           session_id=SESSION_ID,
       )
       _session_initialized = True
   return {
       "session_service": _session_service,
       "app_name": APP_NAME,
       "user_id": USER_ID,
       "session_id": SESSION_ID,
   }