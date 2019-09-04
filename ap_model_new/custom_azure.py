from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'popogstorage'  # Must be replaced by your <storage_account_name>
    account_key = 'nP5hHPR2a8UbFPiNnhgB1AwKoeI+X8X+Gat0BOK9xlnSVYzm657Y5sMWbDLkP3stRHWvLMnX15nVWYiZLYEekw=='  # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'popogstorage'  # Must be replaced by your storage_account_name
    account_key = 'AmtSC7H8vhc5FNLnYheoMplQ+8dR3J7S/VyEPuZvRg2NBm+pz7bakPaFxxPS/Q28++1yBeoBDivozHhf9jyQlA=='  # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None