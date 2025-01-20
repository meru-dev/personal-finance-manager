# Personal Finance Manager

**Personal Finance Manager** is your assistant for managing your budget effectively.

This project is being developed as a pet project, utilizing modern technologies and design principles.

The development process is in the branch "develop".

## Setup
#### Temporary key generation for JWT tokens
```
mkdir jwt-keys
openssl genrsa -out jwt-keys/jwt-private.pem 2048
openssl rsa -in jwt-keys/jwt-private.pem -outform PEM -pubout -out jwt-keys/jwt-public.pem
```

#### Install deps
```commandline
uv venv
make up
```

## Features
- todo

## Technologies Used
- todo
