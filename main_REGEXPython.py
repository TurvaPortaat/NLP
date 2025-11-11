import re

#Task1

texts = [
    'Patient A reported using medication with code N02B01 for pain relief.',
    'Patient B was prescribed a drug with code A02B01 for their stomach.',
    'The report shows Patient C is taking medication with code B01AC06 for blood thinning.',
    'No ATC code is mentioned in the report for Patient D.'
]

# \s = space, t\ = tab

pattern = r"code\s*([A-Z]\d{2}[A-Z]\d{2}|[A-Z]\d{2}[A-Z]{2}\d{2})"

atc_codes = [code for item in texts for code in re.findall(pattern, item)]

print(atc_codes)