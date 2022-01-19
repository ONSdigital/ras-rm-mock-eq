# ras-rm-mock-eq
Mock EQ for rasrm dev testing

## Routes

Includes the following routes:
- GET `/` and `/session` - Simulate being sent to EQ
- GET `/v3/session` - Simulate being sent to EQ v3
- GET `/receipt` - Simulate the completion of an EQ (either version) by sending a message to case and redirecting
back to frontstage

