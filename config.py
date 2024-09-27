MERAKI_API_KEY = "9949c510ecfb423153921db03a31adc08487b9af"
ORG_NAME = "Health-Team-Advantage"
NETWORK_NAME = "HTA-Test"
# NETWORK_NAME = "Health-Team-Advantage-HTA-Wired-Network"

# Insert comma separated lists of acl names, where 'nat_set' are the acls which require nat translation (outside ->
# in), and outbound set is a normal MX outbound list (inside -> inside, or inside -> outside)
ACL_TYPES = {
  "nat_set": [
    "ACL_OUTSIDE_IN",
  ],
  "outbound_set": [
    "CLOUDTREK_VPN",
    "NIRVANA_HEALTH_VPN",
    "Beacon_ACL",
    "ConeHealth_ACL",
    "Envision_ACL",
    "inside_access_in",
    "vti-HTA-Connection-40.76.56.222_access_in",
  ]
}

# Hits
# "CLOUDTREK_VPN",
# "NIRVANA_HEALTH_VPN",
# "Beacon_ACL",
# "ConeHealth_ACL",
# "Envision_ACL",
# No Hits
# "outside_cryptomap",
# "TrizettoABQ_ACL",
# "TrizettoDEN1_ACL",
# "Sirius_ACL",
# "GDIT_ACL",
# "GDIT_2_ACL",
