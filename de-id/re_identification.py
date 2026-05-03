import base64
import pandas as pd
from google.cloud import dlp_v2

PROJECT_ID = "gen-lang-client-0609077635"
LOCATION = "global"

KMS_KEY_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/keyRings/deid-keyring/cryptoKeys/deid-key"

with open("wrapped_dek.bin", "rb") as f:
    wrapped_key = f.read()

wrapped_key_b64 = base64.b64encode(wrapped_key).decode("utf-8")

dlp = dlp_v2.DlpServiceClient()

# IMPORTANT: Read DE-IDENTIFIED file
df = pd.read_csv("output/output_deid.csv")

crypto_config = {
    "crypto_replace_ffx_fpe_config": {
        "crypto_key": {
            "kms_wrapped": {
                "wrapped_key": wrapped_key_b64,
                "crypto_key_name": KMS_KEY_NAME,
            }
        },
        "common_alphabet": "NUMERIC",
    }
}

reidentify_config = {
    "record_transformations": {
        "field_transformations": [
            {
                "fields": [{"name": "UIM"}],
                "primitive_transformation": crypto_config,
            },
            {
                "fields": [{"name": "Agreement Number"}],
                "primitive_transformation": crypto_config,
            },
        ]
    }
}

headers = [{"name": col} for col in df.columns]
rows = [{"values": [{"string_value": str(v)} for v in row]} for _, row in df.iterrows()]

item = {"table": {"headers": headers, "rows": rows}}

response = dlp.reidentify_content(
    request={
        "parent": f"projects/{PROJECT_ID}/locations/{LOCATION}",
        "reidentify_config": reidentify_config,
        "item": item,
    }
)

out_rows = response.item.table.rows
data = [[v.string_value for v in r.values] for r in out_rows]

df_reid = pd.DataFrame(data, columns=df.columns)
df_reid.to_csv("output/output_reid.csv", index=False)

print("✅ Re-ID completed")