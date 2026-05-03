PROJECT_ID = 'gen-lang-client-0609077635'
LOCATION = 'us-west1'
MODEL_NAME = "gemini-2.5-pro" # Using a known stable model. Adjust if a different model is preferred/available.

DATASTORE_PATH = "projects/gen-lang-client-0609077635/locations/us/collections/default_collection/dataStores/practice-vertex-ai-search_1777432125471"


# gcloud projects add-iam-policy-binding gen-lang-client-0609077635 \
#   --member="user:yashwanth8890@gmail.com" \
#   --role="roles/aiplatform.user"

# gcloud projects add-iam-policy-binding gen-lang-client-0609077635 \
#   --member="user:yashwanth8890@gmail.com" \
#   --role="roles/discoveryengine.user"