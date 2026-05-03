gcloud kms keyrings create deid-keyring \
  --location=global

gcloud kms keys create deid-key \
  --location=global \
  --keyring=deid-keyring \
  --purpose=encryption

openssl rand -base64 32 > dek.txt

gcloud kms encrypt \
  --location=global \
  --keyring=deid-keyring \
  --key=deid-key \
  --plaintext-file=dek.txt \
  --ciphertext-file=wrapped_dek.bin

gcloud beta services identity create \
  --service=dlp.googleapis.com \
  --project=<project-id>

gcloud kms keys add-iam-policy-binding deid-key \
  --location=global \
  --keyring=deid-keyring \
  --member="serviceAccount:service-<project_number>@dlp-api.iam.gserviceaccount.com" \
  --role="roles/cloudkms.cryptoKeyDecrypter"