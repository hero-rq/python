import hashlib
import base64
from cryptography.fernet import Fernet

username_trial = "GOUGH"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"

# Calculate SHA256 hash of the username
hash_object = hashlib.sha256(b"GOUGH")
hex_dig = hash_object.hexdigest()

# Generate dynamic part of the key
key_part_dynamic1_trial = hex_dig[4] + hex_dig[5] + hex_dig[3] + hex_dig[6] + hex_dig[2] + hex_dig[7] + hex_dig[1] + hex_dig[8]

# Combine parts to get the full key
key_full = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

# Convert key to base64
key_base64 = base64.b64encode(key_full.encode())

# Decrypt the full version
f = Fernet(key_base64)
full_version = b"gAAAAABgT_nv39GmDRYkPhrc2hba8UHCHnSTHqdFxXNdemW0svN2hYYw-6n56ErD3NrQYQlNL0sfdsGTmvWKxh5gVRGeCv5kNq-l6PpL0Fzzjo1x_E2Jjbw_xWKIwbvd7BRXFQZKnhs2ehcSEacqES4gsVMOExHUetxFtmYiHLMB0_kqueeT8zf_vcXAPzbiYA0hvD_QSAXzPiKwM2IsGpGzIS5O4_ODq6-knKszeQFstWKFNH_-jNAylCTWSQpPrWqJxCWhSINPhOZ9-PkBsy8lpqmksa6ZBCMvej4W9YFldupRHNoHUHzt8xScEvcsTzIgNmvzOsCBSf5GJG(중략)UPihTJC0Gsmm1FAlXtVOmuKYjwOV7DG4aPzE1MjDAHMWidls3ECcueaLdUV-oY6Hw3WwOK_Nnj10sPmWSFSuMPeOBwPEL2M-1tCkbOvilqccCAelhS87qU_fDUKzD68TV1tJIoXEKW4sdwAVGxguEv1BAm4G7LhrH08McB5n3ja5I_3IqkeYdyHaxAXJ-O2thg=="
full_version_code = f.decrypt(full_version)

# Print the decrypted code
print(full_version_code.decode())
