# The realm, where users are allowed to login as administrators
SUPERUSER_REALM = ['super', 'administrators']
# Your database mysql://u:p@host/db
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Pa55w0rd@localhost:5432/privacy_idea'
# This is used to encrypt the auth_token
SECRET_KEY = 't0p s3cr3t'
# This is used to encrypt the admin passwords
PI_PEPPER = 'Never know...'
# This is used to encrypt the token data and token passwords
PI_ENCFILE = '/opt/conda/envs/privacyidea/lib/python3.7/site-packages/enckey'
# This is used to sign the audit log
PI_AUDIT_KEY_PRIVATE = '/opt/conda/envs/privacyidea/lib/python3.7/site-packages/private.pem'
PI_AUDIT_KEY_PUBLIC = '/opt/conda/envs/privacyidea/lib/python3.7/site-packages/public.pem'
# PI_AUDIT_MODULE = <python audit module>
# PI_AUDIT_SQL_URI = <special audit log DB uri>
# PI_LOGFILE = '....'
# PI_LOGLEVEL = 20
# PI_INIT_CHECK_HOOK = 'your.module.function'
# PI_CSS = '/location/of/theme.css'
# PI_UI_DEACTIVATED = True
