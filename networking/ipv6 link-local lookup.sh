""" Ping a complete ipv6 link local network
"""

# List the network interfaces on a Mac:

networksetup -listallhardwareports


# make the ping on link-local multicast

ping6 ff02::1%<interface> -c1


# for more link-local multicasts, see
# https://superuser.com/questions/1135757/scanning-in-ipv6


