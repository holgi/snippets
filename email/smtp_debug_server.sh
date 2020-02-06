""" run a local SMTP server for debugging

You need to change the SMTP server details in your
application settings to localhost:1025 or similar.
"""

# Non-root way to run debugging SMTP server.

python3 -m smtpd -n -c DebuggingServer localhost:1025

# If you want to bind SMTP port 25 you need to run this as a root:
# sudo python3  -m smtpd -n -c DebuggingServer localhost:25
