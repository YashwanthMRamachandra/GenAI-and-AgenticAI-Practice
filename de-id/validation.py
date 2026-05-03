import pandas as pd

# =========================
# FILE PATHS
# =========================
original_file = "data/sample_data.csv"
reid_file = "output/output_reid.csv"

# =========================
# LOAD DATA
# =========================
df_original = pd.read_csv(original_file)
df_reid = pd.read_csv(reid_file)

# =========================
# VALIDATION COLUMNS
# =========================
columns_to_check = ["UIM", "Agreement Number"]

# =========================
# VERIFY MATCH
# =========================
mismatch_count = 0

for col in columns_to_check:
    mismatches = df_original[col] != df_reid[col]
    count = mismatches.sum()
    
    if count > 0:
        print(f"❌ Column '{col}' has {count} mismatched rows")
        mismatch_count += count
    else:
        print(f"✅ Column '{col}' matches perfectly")

# =========================
# FINAL RESULT
# =========================
if mismatch_count == 0:
    print("\n🎉 SUCCESS: Re-identification is 100% accurate!")
else:
    print(f"\n⚠️ Total mismatches found: {mismatch_count}")