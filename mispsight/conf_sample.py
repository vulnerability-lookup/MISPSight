misp_url = "https://misppriv.circl.lu/"
misp_key = ""
misp_verifycert = True

vulnerability_lookup_base_url = "https://vulnerability.circl.lu/"
vulnerability_auth_token = ""


# Hearbeat mechanism
heartbeat_enabled = True
valkey_host = "127.0.0.1"
valkey_port = 10002
expiration_period = 18000

# Optional: customize how a Sighting's "source" field is constructed
# Defaults: "MISP/<event_uuid>"
# source_prefix = "MISP"
# source_attribute = "event_uuid"
