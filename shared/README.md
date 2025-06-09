# Private/Public Keypairs for Testing

The Private/Public keypairs here are used **ONLY** for testing purposes. They absolutely shoud **NOT** be used in any production environment.

## Additional Information
To generate a new keypair, you can use the following command:

```bash
# CD into this 'shared' directory

# Generate a private key
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
# Generate a public key from the private key
openssl rsa -pubout -in private_key.pem -out public_key.pem
```