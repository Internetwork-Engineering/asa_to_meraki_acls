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
    "ConeHealth_ACL",
    "Envision_ACL",
    "TrizettoABQ_ACL",
    "inside_access_in",
    "TrizettoDEN1_ACL",
    "Sirius_ACL",
    "GDIT_ACL",
    "outside_cryptomap",
    "NIRVANA_HEALTH_VPN",
    "NHVPNPKTCPTACL",
    "CLOUDTREK_VPN",
    "Beacon_ACL",
    "GDIT_2_ACL",
    "vti-HTA-Connection-40.76.56.222_access_in",
    "management_access_in",
  ]
}

