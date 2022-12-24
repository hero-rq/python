#BB84 quantum key distribution (QKD) protocol
import random

alice_key = [random.randint(0, 1) for _ in range(10)]

alice_basis = [random.randint(0, 1) for _ in range(10)]

bob_basis = [random.randint(0, 1) for _ in range(10)]

for alice_bit, alice_basis, bob_basis in zip(alice_key, alice_basis, bob_basis):
    if alice_basis == 0:
        alice_encoded_bit = (1 if alice_bit == 0 else 0)
    else:
        alice_encoded_bit = (0 if alice_bit == 0 else 1)


    if bob_basis == 0:
        bob_decoded_bit = (1 if alice_encoded_bit == 0 else 0)
    else:
        bob_decoded_bit = (0 if alice_encoded_bit == 0 else 1)


agreed_bits = [alice_key[i] for i in range(10) if alice_basis[i] == bob_basis[i]]

final_key = [agreed_bits[i] for i in range(len(agreed_bits)) if bob_decoded_bit[i] == agreed_bits[i]]

print(final_key)
